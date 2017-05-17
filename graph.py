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


def initializeEdges():
    for i in range(len(common.G.nodes())):
        for j in range(len(common.G.nodes())): 
            if j > i: 
                if common.G.nodes()[i] < common.N_SOURCES and common.G.nodes()[j] < common.N_SOURCES:
                    pass
                elif common.G.nodes()[i] >= common.N_SOURCES and common.G.nodes()[j] >= common.N_SOURCES:
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

    pos = nx.spring_layout(common.G)
    clearNetworkXdisplay()
    c = []
    for i in range(len(common.G.nodes())):
        if common.G.nodes()[i] < common.N_SOURCES:
            c.append('red')
        else:
            if common.G.nodes(data=True)[i][1]['agent'].active == True:
                c.append('blue')
            else:
                c.append('grey')

    nx.draw(common.G, pos, node_size=25, node_color = c, edge_color='black')

    #to draw labels
    labels = {}
    for i in range(len(common.G.nodes())):
        labels[i] = common.G.nodes()[i]
    nx.draw_networkx_labels(common.G,pos,labels,font_size=12)

    # show plot
    plt.show() 

    if common.graphicStatus == "PythonViaTerminal": plt.pause(0.1)
    # to show the sequence of the shown images in absence of pauses