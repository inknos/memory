# Agent.py
from Tools import *
from agTools import *

#Agent must be the partent class of every object. Must inherit from SuperAgent
class Agent(SuperAgent):
    """
    Create the parent agent

    Def. constructor:
    class Agent(SuperAgent):
        def __init__(self, number,myWorldState, xPos, yPos, lX =-20,rX=19, bY=-20,tY=19, agType="")
    """

    #ptpt
    #def __init__(self, number,myWorldState, xPos, yPos, lX =-20,rX=19, bY=-20,tY=19, agType=""):
    def __init__(self, number,myWorldState, agType=""):
        # the environment
        self.agOperatingSets = []
        self.number = number
        #ptpt
        """
        self.lX = lX
        self.rX = rX
        self.bY = bY
        self.tY = tY
        """
        if myWorldState != 0:
            self.myWorldState = myWorldState
        self.agType = agType
        # the agent
        #ptpt
        """
        self.xPos = xPos
        self.yPos = yPos
        """
        self.state = []
        print "agent", self.agType, "#", self.number, \
              "has been created"

    #ptpt
    #put here all the common methods (if necessary, they can be redefined within
    # the inhering classes)


    #ptpt
    #eliminated all the row below
