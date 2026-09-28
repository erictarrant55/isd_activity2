from abc import ABC, abstractmethod

class Shape(ABC):

    def __init__(
            self,
            color: str,
            area: float):
        
        if color == "":
            raise ValueError("Color cannot be blank")

        self.__color = color
        self.__area = area
    
    @property
    def color(self) -> str:
        """Gets the color of the shape.
        
            Returns: 
                str : The color of the shape.
        """
        return self.__color

    @property
    def area(self) -> float:
        """Gets the area of the shape.
        
            Returns
                float : The area of the shape.
        """
        return self.__area

    @abstractmethod
    def get_perimeter(self) -> float:
        """Gets the perimeter of the shape.
        
            Args:
                float: The perimeter of the shape
        """
        pass

    def __str__(self) -> str:
        return (f"Color: {self.__color}\n"
                f"Area: {self.__area}")