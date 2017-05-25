# parameters.py
from Tools import *
import commonVar as common
import numpy as np
import random


def loadParameters(self):

    # Projct version: contained in commonVariables.py
    try:
        projectVersion = str(common.projectVersion)
    except:
        projectVersion = "Unknown"
    print("\nProject version " + projectVersion)

    mySeed = eval(input("random number seed (1 to get it from the clock) "))
    if mySeed == 1:
        random.seed()
        np.random.seed()
    else:
        random.seed(mySeed)
        np.random.seed(mySeed)

    """

    nAgents, worldXSize, worldYSize are variables from the object ModelSwarm in ModelSwarm.py


    """
    #ptptself.nAgents = input("How many 'bland' agents? ")
    self.nAgents = 0
    print("No 'bland' agents")

    #self.worldXSize= input("X size of the world? ")
    self.worldXSize = 50
    print("X size of the world? ", self.worldXSize)

    #self.worldYSize= input("Y size of the world? ")
    self.worldYSize = 50
    print("Y size of the world? ", self.worldYSize)

    common.N_SOURCES = eval(
        input("How many sources? (default = " + str(common.N_SOURCES) + ") "))
    file = open(common.project + "/sources.txt", "w")
    for i in range(common.N_SOURCES):
        file.write(str(i) + '\n')
    file.close()

    common.N_USERS = eval(
        input("How many users? (default = " + str(common.N_USERS) + ") "))
    file = open(common.project + "/users.txt", "w")
    for i in range(common.N_USERS):
        file.write(str(common.N_SOURCES + i) + '\n')
    file.close()

    common.averageDegree = eval(input(
        "Enter average degree for users? (default = " + str(common.averageDegree) + ") "))
    common.P_a = float(common.averageDegree) / common.N_USERS
    common.P_s = 10 * common.P_a
    common.N_AGENTS = common.N_USERS + common.N_SOURCES

    self.nCycles = eval(input("How many cycles? (0 = exit) "))
