from subshifter_class import SubShifter
from parser import args

if __name__ == "__main__":
    subshifter = SubShifter()
    # subshifter.shift("test.srt", 10, 62, 63, 1200)
    subshifter.shift(args.input_file, args.hrs, args.min, args.sec, args.mil)
