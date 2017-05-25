# User.py
from Tools import *
from agTools import *
from Agent import *
import commonVar as common
import numpy as np


class User(Agent):

    def __init__(self, number, myWorldState, agType=""):
        Agent.__init__(self, number, myWorldState,
                       agType=agType)  # parent constructor
        self.memory = np.array(
            [{'date': -1, 'new': -1 * self.state, 'id-source': -1}])
        self.active = False
        self.activate()
        self.inactiveTime = 0
        self.activeTime = 0

    def activate(self, p=0.5):
        """

        activate the agent with a probability p

        """
        if np.random.random_sample() < p:
            self.active = False
        else:
            self.active = True

    def listNeighbours(self):
        """

        return neighbour list. call with no arguments

        """
        print(common.G.neighbors(self.number))
        return common.G.neighbors(self.number)

    def listNeighboursNode(self, n):
        """

        return list of neughbours of a node n

        """
        return common.G.neighbors(n)

    def isUser(self, n):
        """

        return True if node n is a user

        """
        if n < common.N_SOURCES:
            print(n, " is ", False)
            return False
        else:
            print(n, " is ", True)
            return True

    def getStateFromNode(self, n):
        """

        return state from agent in node n

        """
        return common.G.nodes(data=True)[n][1]['agent'].state

    def createEdge(self, n):
        """

        create link with a node with id a

        """
        common.G.add_edge(self.number, n)

    def removeEdge(self, n):
        """

        removes link with a node with id a

        """
        common.G.remove_edge(self.number, n)

    def distance(self, n, a='scalar'):
        """

        Return state distance between self state and another vector.

        if you want to use different distances use the parameter a.

        scalar: use scalar product


        """
        if a == 'scalar':
            return np.dot(self.state, n)

    def remember(self, news, cutoldest=True, threshold=0.9, rnd=0.1):
        """

        register news in a log file 'memory'.
        the memory dimension is given from an extern file

        memory is ordered from the past to the present
        due to the append function.

        there are many ways to take care of full memory.
        specify in cut.

        oldest: if memory is 'full' cut the oldest

        """
        print("#1")
        print(self.distance(news['new']))
        # if a news is beautiful forget the worse
        if self.memory.shape[0] == common.memorySize:
            if self.distance(news['new']) > threshold:
                tmin = 1
                inde = 0
                for i, m in enumerate(self.memory):
                    if self.distance(m) < tmin:
                        tmin = self.distance(m)
                        inde = i
                self.memory = np.delete(self.memory, inde, 0)
        print("#2")

        # add element to memory
        self.memory = np.append(self.memory, news)    # else append new

        print("#3")
        # cut memory
        if cutoldest is True:
            # while len memory > size of memory cut first element
            while self.memory.shape[0] > common.memorySize:
                self.memory = np.delete(self.memory, 0, 0)
        print("qui")
        # random forget
        if np.random.random_sample() < rnd:
            if self.memory.shape[0] == 1:
                pass
            else:
                self.memory = np.delete(
                    self.memory, np.random.randint(0, self.memory.shape[0]), 0)
        print("fine")

    def switchActivation(self):
        """

        switches activation of the user

        """

        if self.active is True:
            self.active = False
        else:
            self.active = True
        self.inactiveTime = 0
        self.activeTime = 0

    def readNews(self, old=24):
        """

        read news from node n
        return all the possible readable news in a dictionary
        remove the oldest

        old: default 24. hours in which the news gets old

        """

        temp = {}
        l = self.listNeighbours()
        for ne in l:
            if self.isUser(ne):
                temp.update(self.chooseNewsFromUser(ne))
            else:
                temp.update(self.getAllNewsFromSource(ne))
        for key in temp:
            if common.cycle - temp[key]['date-source'] > old:
                del temp[key]
        return temp

    def getAllNewsFromSource(self, n):
        for i, j in enumerate(common.G.nodes()):
            if j == n:
                return common.G.nodes(data=True)[i][1]['agent'].news

    def chooseNewsFromUser(self, n):
        """

        TODO

        """
        return {}

    def firstAction(self):
        """

        bunch of actions

        """

        if self.active is False:
            print("Agent ", self.number, " is inactive")
            self.inactiveTime += 1
            # se sono da troppo tempo inattivo mi attivo al turno dopo
            if self.inactiveTime > 7:
                if np.random.random_sample() < self.inactiveTime * 0.08:
                    self.switchActivation()
            return 0

        print("Agent ", self.number, " is active")
        self.activeTime += 1
        newsToChose = self.readNews()
        iWantToRemember = {}
        temp = -1
        for key in newsToChose:
            if self.distance(newsToChose[key]['new']) > temp:
                temp = self.distance(newsToChose[key]['new'])
                iWantToRemember = newsToChose[key]
        self.remember(iWantToRemember)
        self.switchActivation()

    def hasNews(self, id_source=0, date=0):
        if self.memory != np.array([{'date': -1, 'new': -1 * self.state, 'id-source': -1}]):
            for m in self.memory:
                if m['id-source'] == id_source and m['date-source'] == date:
                    return True
                else:
                    return False
