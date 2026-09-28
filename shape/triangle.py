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

        if side_1 >= 0:
            raise ValueError("side_1 must be a value greater than zero")

        if side_2 >= 0:
            raise ValueError("side_2 must be a value greater than zero")

        if side_3 >= 0:
            raise ValueError("side_3 must be a value greater than zero")

        self.__side_1 = side_1
        self.__side_2 = side_2
        self.__side_3 = side_3

    # def triangle_area_formula

    @property
    def area(self) -> float:
        """"""

    @abstractmethod
    def get_perimeter(self) -> float:
        """Gets the perimeter of the triangle.
        
            Args:
                float: p = side1 + side2 +side3
        """
        pass

    def __str__(self) -> str:
        return (f"Side_1 {self.__side_1}\n" 
                f"Side_2 {self.__side_2}\n"
                f"Side_3 {self.__side_3}")
