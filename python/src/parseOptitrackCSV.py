#!/usr/bin/env python3

###########################################################################
#####                        parseOptitrackCSV                        #####
#####                            Raul Tapia                           #####
#####      GRVC Robotics Laboratory at the University of Seville      #####
###########################################################################

# @file    parseOptitrackCSV.py
# @brief   Parse exported csv files from Motive software.
# @author  Raul Tapia

import csv

class Marker:
    position = []
    quality = []

    # Constructor for Marker
    # @param   px   Position of the marker in x axis
    # @param   py   Position of the marker in y axis
    # @param   pz   Position of the marker in z axis
    # @param   q    Quality of the marker
    def __init__(self, px, py, pz, q):
        position = (px, py, pz)
        quality = q

class RigidBody:
    frame = []
    time = []
    quaternion = []
    position = []
    meanMarkerError = []
    marker = []
    framesWithError = []

    # Constructor for RigidBody
    # @param   filename   Name of the csv file
    def __init__(self, filename):
        ### Load data
        file = open(filename, mode='r')

        ### Skip header
        for i in range(7):
            next(file)

        ### Instance reader
        reader = csv.DictReader(file, delimiter=',',fieldnames=["frame", "time", "rotationX", "rotationY", "rotationZ", "rotationW", "positionX", "positionY", "positionZ", "meanMarkerError"])

        for row in reader:
            self.frame.append(int(row["frame"]))
            self.time.append(float(row["time"]))

            ### Check if error
            if row["rotationX"] == '':
                self.quaternion.append('No value')
                self.position.append('No value')
                self.meanMarkerError.append('No value')
                self.marker.append('No value')
                self.framesWithError.append(self.time[-1])
            else:
                self.quaternion.append((float(row["rotationX"]),float(row["rotationY"]),float(row["rotationZ"]),float(row["rotationW"])))
                self.position.append((float(row["positionX"]),float(row["positionY"]),float(row["positionZ"])))
                self.meanMarkerError.append(float(row["meanMarkerError"]))

                ### Markers
                self.marker.append([])
                for k in range(int(len(row[None])/7)):
                    self.marker[-1].append(Marker(float(row[None][4*k]), float(row[None][4*k+1]), float(row[None][4*k+2]), float(row[None][4*k+3])))

        ### Close file
        file.close()

if __name__ == '__main__':
    print('\nparseOptitrackCSV.py')
    print('\nParse exported csv files from Motive software')
