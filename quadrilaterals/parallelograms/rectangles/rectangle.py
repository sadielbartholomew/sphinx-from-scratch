import math
from ..parallelogram import Parallelogram


class Rectangle(Parallelogram):
    """
    Base class common to all rectangles.

    >>> import quadrilaterals
    >>> q = quadrilaterals.Rectangle(80, 200)

    """

    def __init__(self, height, width):
        super().__init__(
            height, width, any_angle=math.pi/2
        )
        self.number_axes_of_symmetry = 2

    def area(self):
        """ Return the area of the rectangle.

    >>> q = quadrilaterals.Rectangle(80, 200)
    >>> q.area()
    16000

        """
        return self.side_1_length * self.side_2_length
