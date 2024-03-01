from customtkinter import CTk
from constants import *
from Navigation import Navigation

class App(CTk):
    def __init__(self) -> None:
        """
        Initializes the app
        """
        super().__init__()  # Call CTk constructor with required parameters if any
        window_width = 1280
        window_height = 720
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
        self.title("3D Shape Drawer by: Sam Adrian P. Sabalo")
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=0, uniform="nav_col")
        self.grid_columnconfigure(1, weight=1, uniform="nav_col")
        
        navigation = Navigation(parent=self)
        navigation.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        
        
if __name__ == '__main__':
    App().mainloop()
