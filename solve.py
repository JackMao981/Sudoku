import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from sudoku import create_sudoku
from sudoku import fill_presets


def solver(G):
# select colored vertex
    for n in G.nodes():
        if G.nodes[n]["numbers"] != 0:
            # color edges with color of the selected vertex
            # neighbors now know what the color of this node is
            G = color_neighbor(G, G.nodes[n]["numbers"], G.neighbors(n))
# neighbors cannot be the same color as the selected vertex
# find vertex with max colored edges
    n = max_vertex(G)
# if only 1 option for color, color it
# select any vertex that has largest number of uncolored neighbors
# color the selected vertex as lowest value available
# go back to top
    return G

def color_neighbor(G, num, nodes):
    for n in nodes:
        lst = G.nodes[n]["numbers"]
        lst.append(num) if num not in lst else lst
    return G

def max_vertex(G):
    m = (0,(0,0))
    for n in G.nodes():
        if m[0] < len(G.nodes[n]["numbers"]):
            m = len(G.nodes[n]["numbers"]), n
            print(m[0])
    return m[1]



if __name__ == "__main__":
    G = create_sudoku(3.0)
    G = fill_presets(G, [(1,1,1)])
    G.nodes[(5,5)]["numbers"].append(5)
    print(max_vertex(G))
    for n in G.nodes():
        print(G.nodes[n]["numbers"])
