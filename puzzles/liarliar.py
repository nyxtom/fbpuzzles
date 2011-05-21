#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
colors = dict(red="\033[1;31m", nc="\033[0m")

def print_error(message):
    """
    Prints the appropriate error message to the user
    in full red color as it should be.
    """
    print '%s%s%s' % (colors['red'], message, colors['nc'])


class Puzzle(object):
    """
    Defines the liar liar puzzle implementation.
    """
    def run(self, lines):
        """
        Runs through the given input to create 
        an aggregate result of liars/non-liars.
        """
        success, result = self.is_valid(lines)
        if not success:
            print_error(result)
            return

        print '%s %s' % self.tally(result)

    def is_valid(self, lines):
        """
        Ensures that the given input is validated and 
        if not, then the appropriate error message 
        result will be displayed to the user.
        """
        if not lines:
            return False, 'You must provide a valid input file'

        if not lines[0].strip().isdigit():
            return False, 'The first line in the input should be the count'

        lines = [line.strip() for line in lines]

        matches = []
        for line in lines[1:]:
            m = re.match(r'(?P<name>[A-Za-z]+)(\s+(?P<count>\d+))?', line)
            if not m:
                return False, 'All lines must contain a valid name and/or count match'
            else:
                matches.append(m.groupdict())

        return True, matches

    def tally(self, matches):
        """
        Tallies the given matches in the order they were given 
        to determine the number of people accused versus non-accused.
        """
        pot = set()
        accused = set()
        for m in matches:
            count, name = m.values()
            if not count and name not in accused:
                accused.add(name)
                if name in pot:
                    pot.remove(name)
            elif count and name not in accused:
                pot.add(name)

        return len(accused), len(pot)


# Puzzle runner boilerplate
if __name__ == "__main__":
    if not len(sys.argv) > 1:
        print_error('You must provide an input filename')
    else:
        try:
            with open(sys.argv[1]) as input_file:
                input = input_file.readlines()
                runner = Puzzle()
                runner.run(input)
        except IOError as e:
            print_error(e)
