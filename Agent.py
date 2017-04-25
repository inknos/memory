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
    
        if graph.getGraph() == 0: graph.createGraph()

        common.G.add_node(self.number, agent = self)

        print "agent", self.agType, "#", self.number, "has been created"

        if len(common.G.nodes()) == common.N_AGENTS: graph.initializeEdges()

    def getGraph(self): 
        return common.G

    # return neighbour list. call with no arguments
    def listNeighbours(self):
        return common.G.neighbors(self.number)

