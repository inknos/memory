# parameters.py
from Tools import *
import commonVar as common
import numpy as np
import random
import usefulFunctions as uf


def loadParameters(self):

    # Projct version: contained in commonVariables.py
    try:
        projectVersion = str(common.projectVersion)
    except:
        projectVersion = "Unknown"
    print("\nProject version " + projectVersion)

    mySeed = int(uf.digit_input(
        msg="random number seed (1 to get it from the clock) ", DEFAULT=1))
    if mySeed == 1:
        random.seed()
        np.random.seed()
    else:
        random.seed(mySeed)
        np.random.seed(mySeed)

    """

    nAgents, worldXSize, worldYSize are variables from the object ModelSwarm in ModelSwarm.py


    """
    self.nAgents = 0
    # print("No 'bland' agents")

    # self.worldXSize= input("X size of the world? ")
    self.worldXSize = 50
    print("X size of the world? ", self.worldXSize)

    # self.worldYSize= input("Y size of the world? ")
    self.worldYSize = 50
    print("Y size of the world? ", self.worldYSize)
    common.N_SOURCES = int(uf.digit_input(
        msg="How many sources? (default = " + str(common.N_SOURCES) + ") ", DEFAULT=common.N_SOURCES))
    file = open(common.project + "/sources.txt", "w")
    for i in range(common.N_SOURCES):
        file.write(str(i) + '\n')
    file.close()

    common.N_USERS = int(uf.digit_input(
        DEFAULT=common.N_USERS, msg="How many users? (default = " + str(common.N_USERS) + ") "))
    file = open(common.project + "/users.txt", "w")
    for i in range(common.N_USERS):
        file.write(str(common.N_SOURCES + i) + '\n')
    file.close()

    common.averageDegree = uf.digit_input(
        msg="Enter average degree for users? (default = " + str(common.averageDegree) + ") ", DEFAULT=common.averageDegree)
    common.P_a = float(common.averageDegree) / common.N_USERS
    common.P_s = 10 * common.P_a
    common.N_AGENTS = common.N_USERS + common.N_SOURCES

    self.nCycles = uf.digit_input(
        msg="How many cycles? (0 = exit) ", DEFAULT=1)
