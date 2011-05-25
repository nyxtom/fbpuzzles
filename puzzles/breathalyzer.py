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

    def soundex(self, name, len=4):
        """ 
        soundex module conforming to Knuth's algorithm
        implementation 2000-12-24 by Gregory Jorgensen
        public domain
        """
        # digits holds the soundex values for the alphabet
        digits = '01230120022455012623010202'
        sndx = ''
        fc = ''

        # translate alpha chars in name to soundex digits
        for c in name.upper():
            if c.isalpha():
                if not fc: fc = c   # remember first letter
                d = digits[ord(c)-ord('A')]
                # duplicate consecutive soundex digits are skipped
                if not sndx or (d != sndx[-1]):
                    sndx += d

        # replace first digit with first alpha character
        sndx = fc + sndx[1:]

        # remove all 0s from the soundex code
        sndx = sndx.replace('0','')

        # return soundex code padded to len characters
        return (sndx + (len * '0'))[:len]

    def levenshtein(self, s1, s2):
        """
        Measures the distance between two strings defined as the minimum number of edits
        needed to transform one string into another using only insertion, deletion or substitution 
        of a single character. A follow-up to this (including the possibility of using transposition) 
        is the Damerau-Levenshtein distance algorithm.

        http://en.wikipedia.org/wiki/Levenshtein_distance
        http://en.wikipedia.org/wiki/Damerau-Levenshtein_distance
        """
        len1 = len(s1)
        len2 = len(s2)
        if len1 < len2:
            return self.levenshtein(s2, s1)
        if not s1:
            return len2

        previous_row = xrange(len2 + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row

        return previous_row[-1]


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
