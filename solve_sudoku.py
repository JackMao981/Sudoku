import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import copy

def create_sudoku(a):
    #creates graph
    G = nx.Graph()

    #creates all the nodes
    for row in range(int(a*a)):
        for column in range(int(a*a)):
            G.add_node((row+1,column+1))

    #creates edges b/w nodes in same row and same column
    for node in G.nodes():
        for node1 in G.nodes():
            if node[0] == node1[0] and node != node1:
                G.add_edge(node,node1)
            if node[1] == node1[1] and node != node1:
                G.add_edge(node,node1)
            #creates edges b/w nodes in same box
            nodex = np.ceil(node[0]/a)
            nodey = np.ceil(node[1]/a)
            node1x = np.ceil(node1[0]/a)
            node1y = np.ceil(node1[1]/a)
            if nodex == node1x and nodey == node1y and node != node1:
                G.add_edge(node,node1)

    return G

# fills is a list of values for each of the nodes places
def fill_presets(fills):
    given = [] #indices of existing colors on the sudoku board
    nc = {}
    for i, pre in enumerate(fills):
        if pre != 0:
            given.append(i+1)
            nc[i+1] = pre
    return nc, given

def solve_sudoku(G,a,fills):
    nc, given = fill_presets(fills)
    preset = copy.deepcopy(nc)
    H = nx.convert_node_labels_to_integers(G, first_label=1)
    not_presets = list(set(H.nodes()) - set(preset.keys()))
    index = 0
    total_vertices = int(a**4)
    return sud_helper(H,not_presets,index,total_vertices,nc)


def sud_helper(H,not_presets,index,total_vertices,nc):
    if 0 not in nc.values() and len(nc.values())==81:
        return True, nc

    node = not_presets[index]
    #else iterate through each color per node and see what works
    for color in range(1,10):

        #if a safe configuration, set the color and call sud_helper on next node
        if check_safe(H,node,nc,color):
            nc[node] = color
            #if it returns true, then return true and break the loop
            if sud_helper(H,not_presets,index+1,total_vertices,nc)[0]:
                return True, nc
            #otherwise reset the color and try the next color
            nc[node] = 0

    return False, nc


def check_safe(H,node,nc,color):
    #checks neighbors
    for neigh in H.neighbors(node):
        if neigh in nc.keys():
            if nc[neigh] == color:
                return False
    return True

def check_sudoku(solved):
    rows = {}
    columns = {}
    quadrants = {}
    for k in solved.keys():
        row = np.ceil(k/9.0)
        column = (k%9)
        if column == 0:
            column = 9
        if row not in rows.keys():
            rows[row] = set()
        rows[row].add(solved[k])
        if column not in columns.keys():
            columns[column] = set()
        columns[column].add(solved[k])

        quadx = np.ceil(row/3.0)
        quady = np.ceil(column/3.0)

        if (quadx,quady) not in quadrants.keys():
            quadrants[(quadx,quady)] = set()
        quadrants[(quadx,quady)].add(solved[k])

    result = True
    for r in rows.keys():
        if len(rows[r]) != 9:
            # print(rows[r], r, 'rows')
            result = False
    for c in columns.keys():
        if len(columns[c]) != 9:
            # print(columns[c], c,'c')
            result = False
    for q in quadrants.keys():
        if len(quadrants[q]) != 9:
            # print(quadrants[q], q, 'quad')
            result = False
    return result
