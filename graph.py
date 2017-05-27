import networkx as nx
import matplotlib.pyplot as plt
import commonVar as common
import numpy as np
from networkx.drawing.nx_agraph import graphviz_layout
import usefulFunctions as uf


def createGraph():
    global colors, pos

    # graph undirected to set weight specify them as a parameter creating the
    # edges
    common.G = nx.Graph()
    colors = {}
    pos = {}
    common.G_labels = {}
    common.G_edge_labels = {}  # copy the address of the labels of the edges


def initializeEdges():
    """

    random initialization of edges

    """

    for i in range(len(common.G.nodes())):
        for j in range(len(common.G.nodes())):
            if j > i:
                if common.G.nodes()[i] < common.N_SOURCES and common.G.nodes()[j] < common.N_SOURCES:
                    pass
                elif common.G.nodes()[i] >= common.N_SOURCES and common.G.nodes()[j] >= common.N_SOURCES:
                    if np.random.random_sample() < common.P_a:
                        common.G.add_edge(common.G.nodes()[i], common.G.nodes()[
                                          j], weight=0.3 + 0.7 * np.random.random_sample())
                else:
                    if np.random.random_sample() < common.P_s:
                        common.G.add_edge(common.G.nodes()[i], common.G.nodes()[
                                          j], weight=0.3 + 0.7 * np.random.random_sample())


# using networkX and matplotlib case
def closeNetworkXdisplay():
    plt.close()


def openClearNetworkXdisplay():
    if common.graphicStatus == "PythonViaTerminal":
        plt.ion()
    # plt.clf()


def clearNetworkXdisplay():
    plt.clf()


def getGraph():
    """

    returns the graph if exists
    else returns zero

    """

    try:
        return common.G
    except:
        return 0


def drawGraph(n=True, e=True, l=True, clrs='state', static=True):

    clearNetworkXdisplay()
    c = []
    if clrs == 'state':  # draw colors thinking of state
        for i in range(len(common.G.nodes())):
            if common.G.nodes(data=True)[i][1]['agent'].hasNews(id_source=1, date=1) is True:
                c.append('green')
                uf.vprint("green")
            elif common.G.nodes(data=True)[i][1]['agent'].hasNews(id_source=4, date=1) is True:
                c.append('yellow')
                uf.vprint("yellow")
            else:
                if common.G.nodes()[i] < common.N_SOURCES:
                    c.append('red')
                else:
                    if common.G.nodes(data=True)[i][1]['agent'].active is True:
                        c.append('blue')
                    else:
                        c.append('grey')

    if static is True:
        pos = graphviz_layout(common.G)

    if n is True:  # draw nodes
        nx.draw_networkx_nodes(common.G, pos, node_size=60, node_color=c)

    if e is True:  # draw edges
        nx.draw_networkx_edges(common.G, pos, edge_color='black')

    if l is True:  # draw labels
        nx.draw_networkx_labels(common.G, pos, font_size=8)

    plt.show()  # show plot

    if common.graphicStatus == "PythonViaTerminal":
        plt.pause(0.1)
    # to show the sequence of the shown images in absence of pauses
