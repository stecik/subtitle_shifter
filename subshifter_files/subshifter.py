from subshifter_class import SubShifter
from parser import args

if __name__ == "__main__":
    subshifter = SubShifter()
    try:
        subshifter.shift(args.input_file, args.hrs, args.min, args.sec, args.mil)
    except Exception as e:
        print(f"Error: {e}")

