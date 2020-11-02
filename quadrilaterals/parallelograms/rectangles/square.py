from ...kites.rhombi.rhombus import Rhombus
from ..rectangles.rectangle import Rectangle


class Square(Rectangle, Rhombus):
    """
    Base class common to all squares.

    >>> import quadrilaterals
    >>> q = quadrilaterals.Square(0.2)

    """
    dimensions = 2
    sides = 4

    def __init__(self, side_length):
        super(Rectangle, self).__init__(
            side_length, side_length
        )
        self.number_axes_of_symmetry = 4

    def area(self):
        """ Return the area of the square.

    >>> q = quadrilaterals.Square(0.2)
    >>> q.area()
    0.04000000000000001

        """
        return self.side_1_length ** 2
