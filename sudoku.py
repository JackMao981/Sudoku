import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

#creates graph
G = nx.Graph()

#creates all the nodes
for row in range(9):
    for column in range(9):
        G.add_node((row+1,column+1))

# give nodes attributes. 
node_values = 0
nx.set_node_attributes(G, node_values, "numbers")

#creates edges b/w nodes in same row and same column
for node in G.nodes():
    for node1 in G.nodes():
        if node[0] == node1[0] and node != node1:
            G.add_edge(node,node1)
        if node[1] == node1[1] and node != node1:
            G.add_edge(node,node1)
        #creates edges b/w nodes in same box
        nodex = np.ceil(node[0]/3.0)
        nodey = np.ceil(node[1]/3.0)
        node1x = np.ceil(node[0]/3.0)
        node1y = np.ceil(node[1]/3.0)
        if nodex == node1x and nodey == node1y and node != node1:
            G.add_edge(node,node1)

print(G.nodes[(1,1)]["numbers"])
# nx.draw(G, with_labels = True)
# plt.show()

#check columns

#check small boxes
