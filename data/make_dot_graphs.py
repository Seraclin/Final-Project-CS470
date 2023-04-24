import pandas as pd
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("Graph")
    args = parser.parse_args()
    graph_type = args.Graph
    #Create a digraph .dot file (no duplicate edges)
    if graph_type == "digraph":
        data = pd.read_csv("citibike-trips.csv")
        edge_pairs = set()
        f = open("travel_graph_noDupEdges.dot","w")
        f.write("digraph {\n")
        for i in range(len(data)):
            start = data.loc[i, "start_station_id"]
            end = data.loc[i, "end_station_id"]
            edge = (start,end)
            if edge in edge_pairs:
                continue
            else:
                edge_pairs.add(edge)
                f.write(str(start) + " -> " + str(end) + "\n")
        f.write("}")
    #Create a multidigraph .dot file (duplicate edges) 
    elif graph_type == "multidigraph":
        data = pd.read_csv("citibike-trips.csv")
        f = open("travel_graph_DupEdges.dot","w")
        f.write("digraph {\n")
        for i in range(len(data)):
            start = data.loc[i, "start_station_id"]
            end = data.loc[i, "end_station_id"]
            f.write(str(start) + " -> " + str(end) + "\n")
        f.write("}")

if __name__ == '__main__':
    main()
