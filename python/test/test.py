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
sys.path.append("../src")

import parseOptitrackCSV as optitrack

if __name__ == '__main__':
    rigidBody = optitrack.RigidBody('test.csv')
    print(rigidBody.position)

    print(rigidBody.marker)
