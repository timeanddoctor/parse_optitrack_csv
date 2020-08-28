#!/usr/bin/env python3

###########################################################################
#####                        parseOptitrackCSV                        #####
#####                            Raul Tapia                           #####
#####      GRVC Robotics Laboratory at the University of Seville      #####
###########################################################################

# @file    parseOptitrackCSV.py
# @brief   Test for parseOptitrackCSV function.
# @author  Raul Tapia

import sys
import matplotlib.pyplot as plt
sys.path.append("../src")

import parseOptitrackCSV as optitrack

if __name__ == '__main__':
    rigidBody = optitrack.RigidBody('test.csv')

    for i in sorted(rigidBody.framesWithError, reverse=True):
        del rigidBody.time[i]
        del rigidBody.position[i]

    x = [x[0] for x in rigidBody.position]
    y = [y[1] for y in rigidBody.position]
    z = [x[2] for z in rigidBody.position]

    plt.plot(rigidBody.time, [x[0] for x in rigidBody.position])
    plt.plot(rigidBody.time, [y[1] for y in rigidBody.position])
    plt.plot(rigidBody.time, [z[2] for z in rigidBody.position])
    plt.show()
