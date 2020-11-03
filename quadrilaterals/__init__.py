'''
quadrilaterals

A dummy object-oriented codebase in Python modelling
categories of two-dimensional four-sided shape.

An example of creating an instance of each of the main classes available
in the Quadrilaterals API:

>>> import quadrilaterals
>>> quadrilateral = quadrilaterals.Quadrilateral(4, 6, 5, 8)

>>> square = quadrilaterals.Square(4)
>>> rhombus = quadrilaterals.Rhombus(4)
>>> rectangle = quadrilaterals.Rectangle(4, 6)
>>> kite = quadrilaterals.Kite(4, 6)
>>> parallelogram = quadrilaterals.Parallelogram(4, 3)
>>> isosceles_trapezium = quadrilaterals.IsoscelesTrapezium(4, 3, 8)
>>> trapezium = quadrilaterals.Trapezium(4, 3, 8, 2)

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
from .quadrilateral import (
    Quadrilateral, FurtherInformationRequired, AngleInformationRequired
)
# ... and the sub-modules
from .kites.kite import Kite
from .kites.rhombi.rhombus import Rhombus
from .parallelograms.parallelogram import Parallelogram
from .parallelograms.rectangles.rectangle import Rectangle
from .parallelograms.rectangles.square import Square
from .trapezia.trapezium import Trapezium
from .trapezia.isosceles_trapezia.isosceles_trapezium import IsoscelesTrapezium
