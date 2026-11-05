import networkx as nx

import matplotlib.pyplot as plt

#Kruskal's algorithm

def MyMinimumSpanningTree(Graph) -> nx.Graph:
    print("We will be using Kruskal's algorithm")


#making a list of all the edges as weight, node1 and node2
    edges=[]
    for node1,node2,data in Graph.edges(data=True):
        edges.append((data["weight"],node1,node2))

    edges.sort() #this sorts the edges from in terms of weight, smallest to biggest

    mst=nx.Graph()     #starting the MST with all the nodes but no edges
    mst.add_nodes_from(Graph.nodes())

    for edge in edges: #looking at all the edges starting with the smallest one
        weight=edge[0]
        node1=edge[1]
        node2=edge[2]

        if nx.has_path(mst,node1,node2):
           print("We will skip",node1,"-",node2,"with weight",weight, "as it would make a cycle")
        else:
           mst.add_edge(node1,node2,weight=weight)
           print("We will add",node1,"-",node2,"with weight", weight)
    
    return mst
