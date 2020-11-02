'''
quadrilaterals

A dummy object-oriented codebase in Python modelling
categories of two-dimensional four-sided shape.
'''

import datetime


# Set module attributes:
__author__ = 'Sadie Bartholomew'
__date__ = datetime.datetime.now().strftime("%Y-%m-%d")
__version__ = '1.0'


# Raise an error elegantly if the module fails to import:
try:
    import quadrilaterals
except ImportError as err:
    raise ImportError(err)


# Establish the namespace by importing classes of the module ...
from .quadrilateral import Quadrilateral
# ... and the sub-modules
from .kites.kite import Kite
from .kites.rhombi.rhombus import Rhombus
from .parallelograms.parallelogram import Parallelogram
from .parallelograms.rectangles.rectangle import Rectangle
from .parallelograms.rectangles.square import Square
from .trapezia.trapezium import Trapezium
from .trapezia.isosceles_trapezia.isosceles_trapezium import IsoscelesTrapezium
