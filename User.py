# NewAgent.py
from Tools import *
from agTools import *
from Agent import *
import commonVar as common

class User(Agent):

    def __init__(self, number, myWorldState, agType=""):
        Agent.__init__(self, number, myWorldState, agType=agType)
        
        self.memory = 0

        self.activate()
        self.inactiveTime = 0
        self.activeTime = 0

    def activate(self):
        """activates with a probability (initialization)"""
        if np.random.random_sample() < 0.5: self.active = False
        else: self.active = True

    def listNeighbours(self):
        """return neighbour list. call with no arguments"""
        return common.G.neighbors(self.number)

    def listNeighboursNode(self, n):
        """return neighbour list of a node n"""
        return common.G.neighbors(n)

    def isUser(self, n):
        """return True if node n is a user"""
        if n < common.N_SOURCES: return False
        else: return True

    def getStateFromNode(self, n): 
        """return state from agent in node n"""
        return common.G.nodes(data=True)[n][1]['agent'].state

    def createEdge(self, n):
        """create link with a node with id a"""
        common.G.add_edge(self.number, n)

    def removeEdge(self, n):
        """removes link with a node with id a"""
        common.G.remove_edge(self.number, n)

    def distanceSP(self, n):
        """return state distance between self state and another vector with scalar product"""
        return np.dot(self.state, n)

    def remember(self, news):
        """register news in a log file 'memory'. if memory is 'full' cut the oldest"""
        if self.memory == 0: self.memory = array([news]) # if first news create array of news
        else: self.memory = append(self.memory, news)    # else append new

        while self.memory.shape[0] > common.memorySize:  # while len memory > size of memory cut first element
            self.memory = np.delete(self.memory, 0, 0)

    def switchActivation(self):
        """switches activation of the user"""
        if self.active == True:
            self.active = False
        else:
            self.active = True
        self.inactiveTime = 0
        self.activeTime = 0

    def firstAction(self):
        """bunch of actions"""
        if self.active == False: 
            print "Agent ", self.number, " inactiiiiiive iiiis"
            self.inactiveTime += 1
            # se sono da troppo tempo inattivo mi attivo al turno dopo
            if self.inactiveTime > 7:
                if np.random.random_sample() < self.inactiveTime*0.08:
                    self.switchActivation()
            return 0

        print "Agent ", self.number, " actiiiiiive iiiis"
        self.activeTime += 1





