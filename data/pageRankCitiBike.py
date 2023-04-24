# Yuritzy Ramos, Samantha Lin, Ruilin Chen, Matthew Joesoep
import networkx as nx
import pandas as pd
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("Graph")
    parser.add_argument("Output")
    args = parser.parse_args()
    graph_type = args.Graph
    output_file = args.Output
    data = pd.read_csv("citibike-trips.csv")
    #Create multidigraph and pass to NetworkX PageRank Function
    if graph_type == "multidigraph":
        multidigraph = nx.MultiDiGraph()
        edges = []
        for i in range(len(data)):
            #Get start id 
            start = data.loc[i, "start_station_id"]
            #Get end id 
            end = data.loc[i, "end_station_id"]
            #Add edge to list  
            edges.append((start,end))
        #Add edges to graph 
        multidigraph.add_edges_from(edges)
        #Dampening factor 0.85 and maximum iterations 1000
        pr = nx.pagerank(multidigraph, max_iter = 1000)
        #Create file with page rank scores and station IDs 
        f = open(output_file, "w")
        f.write("Station ID,Page Rank" + '\n')
        for key, value in pr.items():
            f.write(str(key)+ ", " + str(value) + '\n')
        f.close()

        # Sorting page rank score in descending order and station IDs in ascending order
        df = pd.read_csv(output_file)
        df_sort = df.sort_values(["Page Rank","Station ID"], ascending=[False, True])
        df_sort.to_csv(output_file, index = False)
    #Create digraph and pass to NetworkX PageRank Function
    elif graph_type == "digraph":
        digraph = nx.DiGraph()
        #Store edges
        edges = []
        for i in range(len(data)):
            #Get start ID
            start = data.loc[i, "start_station_id"]
            #Get end ID
            end = data.loc[i, "end_station_id"]
            #Append edge to list 
            edges.append((start, end))
        #Add edges to graph 
        digraph.add_edges_from(edges)
        pr = nx.pagerank(digraph, max_iter=1000)
        #Write file with page rank score and station ID
        f = open(output_file, "w")
        f.write("Station ID,Page Rank" + '\n')
        for key, value in pr.items():
            f.write(str(key) + ", " + str(value) + '\n')
        f.close()
        #Sorting page rank score in descending order and station IDs in acending order
        df = pd.read_csv(output_file)
        df_sort = df.sort_values(["Page Rank", "Station ID"], ascending=[False, True])
        df_sort.to_csv(output_file, index=False)

if __name__ == '__main__':
    main()
