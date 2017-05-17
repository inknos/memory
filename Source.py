# NewAgent.py
from Tools import *
from agTools import *
from Agent import *
import numpy as np
import commonVar as common
import math

class Source(Agent):

    #ptpt def __init__(self, number,myWorldState, xPos, yPos, lX =-20,rX=19, bY=-20,tY=19, agType=""):
    def __init__(self, number,myWorldState, agType=""):
        #ptpt Agent.__init__(self, number,myWorldState, xPos, yPos, lX =-20,rX=19, bY=-20,tY=19, agType=agType)
        Agent.__init__(self, number,myWorldState, agType=agType)
        self.news = {}
        
        self.reliability = np.random.random_sample()        

        # source state
        # inizializzato a zero
        self.state = np.zeros(common.dim)
        # number of relevant topics for the source: 1, 2 or 3
        r = np.random.randint(1,4)
        # added r number of ones and noise: the noise is 0.15 for one single topic, 0.1 for 2 and 0.5 for three
        for i in range(r):
            self.state[i] = 1
        for i in range(common.dim):
            self.state[i] += ( 0.15 / r ) * np.random.random_sample()
        # the state is shuffled because the topics are not in a partcular order. then it's normalized
        np.random.shuffle(self.state)
        self.state = self.state / self.state.sum()
        print self.state
        if (common.cycle/24.).is_integer():
            self.generateNews()
        print self.news 

    def sleep(self, **d):
        print "I'm %s agent # %d: " % (self.agType, self.number),
        print "happy to sleep!"


    def generateNews(self, n=3):
        """generates a dictionary of n news"""
        # the first part is the id-source, id-mittant, time
        for i in range(n):
            self.news['n'+str(i)] = {}
            self.news['n'+str(i)]['id-source'] = self.number
            self.news['n'+str(i)]['id-sender'] = self.number
            self.news['n'+str(i)]['date-source'] = common.cycle
            self.news['n'+str(i)]['relevance'] = np.random.random_sample()
            tmp = self.state
            for j in range(common.dim):
                tmp[j] += 0.1 * np.random.random_sample()

            tmp = tmp / tmp.sum()
            self.news['n'+str(i)]['new'] = tmp

        print self.number, " generateNews ", n


"""
    # movement
    def randomMovement(self,**k):
        print "I'm %s agent # %d: " % (self.agType,self.number),
        print "absolutely not moving!!!"
"""
