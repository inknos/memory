# Agent.py
from Tools import *
from agTools import *
import graph as graph
import commonVar as common
import numpy as np

#Agent must be the partent class of every object. Must inherit from SuperAgent
class Agent(SuperAgent):
    """
    Create the parent agent

    Def. constructor:
    class Agent(SuperAgent):
        def __init__(self, number,myWorldState, xPos, yPos, lX =-20,rX=19, bY=-20,tY=19, agType="")
    """
    def __init__(self, number, myWorldState, agType=""):
        # the environment
        self.agOperatingSets = []
        self.number = number

        if myWorldState != 0:
            self.myWorldState = myWorldState
        self.agType = agType

        if graph.getGraph() == 0: graph.createGraph() # if first agent create the graph
        common.G.add_node(self.number, agent = self)  # adds himself
        if len(common.G.nodes()) == common.N_AGENTS: graph.initializeEdges() # if last creates edges

        self.state = np.array([np.random.random_sample() for i in range(common.dim) ])
        self.state = self.state / self.state.sum()

        print "agent", self.agType, "#", self.number, "has been created"

    def getGraph(self):
        return common.G

    # return neighbour list. call with no arguments
    def listNeighbours(self):
        return common.G.neighbors(self.number)

    # create link with a node with id a
    def createEdge(self, a):
        pass

    # removes link with a node with id a
    def removeEdge(self, a):
        pass



