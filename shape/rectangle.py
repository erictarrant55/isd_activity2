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

        self.__length = length  
        self.__width = width   
   
    @property
    def length(self) -> float:
        """Gets the length of the rectangle.
        
            Returns:
                float: The length of the rectangle
        """
        return self.__length

    @property
    def width(self) -> float:
        """Gets the width of the rectangle.
        
            Returns:
                float: The width of the rectangle
        """        
        return self.__width


    @property
    def area(self) -> float:
        """Gets the area of the rectangle
        
            Returns:
                float: The area of the triangle.
        """

        return self.__length * self.__width

    @abstractmethod
    def get_perimeter(self) -> float:
        """Gets the perimeter of the rectangle
        
            Returns:
                float: The perimeter of the rectangle
        """
        return 2 * (self.__length * self.__width)

    def __str__(self):
        return (
            f"{super().__str__()}\n"
            f"This rectangle is the length of {self.length}cm"
            f"and the width of {self.__width}cm"
        )