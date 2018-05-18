# Use Create Graphs and use DEPTH FIRST SEARCH AND BREADTH FIRST SEARCH ALGORITHMS TO FIND AN ELEMENT -----

# in this problem, we are accepting the nodes and vertices and creating
# a dictionary of the connections of each node
# this dictionary is then used to traverse across the graph to implement different
# functions such as depth_first_search, breadth_first_search and shortest_path

# GENERATE THE GRAPH --------------------------------------------------------------------------------------
from collections import defaultdict


class Graph(object):

    def __init__(self, connections):
        self.graph = defaultdict(set)
        self.add_connections(connections)

    def add_connections(self, connections):
        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        self.graph[node1].add(node2)
        self.graph[node2].add(node1)


connections = [['A', 'B'], ['B', 'C'], ['B', 'D'], ['E', 'F'], ['F', 'C']]
graph1 = Graph(connections)


# DEPTH FIRST SEARCH ---------------------------------------------------------------------------------------

# Explaination
# for a search algorithm in graphs, we need to keep track
# of each node that has already been visited and then move onto
# those nodes which have not been visited

# in depth first search, we traverse our aim is to look through all the keys firsts
# then we look at elements within the keys by BACKTRACKING

def depth_first_search(element, first, graph, visit=None):
    if visit is None:
        visit = set()  # maintain a set of visited nodes
        # visited nodes can be excluded from next search
    visit.add(first)

    if first == element:
        print('element was found')
        return visit

    else:
        for next in graph[first] - visit:
            # recursive function that keeps going into depth till all elements visited
            depth_first_search(element, next, graph, visit)
            # once all the elements are visited, the set of visited elements is return

    return visit