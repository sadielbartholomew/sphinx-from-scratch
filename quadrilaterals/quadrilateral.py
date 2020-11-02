class Quadrilateral:
    """
    Base class common to all quadrilaterals, four-sided polygons.

    >>> import quadrilateral
    >>> quadrilateral.Quadrilateral(3,4,5,6).perimeter()
    18
    >>> quadrilateral.Quadrilateral(3,4,5,6).area()
    NotImplementedError
    """
    dimensions = 2
    sides = 4

    def __init__(
            self, side_A_length, side_B_length, side_C_length, side_D_length):
        self.side_1_length = side_A_length
        self.side_2_length = side_B_length
        self.side_3_length = side_C_length
        self.side_4_length = side_D_length

        self.axes_of_symmetry = None

    def area(self):
        """ Return the area of the polygon.
        """
        raise NotImplementedError()

    def axes_of_symmetry(self):
        """ Return the number of axes of symmetry of the quadrilateral.
        """
        if self.axes_of_symmetry is None:  # distinguish from Falsy 0
            raise NotImplementedError("")
        return self.axes_of_symmetry

    def perimeter(self):
        """ Return the perimeter of the quadrilateral.
        """
        return (
            self.side_1_length +
            self.side_2_length +
            self.side_3_length +
            self.side_4_length
        )


class AngleInformationRequired(Exception):
    """ Raised when an angle is required in order to calculate something.
    """
    def __init__(self, message=None):
        if message is None:
            # Provide a default error message
            message = (
                "There is no way to calculate the area without "
                "knowing or being able to deduce at least one of the "
                "angles as well as the side lengths for this geometry."
            )
        super(AngleInformationRequired, self).__init__(message)
