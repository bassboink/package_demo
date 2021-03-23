#Importing a module - needs to be located in the same directory to work
from module import demo_module

#Importing modules individually from a package
from package.add import add_together
from package.subtract import subtract_together

#Importing a library
import numpy


#Running from just a module
demo_module("Test")

#Running from a package
add_together(2,3)
subtract_together(2,3)

#Running from a library - requires a pip install to work
print(numpy.add(2,3))