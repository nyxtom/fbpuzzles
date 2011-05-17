from unittest import TestCase
from sure import that

class LiarTestCase(TestCase):
    def test_puzzle_runs(self):
        """
        Test case to ensure that the liar puzzle exists and runs.
        """
        from puzzles.liar import Puzzle
        self.runner = Puzzle()
        pass
