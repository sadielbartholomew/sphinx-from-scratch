class Quadrilateral:
    """
    Base class common to all quadrilaterals, four-sided polygons.

    >>> q = quadrilaterals.Quadrilateral(1, 2, 3, 4)

    """
    dimensions = 2
    sides = 4

    def __init__(
            self, side_A_length, side_B_length, side_C_length, side_D_length):
        self.side_1_length = side_A_length
        self.side_2_length = side_B_length
        self.side_3_length = side_C_length
        self.side_4_length = side_D_length

        self.number_axes_of_symmetry = None

        self.message_unknown = (
            "This is not known for an irregular quadrilateral when "
            "we only know the side lengths."
        )

    def area(self):
        """ Return the area of the polygon.

    >>> q = quadrilaterals.Quadrilateral(1, 2, 3, 4)
    >>> q.area()
    NotImplementedError: This is not known for an irregular quadrilateral when we only know the side lengths.

        """
        raise FurtherInformationRequired(self.message_unknown)

    def axes_of_symmetry(self):
        """ Return the number of axes of symmetry of the quadrilateral.

    >>> q.axes_of_symmetry()
    NotImplementedError: This is not known for an irregular quadrilateral when we only know the side lengths.

        """
        if self.number_axes_of_symmetry is None:  # distinguish from Falsy 0
            raise NotImplementedError(self.message_unknown)
        return self.number_axes_of_symmetry

    def perimeter(self):
        """ Return the perimeter of the quadrilateral.

    >>> q.perimeter()
    10

        """
        return (
            self.side_1_length +
            self.side_2_length +
            self.side_3_length +
            self.side_4_length
        )


class FurtherInformationRequired(Exception):
    """ Raised when further information is required to calculate something.
    """
    def __init__(self, message=None):
        if message is None:
            # Provide a default error message
            message = (
                "There is no way to calculate this without "
                "knowing further information about the quadrilateral."
            )
        super(FurtherInformationRequired, self).__init__(message)


class AngleInformationRequired(FurtherInformationRequired):
    """ Raised when an angle is required in order to calculate something.
    """
    def __init__(self):
        super().__init__(
            "There is no way to calculate the area without "
            "knowing or being able to deduce at least one of the "
            "angles as well as the side lengths for this geometry."
        )
