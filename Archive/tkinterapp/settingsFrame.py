import customtkinter
import api_requests
# self.title("Totus Driver App")
# self.geometry("1024x640")

class SettingsFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        # self.configure(fg_color="transparent")
        
        self.title = "Settings"
        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray40", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")
        
        self.light_or_dark = "light"
        self.light_dark_mode = customtkinter.CTkButton(self, text="Toggle Light/Dark Mode", command=self.light_dark_mode_cmd)
        self.light_dark_mode.grid(row=1, column=0, padx=10, pady=(10, 10), sticky="w")
        
        self.accellerator_on = customtkinter.CTkCheckBox(self, text="Turn Accellerator On", command=self.accellerator_on_cmd)
        self.accellerator_on.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="w")
        
        self.brake_on = customtkinter.CTkCheckBox(self, text="Turn Brake Pedal On", command=self.brake_on_cmd)
        self.brake_on.grid(row=3, column=0, padx=10, pady=(10, 0), sticky="w")
        
        self.steering_on = customtkinter.CTkCheckBox(self, text="Turn Brake Pedal On", command=self.brake_on_cmd)
        self.steering_on.grid(row=4, column=0, padx=10, pady=(10, 10), sticky="w")
    
    def light_dark_mode_cmd(self): 
        if self.light_or_dark == "light":
            customtkinter.set_appearance_mode("Dark")
            self.light_or_dark = "dark"
        elif self.light_or_dark == "dark":
            customtkinter.set_appearance_mode("Light")
            self.light_or_dark = "light"
       
    def accellerator_on_cmd(self): 
        self.accellerator_on.get()
        if self.accellerator_on.get() == 1: 
            api_requests.value_message("/accellerator/change_state", 'on')
        elif self.accellerator_on.get() == 0: 
            api_requests.value_message("/accellerator/change_state", 'off')
            
    def brake_on_cmd(self): 
        self.brake_on.get()
        if self.brake_on.get() == 1: 
            api_requests.value_message("/brake/change_state", 'on')
        elif self.brake_on.get() == 0: 
            api_requests.value_message("/brake/change_state", 'off')
            
    def steering_on_cmd(self): 
        self.steering_on.get()
        if self.steering_on.get() == 1: 
            api_requests.value_message("/steering/change_state", 'on')
        elif self.steering_on.get() == 0: 
            api_requests.value_message("/steering/change_state", 'off')