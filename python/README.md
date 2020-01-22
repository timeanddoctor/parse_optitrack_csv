# Parse Optitrack CSV - Python Version
2020, [ GRVC Robotics Laboratory at the University of Seville](https://grvc.us.es/).

Parse exported csv files from Motive software.

The RigidBody class constructor has as input the csv filename and lets instance an object with the with the following attributes:
* frame
* time
* quaternion
* position
* meanMarkerError
* marker
* framesWithError

## Dependencies
* [Python 2+ or 3+](https://www.python.org/)

## Usage
```
import parseOptitrackCSV
rigidBody = parseOptitrackCSV.RigidBody('file.csv')
```

## Test
parseOptitrackCSV.py can be tested using:
```
python test.py
```
```
python3 test.py
```
