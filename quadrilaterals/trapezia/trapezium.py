import math
from ..quadrilateral import Quadrilateral, FurtherInformationRequired


class Trapezium(Quadrilateral):
    """
    Base class common to all trapezia.

    >>> q = quadrilaterals.Trapezium(5, 7, 5, 4, 4)

    """

    def __init__(
            self, parallel_side_A_length, parallel_side_B_length,
            non_parallel_side_A_length, non_parallel_side_B_length, height=None
    ):
        super().__init__(
            parallel_side_A_length, non_parallel_side_A_length,
            parallel_side_B_length, non_parallel_side_B_length
        )
        self.number_axes_of_symmetry = 0
        self.height = height
        self.message_unknown = (
            "This is not strictly known until a height value is set for the "
            "trapezium."
        )

    def area(self):
        """ Return the area of the trapezium.

    >>> q = quadrilaterals.Trapezium(5, 7, 5, 4, 4)
    >>> q.area()
    24.0
        """
        if self.height:
            return (
                0.5 * (self.side_1_length + self.side_3_length) *
                self.height

            )
        else:
            raise FurtherInformationRequired(self.message_unknown)
