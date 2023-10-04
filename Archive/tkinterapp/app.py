import customtkinter
from settingsFrame import SettingsFrame
from cameraFrame import CameraFrame


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Totus Driver App")
        self.geometry("1024x640")
        self.grid_columnconfigure((1,2), weight=1)
        self.grid_rowconfigure(0, weight=0)

        # ROW 1
        self.settingsframe1 = SettingsFrame(self)
        self.settingsframe1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")
        
        self.cameraframe_front = CameraFrame(self)
        self.cameraframe_front.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="nsew", columnspan=2)
        
        
        # self.settingsframe2 = SettingsFrame(self)
        # self.settingsframe2.grid(row=0, column=3, padx=10, pady=(10, 0), sticky="nsew")

        # ROW 2
        # self.checkbox_frame = CameraFrame(self)
        # self.checkbox_frame.grid(row=1, column=0, padx=10, pady=(10, 10), sticky="nsew", columnspan=2)
        # self.checkbox_frame = CameraFrame(self)
        # self.checkbox_frame.grid(row=1, column=2, padx=10, pady=(10, 10), sticky="nsew", columnspan=2)
        
    
        # self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        # self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

    def button_callback(self):
        print("button pressed")

app = App()

app.cameraframe_front.get_image()
app.mainloop()
