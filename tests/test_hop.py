from unittest import TestCase
from sure import that

class HopTestCase(TestCase):

    def setUp(self):
        from puzzles.hoppity import Puzzle
        self.runner = Puzzle()

    def test_hop_puzzle_runs(self):
        """
        Test case to ensure that the hop puzzle exists and runs.
        """
        self.runner.run("    \n15   \n")
        pass

    def print_hop(self, digits):
        return self.runner.print_hop(digits)

    def test_resolve_digits(self):
        """
        Test case with whitespace characters
        """
        result = self.runner.resolve_digits('   \n    15      \n\n\n')
        assert that(result).equals(15), 'Resolve digits should handle whitespace characters'

    def test_hop_divisible_three(self):
        """
        Test case for integers divisible by three
        """
        result = self.print_hop(12)
        assert that(result).equals('Hoppity'), 'For integers divisible by 3, print Hoppity'

    def test_hop_divisible_five(self):
        """
        Test case for integers divisible by five
        """
        result = self.print_hop(10)
        assert that(result).equals('Hophop'), 'For integers divisible by 5, print Hophop'

    def test_hop_divisible_three_five(self):
        """
        Test case for integers divisible by both three and five
        """
        result = self.print_hop(15)
        assert that(result).equals('Hop'), 'For integers divisible by both 3 & 5, print Hop'

    def test_hop_print_none(self):
        """
        Test case to ensure that print hop returns nothing on non divisible integers
        """
        result = self.print_hop(7)
        assert not result, 'Print hop should print nothing on non divisible integers'
