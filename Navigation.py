from customtkinter import *
from ImageButton import ImageButton

class Navigation(CTkFrame):
    def __init__(self, parent, **kwargs):
        """
        Initializes the Navigation object.

        Args:
            parent (App): The parent CTk object.
            **kwargs: Additional keyword arguments to pass to the parent class initializer.

        Raises:
            TypeError: If the list of buttons is empty.
        """
        super().__init__(parent, **kwargs)
        
        # Create buttons for cubes, spheres, and pyramids
        cube_button = ImageButton(self, "Icons_folder/cube.png")
        cube_button.pack()

        sphere_button = ImageButton(self, "Icons_folder/food.png " )
        sphere_button.pack()

        pyramid_button = ImageButton(self,"Icons_folder/pyramid-chart.png")
        pyramid_button.pack()
        