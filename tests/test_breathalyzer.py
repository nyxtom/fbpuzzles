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

    def test_levenshtein(self):
        """
        Test case to ensure that the distance formular for 
        inserts, substitutions and deletions is working 
        as intended and returns the appropriate count.
        """
        # Test deletion
        result = self.runner.levenshtein('asdf', 'asd')
        assert that(result).equals(1)

        # Testing substitution
        result = self.runner.levenshtein('kat', 'cat')
        assert that(result).equals(1)

        # Testing insertion
        result = self.runner.levenshtein('wondr', 'wonderflow')
        assert that(result).equals(5)
