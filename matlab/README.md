# Parse Optitrack CSV - MATLAB Version
2020, [ GRVC Robotics Laboratory at the University of Seville](https://grvc.us.es/).

Parse exported csv files from Motive software.

The function parseOptitrackCSV returns a structure with the following elements:
* frame
* time
* quaternion
* position
* meanMarkerError
* marker
* framesWithError

## Dependencies
* [MATLAB](https://www.mathworks.com/products/matlab.html)

## Usage
```
rigidBody = parseOptitrackCSV('file.csv');
```

## Test
parseOptitrackCSV.m can be tested using test.m
