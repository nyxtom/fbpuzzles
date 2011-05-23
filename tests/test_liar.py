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
        assert that(result).equals([{'count': '1', 'name': 'Jeff'}, 
                                    {'count': '0', 'name': 'Joe'},
                                    {'count': '1', 'name': 'Tom'},
                                    {'count': '0', 'name': 'Joe'}])

    def test_build_graph(self):
        """
        Tests that the result of matches from the input 
        is successfully built into a undirected connected graph.
        """
        lines = ['2', 'Jeff 1', 'Joe', 'Tom 1', 'Joe']
        success, result = self.runner.is_valid(lines)
        graph, start = self.runner.build_graph(result)
        assert graph == {
                'Jeff': {'Joe': True},
                'Joe': {
                    'Tom': True,
                    'Jeff': True
                },
                'Tom': {'Joe': True}
            }
        assert that(start).equals('Tom')

    def test_bfs(self):
        """
        Tests that the given breadth-first search algorithm appropriately separates the groups.
        """
        lines = ['2', 'Jeff 1', 'Joe', 'Tom 1', 'Joe']
        success, result = self.runner.is_valid(lines)
        graph, start = self.runner.build_graph(result)
        g1, g2 = self.runner.bfs(graph, start)
        assert g1 == {'Jeff': True, 'Tom': True}, 'Jeff and Tom, having a connection through Joe, are in group 1'
        assert g2 == {'Joe': True}, 'Joe, having no connections out, is in group 2'
        assert that(len(g1)).equals(2) and that(len(g2)).equals(1), 'BFS should determine a group of 2 and a group of 1'
