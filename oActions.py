from Tools import *
from Agent import *
import graph as graph


def do1b(address):

    #basic action to visualize the networkX output
    graph.openClearNetworkXdisplay()
    graph.drawGraph()


def do2a(address, cycle):
    self = address  # if necessary

    # ask each agent, without parameters

    print "Time = ", cycle, "ask all agents to report position"
    # askEachAgentInCollection(address.modelSwarm.getAgentList(),Agent.reportPosition)


def do2b(address, cycle):
    self = address  # if necessary

    # ask a single agent, without parameters
    print "Time = ", cycle, "ask first agent to report position"
    if address.modelSwarm.getAgentList() != []:
        print 'ciao'
        #askAgent(address.modelSwarm.getAgentList()[0], Agent.reportPosition)

"""             
def otherSubSteps(subStep, address):
    return False
"""
