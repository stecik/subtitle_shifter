class SubShifter:

    def shift(self, filename, hours, minutes, seconds, milliseconds):
        # resyncs file by given time
        # convert time to milliseconds
        millis = self._time_to_millis(hours, minutes, seconds, milliseconds)
        name, extension = self._separate_file_extension(filename)
        if extension == "srt":
            list_of_lines = self._read_srt_file(filename, millis)
            self._generate_shifted_srt_file(list_of_lines, self._generate_filename(filename))
            print("srt")
        elif extension == "sub":
            list_of_lines = self._read_sub_file(filename, millis)
            self._generate_shifted_sub_file(list_of_lines, self._generate_filename(filename))
            print("sub")

    def _read_srt_file(self, filename, millis):
        # opens specified file and reads each line
        list_of_lines = []
        line_counter = 0
        with open(filename, "r") as f:
            block = []
            for line in f:
                # if line is a separator appends block and resets it
                if line == "\n":
                    list_of_lines.append(block)
                    block = []
                    line_counter = 0
                    continue
                else:
                    line_counter += 1
                    # if line contains time values, shift it
                    if line_counter == 2:
                        # separate origin and end
                        origin, end = self._prepare_for_shift(line)
                        # resync
                        origin = self._shift_time(origin, millis)
                        end = self._shift_time(end, millis)
                        # give proper format and append
                        time_line = f"{origin} --> {end}\n"
                        block.append(time_line)
                    else:
                        # line contains text
                        block.append(line)
            # solves the last block in a file
            list_of_lines.append(block)
        return list_of_lines

    def _read_sub_file(self, filename, millis):
        list_of_lines = []
        with open(filename, "r") as f:
            for line in f:
                origin, end, text = self._separate_sub_line(line)
                origin, end = self._shift_sub_line(origin, end, millis)
                line_connected = "{" + str(origin) + "}" + "{" + str(end) + "}" + text
                list_of_lines.append(line_connected)
        return list_of_lines

    def _separate_sub_line(self, line):
        origin, end, text = line.strip().split("}")
        origin = int(origin.strip().replace("{", ""))
        end = int(end.strip().replace("{", ""))
        return origin, end, text

    def _shift_sub_line(self, origin, end, millis):
        return origin + millis, end + millis

    def _prepare_for_shift(self, line):
        # changes time format for calculations
        line = line.replace(",", ":")
        origin, end = line.strip().split(" --> ")
        return origin, end

    def _generate_shifted_srt_file(self, list_of_lines, filename):
        # generates resynchronized srt file
        with open(filename, "w") as f:
            for block in list_of_lines:
                for line in block:
                    f.write(line)
                f.write("\n")

    def _generate_shifted_sub_file(self, list_of_lines, filename):
        # generates resynchronized sub file
        with open(filename, "w") as f:
            for line in list_of_lines:
                f.write(line)
                f.write("\n")

    def _generate_filename(self, filename):
        # generates new filename for output file
        name, ext = self._separate_file_extension(filename)
        return f"{name}_shifted.{ext}"

    def _separate_file_extension(self, filename):
        # Returns separated file name and file extension
        extension = ""
        i = 1
        symbol = filename[-i]
        while symbol != ".":
            extension += symbol
            i += 1
            symbol = filename[-i]
        name = filename[:len(filename) - i]
        return name, extension[::-1]

    def _shift_time(self, time, millis):
        # resyncs time by given values
        time = list(map(int, time.strip().split(":")))
        zeroes = []

        # calculates time in milliseconds
        time_in_millis = self._time_to_millis(time[0], time[1], time[2], time[3])
        new_time = time_in_millis + millis

        # list of new time values [hrs, min, sec, millis]
        new_time = list(self._millis_to_time(new_time))

        # checks for number of figures of each value, adds zero where necessary
        for i in range(0, len(new_time) - 1):
            zeroes = self._check_zeroes(new_time[i], 2, zeroes)
        zeroes = self._check_zeroes(new_time[3], 3, zeroes)

        return f"{zeroes[0]}{new_time[0]}:{zeroes[1]}{new_time[1]}:{zeroes[2]}{new_time[2]},{zeroes[3]}{new_time[3]}"

    def _time_to_millis(self, h, m, s, ms):
        # calculates time in milliseconds
        return ms + s * 1000 + m * 60000 + h * 3600000

    def _millis_to_time(self, millis):
        # transfers time in milliseconds into hrs, min, sec, millis
        hours, rest = divmod(millis, 3600000)
        minutes, rest = divmod(rest, 60000)
        seconds, rest = divmod(rest, 1000)
        millis = rest
        return hours, minutes, seconds, millis

    def _check_zeroes(self, time, length, l):
        # checks for number of figures of each value, appends necessary zeroes to a list
        time = str(time)
        if len(time) < length:
            l.append("0" * (length - len(time)))
            return l
        l.append("")
        return l