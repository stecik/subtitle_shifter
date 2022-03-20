class SubShifter:

    def shift(self, filename, hours, minutes, seconds, milliseconds):
        list_of_lines = self._read_file(filename, hours, minutes, seconds, milliseconds)
        self._generate_shifted_file(list_of_lines, self._generate_filename(filename))

    def _read_file(self, filename, hours, minutes, seconds, milliseconds):
        list_of_lines = []
        line_counter = 0
        with open(filename, "r") as f:
            block = []
            for line in f:
                if line == "\n":
                    list_of_lines.append(block)
                    block = []
                    line_counter = 0
                    continue
                else:
                    line_counter += 1
                    if line_counter == 2:
                        origin, end = self._prepare_for_shift(line)
                        origin = self._shift_time(origin, hours, minutes, seconds, milliseconds)
                        end = self._shift_time(end, hours, minutes, seconds, milliseconds)
                        time_line = f"{origin} --> {end}\n"
                        block.append(time_line)
                    else:
                        block.append(line)
            list_of_lines.append(block)
        return list_of_lines

    def _prepare_for_shift(self, line):
        line = line.replace(",", ":")
        origin, end = line.strip().split(" --> ")
        return origin, end

    def _generate_shifted_file(self, list_of_lines, filename):
        with open(filename, "w") as f:
            for block in list_of_lines:
                for line in block:
                    f.write(line)
                f.write("\n")

    def _generate_filename(self, filename):
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
        time_hrs, time_min, time_sec, time_msec = list(map(int, time.strip().split(":")))
        zeroes = []

        time_msec += milliseconds
        s, ms = divmod(time_msec, 1000)
        time_msec = str(ms)
        zeroes = self._check_zeroes(time_msec, 3, zeroes)

        time_sec += seconds + s
        m, s = divmod(time_sec, 60)
        time_sec = str(s)
        zeroes = self._check_zeroes(time_sec, 2, zeroes)

        time_min += minutes + m
        h, m = divmod(time_min, 60)
        time_min = str(m)
        zeroes = self._check_zeroes(time_min, 2, zeroes)

        time_hrs += hours + h
        time_hrs = str(time_hrs)
        zeroes = self._check_zeroes(time_hrs, 2, zeroes)
        return f"{zeroes[-1]}{time_hrs}:{zeroes[-2]}{time_min}:{zeroes[-3]}{time_sec},{zeroes[-4]}{time_msec}"

    def _check_zeroes(self, time, length, l):
        if len(time) < length:
            l.append("0" * (length - len(time)))
            return l
        l.append("")
        return l