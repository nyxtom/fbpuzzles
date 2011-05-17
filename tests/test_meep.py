from unittest import TestCase
from sure import that

class MeepTestCase(TestCase):

    def setUp(self):
        from puzzles.meep import Puzzle
        self.runner = Puzzle()

    def test_puzzle_runs(self):
        """
        Test case to ensure that the meep puzzle exists and runs.
        """
        self.runner.run("Just ignore me, I am not important")
        pass

    def test_outputs_meep(self):
        """
        Test case to ensure that print returns the right output.
        """
        result = self.runner.print_meep('Just ignore me, I am not important')
        assert that(result).equals('Meep meep!'), 'The output of the meep puzzle should always be Meep meep!'
