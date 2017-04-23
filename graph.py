import networkx as nx
import matplotlib.pyplot as plt
import commonVar as common
import numpy as np

def createGraph():
    global colors, pos

    common.G=nx.Graph() # graph undirected to set weight specify them as a parameter creating the edges
    colors={}
    pos={}
    common.G_labels={}
    common.G_edge_labels={}  #copy the address of the labels of the edges

# searching tools

def initializeEdges():
    """for i in range(len(common.G.nodes())):
        #controlla che il nodo i esimo non sia una source
        if common.G.nodes()[i].number < common.N_SOURCES: continue
        for j in range(len(common.G.nodes())): 
            #evita il conteggio doppio
            if j < i: continue
            if common.G.nodes()[j].number < common.N_SOURCES: 
                if random.random() < common.P_s:
                    common.G.add_edge(common.G.nodes()[i], common.G.nodes()[j])
    """
    for i in range(len(common.G.nodes())):
        for j in range(len(common.G.nodes())): 
            if j > i: 
                if common.G.nodes()[i].number < common.N_SOURCES and common.G.nodes()[j].number < common.N_SOURCES:
                    pass
                elif common.G.nodes()[i].number >= common.N_SOURCES and common.G.nodes()[j].number >= common.N_SOURCES:
                    if np.random.random_sample() < common.P_a:
                        common.G.add_edge(common.G.nodes()[i], common.G.nodes()[j])
                else: 
                    if np.random.random_sample() < common.P_s:
                        common.G.add_edge(common.G.nodes()[i], common.G.nodes()[j])


# using networkX and matplotlib case
def closeNetworkXdisplay():
    plt.close()

def openClearNetworkXdisplay():
    if common.graphicStatus == "PythonViaTerminal": plt.ion()
    #plt.clf()

def clearNetworkXdisplay():
    plt.clf()

def getGraph():
    try:
        return common.G
    except:
        return 0


def drawGraph():


    #directed, due to the use of DiGraph

    # draw_netwokx is well documented at
    # https://networkx.github.io/documentation/latest/reference/
    # generated/networkx.drawing.nx_pylab.draw_networkx.html
    #nx.draw_networkx(agentGraph,    font_size=10,node_size=500, \
    pos = nx.spring_layout(common.G)
    clearNetworkXdisplay()
    c = []
    for i in range(len(common.G.nodes())):
        if common.G.nodes()[i].number < common.N_SOURCES:
            c.append('red')
        else:
            c.append('blue')
    nx.draw(common.G, pos, node_size=25, node_color = c, edge_color='black')
    plt.show() # used by %Matplotlib inline [without ion()]; not conflicting
               # with ion()

    if common.graphicStatus == "PythonViaTerminal": plt.pause(0.1)
    # to show the sequence of the shown images in absence of pauses