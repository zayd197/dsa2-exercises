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
        weight=edge[0] #each tuple is split into three named variables edge[0],edge[1] and edge[2]
        node1=edge[1]
        node2=edge[2]

        if nx.has_path(mst,node1,node2): #this says in hte mst built so far, can i get from node1 to node2?  (Kruskal's rule)
           print("We will skip",node1,"-",node2,"with weight",weight, "as it would make a loop") #yes, so adding this will create a loop. we will skip it.
        else:
           mst.add_edge(node1,node2,weight=weight)#they are not connected to this edge will be added to MST with its weight.
           print("We will add",node1,"-",node2,"with weight", weight)
    
    return mst

def draw_graph(Graph, positions, title):
    nx.draw(Graph, positions,with_labels=True, node_color="lightblue",node_size=800) #draws the functions and edges, with_labels=true writes the letters on the nodes
    nx.draw_networkx_edge_labels(Graph, positions, edge_labels=nx.get_edge_attributes(Graph, "weight"))#writes each edge weights on its line
    plt.title(title)#adds a heading
    plt.show()#opens it in a window

#drawing graph1 with 6 nodes and 11 edges
    
graph1=nx.Graph()
graph1.add_edge("A", "B", weight=4)
graph1.add_edge("A", "C", weight=2)
graph1.add_edge("A", "D", weight=7)
graph1.add_edge("B", "C", weight=5)
graph1.add_edge("B", "E", weight=10)
graph1.add_edge("C", "D", weight=3)
graph1.add_edge("C", "E", weight=8)
graph1.add_edge("C", "F", weight=6)
graph1.add_edge("D", "F", weight=1)
graph1.add_edge("E", "F", weight=9)
graph1.add_edge("B", "F", weight=11)

print("Graph 1")
positions1=nx.spring_layout(graph1, seed=1)
draw_graph(graph1, positions1, "Graph 1")
mst1=MyMinimumSpanningTree(graph1)
draw_graph(mst1, positions1, "Graph 1 MST")

#drawing graph2 with 5 nodes and 8 edges

graph2=nx.Graph()
graph2.add_edge("A", "B", weight=3)
graph2.add_edge("A", "C", weight=8)
graph2.add_edge("A", "D", weight=1)
graph2.add_edge("B", "C", weight=2)
graph2.add_edge("B", "E", weight=7)
graph2.add_edge("C", "D", weight=6)
graph2.add_edge("C", "E", weight=4)
graph2.add_edge("D", "E", weight=5)

print("Graph 2")
positions2=nx.spring_layout(graph2, seed=2)
draw_graph(graph2, positions2, "Graph 2")
mst2=MyMinimumSpanningTree(graph2)
draw_graph(mst2, positions2, "Graph 2 MST")

print("Graph 2")
positions2=nx.spring_layout(graph2, seed=2)
draw_graph(graph2, positions2, "Graph 2")
mst2=MyMinimumSpanningTree(graph2)
draw_graph(mst2, positions2, "Graph 2 MST")


#drawing graph3 with 7 nodes and 10 edges

graph3=nx.Graph()
graph3.add_edge("A", "B", weight=12)
graph3.add_edge("A", "C", weight=5)
graph3.add_edge("B", "C", weight=9)
graph3.add_edge("B", "D", weight=3)
graph3.add_edge("C", "E", weight=14)
graph3.add_edge("D", "E", weight=7)
graph3.add_edge("D", "F", weight=6)
graph3.add_edge("E", "G", weight=2)
graph3.add_edge("F", "G", weight=8)
graph3.add_edge("C", "D", weight=10)

print("Graph 3")
positions3=nx.spring_layout(graph3, seed=3)
draw_graph(graph3, positions3, "Graph 3")
mst3=MyMinimumSpanningTree(graph3)
draw_graph(mst3, positions3, "Graph 3 MST")
