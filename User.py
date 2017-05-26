# User.py
from Tools import *
from agTools import *
from Agent import *
import commonVar as common
import numpy as np
import sys


class User(Agent):

    def __init__(self, number, myWorldState, agType=""):
        Agent.__init__(self, number, myWorldState,
                       agType=agType)  # parent constructor
        self.database = {}
        self.active = False
        self.activate()
        self.inactiveTime = 0
        self.activeTime = 0

    def activate(self, p=0.5):
        """

        activate the agent with a probability p.

        """
        if np.random.random_sample() < p:
            self.active = False
        else:
            self.active = True

    def listNeighbours(self):
        """

        return neighbour list. call with no arguments

        """
        print("list neighbours", common.G.neighbors(self.number))
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

        # read anything
        if news == {}:
            return False

        print(self.distance(news['new']))
        # if a news is beautiful forget the worse
        if len(self.database) == common.memorySize:
            if self.distance(news['new']) > threshold:
                tmin = 1
                for key in self.database:
                    if self.distance(self.database[key]['new']) < tmin:
                        tmin = self.distance(self.database[key]['new'])
                del(self.database[key])
        # add element to memory
        self.database[news['id-n']] = news    # else append new
        print("Agent", self.number, "remembered", self.database)
        # cut memory
        if cutoldest is True:
            # while len memory > size of memory cut first element
            while len(self.database) > common.memorySize:
                tdate = sys.maxsize
                kmin = 0
                for key in self.database:
                    if self.database[key]['date-creation'] < tdate:
                        tdate = self.database[key]['date-creation']
                        kmin = key
                del(self.database[kmin])
        # random forget
        if np.random.random_sample() < rnd:
            if self.database == {}:
                pass
            else:
                forgot = self.database[random.choice(list(self.database))]
                if forgot != news:
                    print("Agent", self.number, "forgot", forgot)
                    del(forgot)
        return True

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
                temp.update(self.getAllNewsFromUser(ne))
            else:
                temp.update(self.getAllNewsFromSource(ne))

        """
        # remove old news
        for key in temp:
            if common.cycle - temp[key]['date-source'] > old:
                del temp[key]
        if temp == {}:
            temp = {'empty':{}}
        """
        return temp

    def getAllNewsFromSource(self, n):
        for i, j in enumerate(common.G.nodes()):
            if j == n:
                return common.G.nodes(data=True)[i][1]['agent'].database

    def getAllNewsFromUser(self, n):
        """

        TODO

        """
        # for i, j in enumerate(common.G.nodes()):
        #   if j == n:
        #        pass
        return {}

    def becomeActive(self, t=7, p=0.08):
        if self.inactiveTime > t:
            if np.random.random_sample() < self.inactiveTime * p:
                self.switchActivation()

    def becomeInactive(self, t=2, p=0.08, tired=False, tiredness=1.5):
        if tired is True:
            p = p * tiredness
        if self.activeTime > t:
            if np.random.random_sample() < self.activeTime * p:
                self.switchActivation()

    def firstAction(self):
        """

        bunch of actions

        """

        if self.active is False:
            print("Agent ", self.number, " is inactive")
            self.inactiveTime += 1
            # se sono da troppo tempo inattivo mi attivo al turno dopo
            self.becomeActive(t=3, p=0.08)
            return 0

        print("Agent ", self.number, " is active")
        self.activeTime += 1
        print("#1")
        newsToChose = self.readNews()
        print("#2")
        iWantToRemember = self.chooseNews(newsToChose)
        print("#3")
        print("#4")
        self.becomeInactive(tired=self.remember(iWantToRemember))
        print("#5")

    def hasNews(self, id_source=0, date=1):
        if self.database == {}:
            return False
        for key in self.database:
            if self.database[key]['id-source'] == id_source and self.database[key]['date-creation'] == date:
                return True
            else:
                return False

    def chooseNews(self, newsdict):
        """

        takes dict of dicts as argument
        returns the best internal dict according to the distance

        """
        if newsdict == {}:
            return newsdict
        temp = -1
        for key in newsdict:
            if self.distance(newsdict[key]['new']) > temp:
                temp = self.distance(newsdict[key]['new'])
        return newsdict[key]
