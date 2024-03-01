import pyopengltk

class Canvas(pyopengltk.OpenGLFrame):
    
    def __init__(self, parent, *args, **kwargs) -> None:
        """
        Initializes the App object.

        Args:
            parent (App): The parent MainApp object.
            **kwargs: Additional keyword arguments to pass to the parent class initializer.
        """
        super().__init__(parent, *args, **kwargs)
        
        Canvas.width = self.winfo_width()
        Canvas.height = self.winfo_height()
