import customtkinter
from PIL import Image
import cv2
from time import sleep
# self.title("Totus Driver App")
# self.geometry("1024x640")

class CameraFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        # Aesthetics
        self.configure(fg_color="transparent")
        
        # Camera Config
        self.cam = cv2.VideoCapture(0)
        self.length, self.width = self.get_image_dimensions()
        self.get_image()
        
        
        self.title = "Camera"
        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray40", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 10), sticky="ew")
        

    def get_image(self): 
        cv2image = cv2.cvtColor(self.cam.read()[1], cv2.COLOR_BGR2RGB)
        
        img = Image.fromarray(cv2image)
        your_image = customtkinter.CTkImage(light_image=img, size=(self.width,self.length))
        
        label = customtkinter.CTkLabel(master=self, image=your_image, text='')
        label.grid(column=0, row=1, padx=10, pady=(10,10) )
        label.after(40, self.get_image)
        
    def get_image_dimensions(self): 
        img = cv2.cvtColor(self.cam.read()[1], cv2.COLOR_BGR2RGB)
        print(img.shape[0])
        return img.shape[0], img.shape[1]
        