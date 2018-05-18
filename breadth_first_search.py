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


# BREADTH FIRST SEARCH ------------------------------------------------------------------------------------------

# Explaination
# for breadth first, we try to go through all the elements that are "values" of that particular key
# then we move onto the next key in the dictionary

# we cannot use reccursive function for breadth first search

def breadth_first_search(element, first, graph):
    visit = set()
    stack = [first]

    while stack:
        vertex = stack.pop(0)
        if vertex not in visit:
            visit.add(vertex)
            if vertex == element:
                print('element found')
                return visit

            stack.extend(graph[vertex] - visit)  # taking elements within the same key till all have been visited
    return visit

# copy and paste the following code in shell to test:

# visited = breadth_first_search(s,V[1],Graph(E))
##to see all visited elements
# print(visited)

# ---------------------------------------------------------------------------------------------------------------
