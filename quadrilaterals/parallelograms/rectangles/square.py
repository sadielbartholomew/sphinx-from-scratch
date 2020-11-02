from ...kites.rhombi.rhombus import Rhombus


class Square(Rhombus):
    """
    Base class common to all squares.
    """
    dimensions = 2
    sides = 4

    def __init__(self, side_length):
        self.side_1_length = side_length
        self.side_2_length = side_length
        self.side_3_length = side_length
        self.side_4_length = side_length

        self.axes_of_symmetry = 4

    def area(self):
        """ Return the area of the square.
        """
        return self.side_1_length ** 2
