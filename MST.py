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

def draw_graph(Graph, positions, title):
    nx.draw(Graph, positions,with_labels=True, node_color="lightblue",node_size=800)
    nx.draw_networkx_edge_labels(Graph, positions, edge_labels=nx.get_edge_attributes(Graph, "weight"))
    plt.title(title)
    plt.show()

#drawing graph1
    
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
