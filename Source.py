# NewAgent.py
from Tools import *
from agTools import *
from Agent import *
import numpy as np
import commonVar as common
import math


class Source(Agent):
    """

    Members:

    news: dictionary of dictionaries
    each one contains a news
    the news is made of several voices:
    - id-source: the number of the source
    - id-sender: the number of the last sender
    - date-source: date of creation
    - relevance: importance of the news
    - new: false english to identify a single news
    see generateNews

    reliability: importance of the source

    state: mind state of the source
    each source has almost all components of its state
    of mind near zero
    only one, two or three components are randomly chosen
    to be one
    after the first 'binary' initialization, noise
    is added; the vector is then normalized

    """

    def __init__(self, number, myWorldState, agType=""):
        Agent.__init__(self, number, myWorldState, agType=agType)
        self.news = {}
        self.reliability = np.random.random_sample()

        # source state
        self.state = np.zeros(common.dim)  # inizializzato a zero
        # number of relevant topics for the source: 1, 2 or 3
        r = np.random.randint(1, 4)
        # added r number of ones and noise: the noise is 0.15 for one single
        # topic, 0.1 for 2 and 0.5 for three
        for i in range(r):
            self.state[i] = 1
        for i in range(common.dim):
            self.state[i] += (0.15 / r) * np.random.random_sample()
        # the state is shuffled because the topics are not in a partcular
        # order. then it's normalized
        np.random.shuffle(self.state)
        self.state = self.state / self.state.sum()
        print self.state
        if (common.cycle / 24.).is_integer():
            self.generateNews()
        print self.news

    def generateNews(self, n=3, p=0.1):
        """

        generates a dictionary of n news:
        each new is distant from zero to p from
        the mind state of the source

        """

        # the first part is the id-source, id-mittant, time
        for i in range(n):
            self.news['n' + str(i)] = {}
            self.news['n' + str(i)]['id-source'] = self.number
            self.news['n' + str(i)]['id-sender'] = self.number
            self.news['n' + str(i)]['date-source'] = common.cycle
            self.news['n' + str(i)]['relevance'] = np.random.random_sample()
            tmp = self.state
            for j in range(common.dim):
                tmp[j] += 0.1 * np.random.random_sample()
            tmp = tmp / tmp.sum()
            self.news['n' + str(i)]['new'] = tmp

        print self.number, " generateNews ", n
