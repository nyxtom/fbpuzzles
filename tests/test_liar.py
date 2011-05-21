from unittest import TestCase
from sure import that

class LiarTestCase(TestCase):
    def setUp(self):
        """
        Sets up the test runner for the puzzle.
        """
        from puzzles.liarliar import Puzzle
        self.runner = Puzzle()

    def test_puzzle_runs(self):
        """
        Test case to ensure that the liar puzzle exists and runs.
        """
        self.runner.run(None)
        pass

    def test_provide_invalid_noinput(self):
        """
        Tests that input should actually be there.
        """
        success, result = self.runner.is_valid(None)
        assert not success, 'The given input is not considered valid if it is None'
        assert that(result).equals('You must provide a valid input file')

    def test_provide_invalid_no_count(self):
        """
        Tests that the first line is always the count.
        """
        success, result = self.runner.is_valid('xx')
        assert not success, 'The given input is not considered valid if there is no count'
        assert that(result).equals('The first line in the input should be the count')

    def test_provide_invalid_no_match(self):
        """
        Tests that an input lines must always be provided.
        """
        lines = ['2', 'Jeff  2', '323&&invalid line here 33 sd']
        success, result = self.runner.is_valid(lines)
        assert not success, 'The given input is not valid with an invalid line match'
        assert that(result).equals('All lines must contain a valid name and/or count match')

    def test_valid_matches(self):
        """
        Tests that a valid match is made and a match set is returned.
        """
        lines = ['2', 'Jeff 1', 'Joe', 'Tom 1', 'Joe']
        success, result = self.runner.is_valid(lines)
        assert success, 'A valid set of lines should be successful in matching'
        assert that(result).equals([{'count': '1',  'name': 'Jeff'}, 
                                    {'count': None, 'name': 'Joe'},
                                    {'count': '1',  'name': 'Tom'},
                                    {'count': None, 'name': 'Joe'}])

    def test_tally(self):
        """
        Tests that the tally of the accused versus the non is accurate.
        """
        lines = ['2', 'Jeff 1', 'Doug', 'Mindy 2', 'Windy', 'Jeff']
        success, matches = self.runner.is_valid(lines)
        assert success, 'A valid set of lines should be successful in matching'

        accused, rest = self.runner.tally(matches)
        assert that(accused).equals(3) and that(rest).equals(1), 'There were 2 people accusing 3 people, and only one person was never accused.'
