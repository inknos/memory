# NewAgent.py
from Tools import *
from agTools import *
from Agent import *


class User(Agent):

    def __init__(self, number, myWorldState, agType=""):

        Agent.__init__(self, number, myWorldState, agType=agType)

    # sleeping
    def sleep(self, **d):
        print "I'm %s agent # %d: " % (self.agType, self.number),
        print "happy to sleep!"

"""
    # movement
    def randomMovement(self,**k):
        print "I'm %s agent # %d: " % (self.agType,self.number),
        print "absolutely not moving!!!"
"""
