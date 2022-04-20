import argparse
from constants import DESCRIPTION, PROGRAM_SHORTCUT

# Functions
def integer(arg):
    # limits arguments to integers
    try:
        argument = int(arg)
    except ValueError:
        raise argparse.ArgumentTypeError("Must be an integer")
    return argument

parser = argparse.ArgumentParser(prog=PROGRAM_SHORTCUT, description=DESCRIPTION)

# positional arguments
parser.add_argument("input_file", type=str, help="Specify intput file name")

# optional arguments
parser.add_argument("-m", "--mil", type=integer, default=0, help="Time for resync in milliseconds")
parser.add_argument("-s", "--sec", type=integer, default=0, help="Time for resync in seconds")
parser.add_argument("-M", "--min", type=integer, default=0, help="Time for resync in minutes")
parser.add_argument("-H", "--hrs", type=integer, default=0, help="Time for resync in hours")
parser.add_argument("-f", "--filetype", default="srt", help="Output file type [srt/sub]")

args = parser.parse_args()