import math
from ..quadrilateral import Quadrilateral, AngleInformationRequired


class Parallelogram(Quadrilateral):
    """
    Base class common to all parallelograms.
    """

    def __init__(
            self, longer_side_length, shorter_side_length, smaller_angle=None):
        self.side_1_length = longer_side_length
        self.side_2_length = shorter_side_length
        self.side_3_length = longer_side_length
        self.side_4_length = shorter_side_length

        self.included_angle = smaller_angle

        self.axes_of_symmetry = 0

    def area(self):
        """ Return the area of the parallelogram.
        """
        if self.included_angle:
            return (
                self.side_1_length * self.side_2_length *
                math.sin(self.included_angle)
            )
        else:
            raise AngleInformationRequired()
