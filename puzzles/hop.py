class Puzzle(object):
    """
    Defines the Hoppity Hop puzzle implementation.
    """
    def run(self, input):
        """
        Runs the puzzle given the expected input.
        """
        value = self.resolve_digits(input)
        self.loop(value)

    def resolve_digits(self, text):
        """
        Resolves the given text to an integer.
        """
        text = text.strip()
        if text.isdigit():
            return int(text)
        else:
            raise ValueError('Input must contain a numeric value')

    def print_hop(self, value):
        """
        Prints the given value based on a set of rules.
        """
        if value % 15 == 0:
            return 'Hop'
        elif value % 5 == 0:
            return 'Hophop'
        elif value % 3 == 0:
            return 'Hoppity'
        else:
            return None

    def loop(self, value):
        """
        Loops over the given range, printing the expected output per iteration.
        """
        for i in xrange(1, value+1):
            result = self.print_hop(i)
            if result:
                print result
