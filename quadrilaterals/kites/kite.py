import math
from ..quadrilateral import Quadrilateral, AngleInformationRequired


class Kite(Quadrilateral):
    """
    Base class common to all kites.

>>> q = quadrilaterals.Kite(3, 5, 2.4)

    """

    def __init__(self, side_A_length, side_B_length, angle_AB=None):
        super().__init__(
            side_A_length, side_B_length, side_A_length, side_B_length
        )
        self.number_axes_of_symmetry = 1
        self.included_angle = angle_AB  # angle must be in radians

    def area(self):
        """ Return the area of the kite.

        Example:

    >>> q = quadrilaterals.Kite(3, 5, 2.4)
    >>> q.area()
    10.131947708267264

        """
        if self.included_angle:
            return (
                self.side_1_length * self.side_2_length *
                math.sin(self.included_angle)
            )
        else:
            raise AngleInformationRequired()
