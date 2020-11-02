from ..trapezium import Trapezium


class IsoscelesTrapezium(Trapezium):
    """
    Base class common to all isosceles trapezia.
    """

    def __init__(
            self, longer_side_length, shorter_side_length, smaller_angle=None):
        self.axes_of_symmetry = 1
