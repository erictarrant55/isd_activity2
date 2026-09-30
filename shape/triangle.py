__author__ = "Eric Tarrant"
__version__ = "1.0.0"

from shape.shape import Shape
from shape.shape import abstractmethod


class Triangle():
    """Represents a triangle."""
    def __init__(
            self,
            color: str,
            side_1: float,
            side_2: float,
            side_3: float):

        if side_1 <= 0:
            raise ValueError("side_1 must be a value greater than zero")

        if side_2 <= 0:
            raise ValueError("side_2 must be a value greater than zero")

        if side_3 <= 0:
            raise ValueError("side_3 must be a value greater than zero")


        if (side_1 + side_2 <= side_3 or
            side_1 + side_3 <= side_2 or
            side_2 + side_3 <= side_1):
            raise ValueError("The sides do not satisfy the Triangle" \
            "Inequality Theorem")

        self.__side_1 = side_1
        self.__side_2 = side_2
        self.__side_3 = side_3



    @property
    def area(self) -> float:
        """Represents the area of the triangle
        
            Returns:
                float: the area of the triangle
        """
        semi_perimeter = self.get_perimeter() / 2
        return (
            semi_perimeter
            * (semi_perimeter - self.__side_1)
            * (semi_perimeter - self.__side_2)
            * (semi_perimeter - self.__side_3)
        )

    @abstractmethod
    def get_perimeter(self) -> float:
        """Gets the perimeter of the triangle.
        
            Args:
                float: p = side1 + side2 +side3
        """
        return self.__side_1 + self.__side_2 + self.__side_3

    def __str__(self) -> str:
        return (f"Side_1 {self.__side_1}\n" 
                f"Side_2 {self.__side_2}\n"
                f"Side_3 {self.__side_3}")
