from unittest import TestCase
from sure import that

class BreathalyzerTestCase(TestCase):

    def setUp(self):
        from puzzles.breathalyzer import Puzzle
        self.runner = Puzzle()

    def test_puzzle_runs(self):
        """
        Test case to ensure that the puzzle exists and runs.
        """
        self.runner.run("")
        pass
