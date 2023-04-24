import numpy as np
fname = './dataset/travel_graph_no_duplicates.dot'


class Graph:
    def __init__(self):
        self.nodes = []

    # Searches if graph already has a node of a name in nodes[]
    def contains(self, name):
        for node in self.nodes:
            if(node.name == name):
                return True
        return False

    # Return the node with the name, create and return new node if not found
    def find(self, name):
        if(not self.contains(name)):
            new_node = Node(name)
            self.nodes.append(new_node)
            return new_node
        else:
            return next(node for node in self.nodes if node.name == name)

    # Adds new connections from a node to its parent and to its children
    def add_edge(self, parent, child):
        parent_node = self.find(parent)
        child_node = self.find(child)

        parent_node.link_child(child_node)
        child_node.link_parent(parent_node)

    # Prints all children of a node
    def display(self):
        for node in self.nodes:
            print(f'{node.name} links to {[child.name for child in node.children]}')

    # Sorts nodes in the graph according to a key
    def sort_nodes(self):
        self.nodes.sort(key=lambda node: node.name)

    # Updates the sum of all pageranks of the nodes and updates pageranks of each node to reflect relation to new sum
    def normalize_pagerank(self):
        pagerank_sum = sum(node.pagerank for node in self.nodes)

        for node in self.nodes:
            node.pagerank /= pagerank_sum

    # Gives list of pageranks of all nodes in graph
    def get_pagerank_list(self):
        pagerank_list = np.asarray([node.pagerank for node in self.nodes], dtype='float32')
        return np.round(pagerank_list, 10)
    
    # Gives list of names of all nodes in graph
    def get_node_list(self):
        node_list = np.asarray([node.name for node in self.nodes], dtype='str')
        return node_list


class Node:
    # Initializes node with its name, children list, parents list, and starting pagerank of 1.0
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parents = []
        self.pagerank = 1.0

    # Links node to child node if it is not already linked
    def link_child(self, new_child):
        for child in self.children:
            if(child.name == new_child.name):
                return None
        self.children.append(new_child)

    # Links node to parent node if it is not already linked
    def link_parent(self, new_parent):
        for parent in self.parents:
            if(parent.name == new_parent.name):
                return None
        self.parents.append(new_parent)

    # Updates pagerank of individual node
    def update_pagerank(self, d, n):
        in_neighbors = self.parents
        pagerank_sum = sum((node.pagerank / len(node.children)) for node in in_neighbors)
        random_jumping = d / n
        self.pagerank = random_jumping + (1-d) * pagerank_sum

# line reader
def init_graph(fname):
    with open(fname) as f:
        lines = f.readlines()
    graph = Graph()

    for line in lines:

        if '->' in line:
            [parent, child] = line.strip().split(' -> ')
            graph.add_edge(parent, child)

    graph.sort_nodes()

    return graph

# for one iteration of PageRank
def PageRank_one_iter(graph, d):
    node_list = graph.nodes
    for node in node_list:
        node.update_pagerank(d, len(graph.nodes))
    graph.normalize_pagerank()
    # print(graph.get_pagerank_list())
    # print()

# Repeats PageRank for however many iterations as necessary
def PageRank(graph, d, iteration=100):
    for i in range(int(iteration)):
        PageRank_one_iter(graph, d)

