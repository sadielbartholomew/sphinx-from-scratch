import math
from ..quadrilateral import Quadrilateral, AngleInformationRequired


class Parallelogram(Quadrilateral):
    """
    Base class common to all parallelograms.

    >>> import math
    >>> q1 = quadrilaterals.Parallelogram(2, 5, 1.1)
    >>> q2 = quadrilaterals.Parallelogram(2, 5, math.pi - 1.1)

    """

    def __init__(
            self,
            parallel_side_A_length, parallel_side_B_length, any_angle=None):
        super().__init__(
            parallel_side_A_length, parallel_side_B_length,
            parallel_side_A_length, parallel_side_B_length,
        )
        self.number_axes_of_symmetry = 0
        self.included_angle = any_angle

    def area(self):
        """ Return the area of the parallelogram.

    >>> q1 = quadrilaterals.Parallelogram(2, 5, 1.1)
    >>> q1.area()
    8.912073600614354
    >>> q2 = quadrilaterals.Parallelogram(2, 5, math.pi - 1.1)
    >>> q2.area()  == q1.area()
    True

        """
        if self.included_angle:
            return (
                self.side_1_length * self.side_2_length *
                math.sin(self.included_angle)
            )
        else:
            raise AngleInformationRequired()
