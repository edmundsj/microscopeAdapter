# microscopeAdapter
Adapter that converts a 38mm tube lens to Thorlabs 30mm cage system for mounting subsequent optics.


## Getting Started
To generate an STL file for this project, you need to do the following (if you want to modify the STL, otherwise just download it):

### Installing Dependencies

If you have not already, install the [openSCAD](http://www.openscad.org/) and [openpyscad](https://pypi.org/project/openpyscad/)

### Verify file, generate STL

Once this is done, run the `thorlabs_cage_plate.py` script. This should generate the source file for openSCAD and use the command line interface of openSCAD to create an .stl file. Verify that the .stl file looks OK, and you are good to go.


### Debugging

The main issue you may run into is openSCAD not being on your path. If this is the case, you need to add openscad to your path or manually create the .stl file in openscad.
