from unittest import TestCase
from sure import that

class BreathalyzerTestCase(TestCase):

    def setUp(self):
        from puzzles.breathalyzer import Puzzle
        self.runner = Puzzle()

        # initialize the sample with a small dictionary
        processed_words = {'D235': ['dictionary'], 
                           'S514': ['sample'], 
                           'I200': ['is'], 
                           'T200': ['this'], 
                           'A000': ['a'], 
                           'T230': ['test']}
        self.runner.WORDS = processed_words

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

    def test_search(self):
        """
        Tests to ensure that a given search query against 
        a soundex dictionary will return the appropriate result
        relative to the input's resolving soundex.
        """
        # Ensure that we use a soundex from the given dictionary
        assert that(self.runner.soundex('tist')).equals('T230')

        results = self.runner.search('tist')
        assert 'test' in results, 'Given a soundex dictionary, tist search should result in test'

    def test_find_distance(self):
        """
        Test case for finding the edit distance from the given input.
        """
        # single word test case
        result = self.runner.find_distance('tist')
        assert that(result).equals(1), 'Single word test case for a single substitution edit'

        # multi-word test case with insertion
        result = self.runner.find_distance('tist dctinr')
        assert that(result).equals(5), 'Multi-word test case for insertion and substitutions'

        # multi-word test case with deletions
        result = self.runner.find_distance('iis thisa')
        assert that(result).equals(2), 'Multi-word test case for deletions'
