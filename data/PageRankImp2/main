# THIS CODE IS MY OWN WORK, IT IS INSPIRED BY THE IMPLEMENTATION LOCATED AT https://towardsdatascience.com/pagerank-3c568a7d2332

from src.PageRank import init_graph
from src.PageRank import PageRank
import numpy as np
import pandas as pd
import os

# function to call Pagerank and return a list with all nodes and corresponding pageranks, creates txt file as output
def output_PageRank(iteration, graph, damping_factor, result_dir, fname):

    PageRank(graph, damping_factor, iteration)
    pagerank_list = graph.get_pagerank_list()
    node_list = graph.get_node_list()
    full_list = list(zip(node_list, pagerank_list))
    print('PageRank:')
    # print(full_list)
    print()
    path = os.path.join(result_dir, fname)
    os.makedirs(path, exist_ok=True)
    np.savetxt(os.path.join(path, fname), full_list, header="vertex,pagerank", fmt='%s', delimiter=',', newline="\n")
    return full_list

# testing class for initialization of input and output file names
class PageRankTester:
    def __init__(self):
        input_name = 'travel_graph_no_duplicates.dot'
        output_name = 'travelprnodupes.csv'

        PageRankTester.test(input_name, output_name)

        input_name = 'travel_graph.dot'
        output_name = 'travelpr.csv'
        PageRankTester.test(input_name, output_name)
    
    def test(input_name, output_name):
        iteration = 1000
        damping_factor = 0.15
        initialize = './dataset/'
        result_dir = 'result'
        graph = init_graph(initialize + input_name)

        output = output_PageRank(iteration, graph, damping_factor, result_dir, output_name)
        print(output)

        return output_name

# Creates a PageRankTester() so that user is called for their input
if __name__ == '__main__':
    obj = PageRankTester()

