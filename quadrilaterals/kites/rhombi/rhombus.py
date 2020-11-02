from ..kite import Kite
from ...parallelograms.parallelogram import Parallelogram


class Rhombus(Kite, Parallelogram):
    """
    Base class common to all rhombi.

    >>> q = quadrilaterals.Rhombus(4, 1.5)

    """

    def __init__(self, side_length, any_angle=None):
        super(Kite, self).__init__(
            side_length, side_length, any_angle
        )
        self.number_axes_of_symmetry = 2
        self.an_angle = any_angle
