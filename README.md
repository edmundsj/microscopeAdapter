# microscopeAdapter
Adapter that converts a 38mm tube lens to Thorlabs 30mm cage system for mounting subsequent optics.


## Getting Started
To generate an STL file for this project, you need to do the following (if you want to modify the STL, otherwise just download it):

### Installing Dependencies

If you have not already, install the [openSCAD](http://www.openscad.org/) and [openpyscad](https://pypi.org/project/openpyscad/)

### Verify file, generate STL

Once this is done, run the `thorlabs_cage_plate.py` script. This should generate the source file for openSCAD. Then, open openSCAD and load in the `thorlabs_microscope_adapter.scad` file. Verify the thing looks correct (rendering has a large number of edges), and build it by pressing `F6` (`fn -> F6` if on a mac), and then `File->Export` the STL file.

Done!

