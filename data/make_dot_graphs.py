# Yuritzy Ramos, Samantha Lin, Ruilin Chen, Matthew Joesoep 
# Note: Multi-digraph with output file travel_graph_DupEdges.dot and digraph will output file travel_graph_noDupEdges.dot
import pandas as pd
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("Graph")
    args = parser.parse_args()
    graph_type = args.Graph
    #Create a digraph .dot file (no duplicate edges)
    if graph_type == "digraph":
        # Read data
        data = pd.read_csv("citibike-trips.csv")
        #Create set to avoid duplicate edges 
        edge_pairs = set()
        f = open("travel_graph_noDupEdges.dot","w")
        f.write("digraph {\n")
        for i in range(len(data)):
            #Get start ID
            start = data.loc[i, "start_station_id"]
            #Get end ID 
            end = data.loc[i, "end_station_id"]
            #Create tuple with edge between nodes
            edge = (start,end)
            #If edge already exists then continue to the next edge 
            if edge in edge_pairs:
                continue
            else:
                #Otherwise add it to the set of edges 
                edge_pairs.add(edge)
                #Write edge into the file 
                f.write(str(start) + " -> " + str(end) + "\n")
        f.write("}")
    #Create a multidigraph .dot file (duplicate edges) 
    elif graph_type == "multidigraph":
        data = pd.read_csv("citibike-trips.csv")
        #Write a file 
        f = open("travel_graph_DupEdges.dot","w")
        f.write("digraph {\n")
        for i in range(len(data)):
            #Get start ID
            start = data.loc[i, "start_station_id"]
            #Get end ID
            end = data.loc[i, "end_station_id"]
            #Write edge to file 
            f.write(str(start) + " -> " + str(end) + "\n")
        f.write("}")

if __name__ == '__main__':
    main()
