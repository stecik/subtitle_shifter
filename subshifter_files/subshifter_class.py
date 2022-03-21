class SubShifter:

    def shift(self, filename, hours, minutes, seconds, milliseconds):
        # resyncs file by given time
        list_of_lines = self._read_file(filename, hours, minutes, seconds, milliseconds)
        self._generate_shifted_file(list_of_lines, self._generate_filename(filename))

    def _read_file(self, filename, hours, minutes, seconds, milliseconds):
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
                        origin = self._shift_time(origin, hours, minutes, seconds, milliseconds)
                        end = self._shift_time(end, hours, minutes, seconds, milliseconds)
                        # give proper format and append
                        time_line = f"{origin} --> {end}\n"
                        block.append(time_line)
                    else:
                        # line contains text
                        block.append(line)
            # solves the last block in a file
            list_of_lines.append(block)
        return list_of_lines

    def _prepare_for_shift(self, line):
        # changes time format for calculations
        line = line.replace(",", ":")
        origin, end = line.strip().split(" --> ")
        return origin, end

    def _generate_shifted_file(self, list_of_lines, filename):
        # generates resynchronized srt file
        with open(filename, "w") as f:
            for block in list_of_lines:
                for line in block:
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

    def _shift_time(self, time, hours, minutes, seconds, milliseconds):
        # resyncs time by given values
        time = list(map(int, time.strip().split(":")))
        zeroes = []

        # calculates time in milliseconds
        time_in_millis = self._time_to_millis(time[0], time[1], time[2], time[3])
        time_plus_in_millis = self._time_to_millis(hours, minutes, seconds, milliseconds)
        new_time = time_in_millis + time_plus_in_millis

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