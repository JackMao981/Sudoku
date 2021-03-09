import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def create_sudoku(a):
    #creates graph
    G = nx.Graph()

    #creates all the nodes
    for row in range(int(a*a)):
        for column in range(int(a*a)):
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
            nodex = np.ceil(node[0]/a)
            nodey = np.ceil(node[1]/a)
            node1x = np.ceil(node1[0]/a)
            node1y = np.ceil(node1[1]/a)
            if nodex == node1x and nodey == node1y and node != node1:
                G.add_edge(node,node1)

    return G

# numbers is a list of tuples (x, y, number)
def fill_presets(G, numbers):
#first we need to fill out pre-set colors
    for (x,y,n) in numbers:
        G.nodes[(x,y)]["numbers"] = n
    return G

def solve_sudoku(G):
    result = True
    count = 1
    # colors.values()
    # print(colors)
    # {(x,y):color; (x,y):color}
    colors = nx.get_node_attributes(G,"numbers")
    while any(map(lambda x: x == 0, colors.values())): #there exists a node whose attribute "numbers" == 0: #while something uncolored
        if count > 9:
            # print("The count is ", count)
            result = False
        # node that is empty
        for (x,y) in colors:
            if colors[(x,y)] == 0:
                start = (x,y)
        G = sud_helper(G, start, count)
        count += 1
        colors = nx.get_node_attributes(G,"numbers")
        # print(colors.values())
    return G, result

# node, color
def sud_helper(G):
    for node in G.nodes():
        if G.nodes[node]["numbers"] == 0:
            # print("here")
            G.nodes[node]["numbers"] = check_neighbors(G,node) + 1
    #print(nx.non_neighbors(G,list(G.nodes[node])))
    return G


# return list of not neighbors
def not_neighbor(G, node):
    s = list(set(G.nodes()) - set(G.neighbors(node)))
    s.remove(node)
    return s

# check if the neighbors are colored. return highest color
def check_neighbors(G,node):
    # print(list(G.neighbors(node)))
    # print(list(map(lambda x: G.nodes[x]["numbers"],list(G.neighbors(node)))))
    return max(list(map(lambda x: G.nodes[x]["numbers"],list(G.neighbors(node)))))

def check_sudoku(G):
    pass

# def print_sudoku(G):
#     for n in G.nodes()
#         return
if __name__ == "__main__":
    G = create_sudoku(3.0)

    G = sud_helper(G)
    print(nx.get_node_attributes(G, "numbers"))
    # print(list(G.nodes()))
    # G, r = solve_sudoku(G)
    # nx.draw(G, with_labels = True)
    # plt.show()
