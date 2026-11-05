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
