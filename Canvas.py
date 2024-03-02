import pyopengltk
from OpenGL.GL import *

class Canvas(pyopengltk.OpenGLFrame):
    
    def __init__(self, parent, *args, **kwargs) -> None:
        """
        Initializes the App object.

        Args:
            parent (App): The parent MainApp object.
            **kwargs: Additional keyword arguments to pass to the parent class initializer.
        """
        super().__init__(parent, *args, **kwargs)
        Canvas.width = 400
        Canvas.height = 400
        # Main frame
        self.parent = parent
         # Set background color
        self.bg_color = (0.8, 0.8, 0.8, 1.0)  
        self.configure(bg="black")

    def initgl(self):
        """
        Initializes OpenGL
        """
        glClearColor(*self.bg_color)  # Set the clear color to the background color