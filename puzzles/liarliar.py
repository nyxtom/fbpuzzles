#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
colors = dict(red="\033[1;31m", nc="\033[0m")

def print_error(message):
    """
    Prints the appropriate error message to the user
    in full red color as it should be.
    """
    print '%s%s%s' % (colors['red'], message, colors['nc'])


class Puzzle(object):
    """
    Defines the liar liar puzzle implementation.
    """
    def run(self, lines):
        """
        Runs through the given input to create 
        an aggregate result of liars/non-liars.
        """
        success, result = self.is_valid(lines)
        if not success:
            print_error(result)
            return

        graph, start = self.build_graph(result)
        groups = [len(g) for g in self.bfs(graph, start)]
        groups.reverse()
        print '%s %s' % (groups[0], groups[1])

    def is_valid(self, lines):
        """
        Ensures that the given input is validated and 
        if not, then the appropriate error message 
        result will be displayed to the user.
        """
        if not lines:
            return False, 'You must provide a valid input file'

        if not lines[0].strip().isdigit():
            return False, 'The first line in the input should be the count'

        lines = [line.strip() for line in lines]

        matches = []
        for line in lines[1:]:
            m = re.match(r'(?P<name>[A-Za-z]+)(\s+(?P<count>\d+))?', line)
            if not m:
                return False, 'All lines must contain a valid name and/or count match'
            else:
                matches.append(m.groupdict('0'))

        return True, matches

    def build_graph(self, matches):
        """
        Builds an undirected connected graph using the matching input.
        """
        names = set([m['name'] for m in matches])
        graph = {}
        for n in names:
            graph[n] = {}

        i = 0
        while i < len(matches):
            count, n = matches[i].values()
            start = n
            for l in xrange(int(count)):
                ln = matches[i + 1]['name']
                graph[n][ln] = graph[ln][n] = True
                i = i + 1
            i = i + 1

        return graph, start

    def bfs(self, graph, start):
        """
        Groups vertices into two groups using a FIFO queue for traversal.

        http://en.wikipedia.org/wiki/Adjacency_matrix
        http://en.wikipedia.org/wiki/Breadth-first_search
        """
        visited = {start: True}
        group1 = {start: True}
        group2 = {}

        import Queue
        queue = Queue.Queue()
        queue.put(start)
        while not queue.empty():
            n = queue.get()
            for k in graph[n].keys():
                if k in visited:
                    continue

                visited[k] = True

                if group2.get(n):
                    group1[k] = True
                if group1.get(n):
                    group2[k] = True

                queue.put(k)

        return [group1, group2]

# Puzzle runner boilerplate
if __name__ == "__main__":
    if not len(sys.argv) > 1:
        print_error('You must provide an input filename')
    else:
        try:
            with open(sys.argv[1]) as input_file:
                input = input_file.readlines()
                runner = Puzzle()
                runner.run(input)
        except IOError as e:
            print_error(e)
