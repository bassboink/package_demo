#Importing a module - needs to be located in the same directory to work
from module import demo_module

#Importing modules individually from a package
from package.add import add_together
from package.subtract import subtract_together

#Importing a library from PyPI
import numpy

#Importing a library from a locally built wheel file
#Run "python setup.py bdist_wheel" to build a wheel file from source (requires "pip install twine" if twine has not been installed already)
#Then the wheel file can be installed by running pip install sample_library-0.0.1-py3-none-any.whl
from sample_library.main import add_from_library

#Running from just a module
demo_module("Test")

#Running from a package
add_together(2,3)
subtract_together(2,3)

#Running from a PyPI library - requires a pip install to work
print(numpy.add(2,3))

#Running from a locally installed library - requires a pip install to work
print(add_from_library(7,2))