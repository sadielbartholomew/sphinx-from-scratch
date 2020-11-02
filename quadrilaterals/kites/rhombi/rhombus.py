from ..kite import Kite


class Rhombus(Kite):
    """
    Base class common to all rhombi.
    """

    def __init__(self, side_length, smaller_angle=None):
        self.side_1_length = side_length
        self.side_2_length = side_length
        self.side_3_length = side_length
        self.side_4_length = side_length

        self.included_angle = smaller_angle

        self.axes_of_symmetry = 2
