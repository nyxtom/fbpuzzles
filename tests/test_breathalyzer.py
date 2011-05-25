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

        # Test multiple combinations
        result = self.runner.levenshtein('alright', 'all right')
        assert that(result).equals(2)

        result = self.runner.levenshtein('accosinly', 'occasionally')
        assert that(result).equals(5)

    def test_boundary_levenshtein(self):
        """
        Test case to ensure that the boundaries for levenshtein are hit
        and work as expected for empty, * and...etc.
        """
        empty = ''
        assert that(self.runner.levenshtein(empty, empty)).equals(0)

        text = ''
        for i in range(1, 10):
            text += '*'
            result = self.runner.levenshtein(empty, text)
            assert that(result).equals(i)
            result = self.runner.levenshtein(text, empty)
            assert that(result).equals(i)

    def test_soundex(self):
        """
        Test case to ensure soundex is appropriately resolving.
        """
        variations = ['london', 'lONDoN', '.,lon123don', 'l on do n', 'londn', 
                      'londdn', 'londan', 'lnodno']
        for v in variations:
            assert that(self.runner.soundex(v)).equals('L535')

    def test_soundex_boundary(self):
        """
        Test case to ensure that the boundary cases of the soundex algorithm are handled appropriately.
        """
        assert that(self.runner.soundex('')).equals('0000')
        assert that(self.runner.soundex('   \r\n')).equals('0000')
        assert that(self.runner.soundex('3940')).equals('0000')
