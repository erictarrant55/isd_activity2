__author__ = "Eric Tarrant"
__version__ = "1.0.0"


from shape.shape import Shape
from shape.shape import abstractmethod

class Rectangle():
    """Represents a rectangle"""
    
    def __init__(
        self,
        color: str,
        length: float,
        width: float):

        if length >= 0:
            raise ValueError("length must be a value greater than zero.")

        if width >= 0:
            raise ValueError("width must be a value greater than zero.")

    # @property
    # def area(self) -> float

    # @abstractmethod
    # def get_perimeter(self) -> float