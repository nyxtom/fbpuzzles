#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
colors = dict(red="\033[1;31m", nc="\033[0m")

def print_error(message):
    """
    Prints the appropriate error message to the user
    in full red color as it should be.
    """
    print '%s%s%s' % (colors['red'], message, colors['nc'])


class Puzzle(object):
    """
    Defines the breathalyzer puzzle implementation.
    """
    
    def run(self, input):
        """
        Given an example sentence input. This will 
        run the appropriate distance formula for 
        approximating correctness for the solution.
        """
        pass


if __name__ == "__main__":
    if not len(sys.argv) > 1:
        print_error('You must provide an input filename')
    else:
        try:
            with open(sys.argv[1]) as input_file:
                input = input_file.read()
                runner = Puzzle()
                runner.run(input)
        except IOError as e:
            print_error(e)
