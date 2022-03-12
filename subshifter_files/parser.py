import argparse
from constants import DESCRIPTION, PROGRAM_SHORTCUT
import os

# Functions
def integer(arg):
    # limits arguments to positive integers
    try:
        argument = int(arg)
    except ValueError:
        raise argparse.ArgumentTypeError("Must be an integer")
    return argument

parser = argparse.ArgumentParser(prog=PROGRAM_SHORTCUT, description=DESCRIPTION)

parser.add_argument("input_file", type=str, required=True, help="Specify intput file name")

parser.add_argument("-s", "--sec", type=integer, default=0, help="Time for resync in seconds")
parser.add_argument("-m", "--min", type=integer, default=0, help="Time for resync in seconds")
parser.add_argument("-h", "--hrs", type=integer, default=0, help="Time for resync in seconds")
parser.add_argument("-f", "--format", type=str, default="srt", help="Specify file format (extension)")

args = parser.parse_args()