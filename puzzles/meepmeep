#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Puzzle(object):
    """
    Defines the Meep meep puzzle implementation.
    """
    def run(self, input):
        """
        Given garbage input, print the statement appropriately.
        """
        print self.print_meep(input)

    def print_meep(self, input):
        """
        Prints the output Meep meep.
        """
        return 'Meep meep!'

# Puzzle runner boilerplate
if __name__ == "__main__":
    import sys
    colors = dict(
        red="\033[1;31m",
        nc="\033[0m"
    )
    if not len(sys.argv) > 1:
        print '%sYou must provide an input filename%s' % (colors['red'], colors['nc'])
    else:

        # Since this particular puzzle will throw away input, just call run with nothing
        runner = Puzzle()
        runner.run('')
