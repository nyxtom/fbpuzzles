from unittest import TestCase
from sure import that

class HopTestCase(TestCase):

    def test_hop_puzzle_exists(self):
        """
        Test case to ensure that the hop puzzle exists
        """
        from puzzles.hop import print_hop, resolve_digits
        pass

    def print_hop(self, digits):
        from puzzles.hop import print_hop
        return print_hop(digits)

    def test_resolve_digits(self):
        """
        Test case with whitespace characters
        """
        from puzzles.hop import resolve_digits

        result = resolve_digits('   \n    15      \n\n\n')
        assert that(result).equals(15), 'Resolve digits should handle whitespace characters'

    def test_hop_divisible_three(self):
        """
        Test case for integers divisible by three
        """
        result = self.print_hop(12)
        assert that(result).equals('Hoppity\n'), 'For integers divisible by 3, print Hoppity\n'

    def test_hop_divisible_five(self):
        """
        Test case for integers divisible by five
        """
        result = self.print_hop(10)
        assert that(result).equals('Hophop\n'), 'For integers divisible by 5, print Hophop\n'

    def test_hop_divisible_three_five(self):
        """
        Test case for integers divisible by both three and five
        """
        result = self.print_hop(15)
        assert that(result).equals('Hop\n'), 'For integers divisible by both 3 & 5, print Hop\n'
