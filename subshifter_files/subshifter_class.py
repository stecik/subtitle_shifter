import datetime

class SubShifter:

    def shift(self, filename, hours, minutes, seconds):
        list_of_lines = self._read_file(filename)

    def _read_file(self, filename):
        list_of_lines = []
        line_counter = 0
        with open(filename, "r") as f:
            block = []
            for line in f.readlines():
                if line == "\n":
                    list_of_lines.append(block)
                    block = []
                    line_counter = 0
                    continue
                else:
                    line_counter += 1
                    if line_counter == 2:
                        origin, end = self._str_to_datetime(line)
                        # continue here
                    else:
                        block.append(line)
        return list_of_lines

    def _str_to_datetime(self, line):
        origin, end = line.strip().split(" --> ")
        origin = datetime.datetime.strptime(origin, "%H:%M:%S,%f").time()
        end = datetime.datetime.strptime(end, "%H:%M:%S,%f").time()
        # print(origin)
        # print(end)
        return origin, end

    def _datetime_to_str(self, origin, end):
        pass

    def _generate_shifted_file(self, list_of_lines, filename):
        with open(filename, "w") as f:
            pass

    def _generate_filename(self, filename):
        pass