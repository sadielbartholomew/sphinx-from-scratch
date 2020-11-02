from ..parallelogram import Parallelogram
from ...trapezia.isosceles_trapezia.isosceles_trapezium import (
    IsoscelesTrapezium
)


class Rectangle(Parallelogram, IsoscelesTrapezium):
    """
    Base class common to all rectangles.
    """

    def __init__(self, height, side_width):
        self.side_1_length = height
        self.side_2_length = width
        self.side_3_length = height
        self.side_4_length = width

        self.axes_of_symmetry = 2

    def area(self):
        """ Return the area of the rectangle.
        """
        return self.side_1_length * self.side_2_width
