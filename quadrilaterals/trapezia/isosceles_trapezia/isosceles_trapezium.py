from ..trapezium import Trapezium


class IsoscelesTrapezium(Trapezium):
    """
    Base class common to all isosceles trapezia.

    >>> q = quadrilaterals.IsoscelesTrapezium(4, 5, 6)
    """

    def __init__(
            self, parallel_side_A_length, parallel_side_B_length,
            non_parallel_sides_length
    ):
        super().__init__(
            parallel_side_A_length, parallel_side_B_length,
            non_parallel_sides_length, non_parallel_sides_length,
        )

    @staticmethod
    def brahmagupta_formula(a, b, c, d):
        """Calculate area from side lengths for cyclic quadrilaterals only."""
        s = 0.5 * (a + b + c + d)
        return ((s - a) * (s - b) * (s - c) * (s - d)) ** 0.5

    def area(self):
        """ Return the area of the isosceles trapezium.

    >>> q = quadrilaterals.IsoscelesTrapezium(4, 5, 6)
    >>> q.area()
    26.906086671978144
        """
        # Using the fact that the two non-parallel sides have the same length
        return self.brahmagupta_formula(
            self.side_1_length, self.side_3_length,
            self.side_2_length, self.side_2_length
        )
