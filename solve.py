import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from sudoku import create_sudoku
from sudoku import fill_presets


def solver(G,a):
    """
    1. select colored vertex and check if an edge is uncolored
    2. color the uncolored edges of this vertex
    3. find vertex with max colored in_degree
    4. color it the lowest option possible
    5. repeat steps 1-4
    """
    ec = {}
    nc = {}
    chosen = set()
    while not_complete(nc,a):
    #step 1
        for n in G.nodes():
            if n not in chosen and n in nc.keys():
                #step 2
                for edge in G.edges(n):
                    if edge not in ec.keys():
                        ec[edge] = nc[n]
            chosen.add(n)
            break;

    #step 3
        max_n = max_colored_degree(ec,nc)
        color = min_color_available(ec,max_n,a)
        #step 4
        if color == -1:
            exit(-1)
        nc[max_n] = color
    return nc

def not_complete(nc,a):
    return len(nc.keys()) != a**4

def max_colored_degree(ec,nc):

#goal: find the vertex with the most colored edges
#ec - has a list of edges, let's find the node that shows up the most in ec that isn't colored
#if there is a tie, then we just pick one
    how_many = {}
    if ec == {}:
        return (1,1)
    for (n1,n2) in ec.keys():
        if n1 not in nc.keys():
            if n1 not in how_many:
                how_many[n1] = 0
            how_many[n1] = how_many[n1] + 1
        if n2 not in nc.keys():
            if n2 not in how_many:
                how_many[n2] = 0
            how_many[n2] = how_many[n2] + 1
    #find maximum value in how_many and return its key, if tie just pick one
    max_value = max(how_many.values())  # maximum value
    max_keys = [k for k, v in how_many.items() if v == max_value] # getting all keys containing the `maximum`
    return max_keys[0]

def min_color_available(ec,max_n,a):
    bad_color = set()
    colors = set([i+1 for i in range(int(a*a))])

    for k in ec.keys():
        if max_n in k:
            bad_color.add(ec[k])
    colors = colors - bad_color
    for color in colors:
        if color > 9:
            print("we're f*****ed")
            return -1
    return min(colors)

# def check_sudoku(nc):
#     pass

if __name__ == "__main__":
    a = 3.0
    G = create_sudoku(a)
    # G = fill_presets(G, [(1,1,1)])
    nc = solver(G,a)
    print(nc)

    # ec = {(1,2):1,(1,3):1,(1,4):1,(3,2):2, (4,2):3}
    # nc = {1:1,3:5}
    # max_n = max_colored_degree(ec, nc)
    # print(min_color_available(ec, max_n, a))
