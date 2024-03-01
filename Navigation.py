from customtkinter import *

class Navigation(CTkFrame):
    def __init__(self, parent: App, **kwargs):
        """
        Initializes the Navigation object.

        Args:
            parent (App): The parent CTk object.
            **kwargs: Additional keyword arguments to pass to the parent class initializer.

        Raises:
            TypeError: If the list of buttons is empty.
        """
        super().__init__(parent, **kwargs)