import argparse
from constants import DESCRIPTION, PROGRAM_SHORTCUT

# Functions
def length_value_limit(arg):
    # limits arguments to positive integers
    try:
        argument = int(arg)
    except ValueError:
        raise argparse.ArgumentTypeError("Must be an integer")
    if argument < 0:
        raise argparse.ArgumentTypeError("Argument must be positive")
    return argument

parser = argparse.ArgumentParser(prog=PROGRAM_SHORTCUT, description=DESCRIPTION)


args = parser.parse_args()