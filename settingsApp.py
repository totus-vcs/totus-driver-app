import customtkinter, requests

class App(customtkinter.CTk):
    def __init__(self, ROOT_ADDRESS):
        super().__init__()
        
        self.ROOT_ADDRESS = ROOT_ADDRESS
        
        self.title("Totus Driver App")
        # self.geometry("1024x640")
        self.geometry("190x330")
        self.grid_columnconfigure((1,2), weight=1)
        self.grid_rowconfigure(0, weight=0)
        customtkinter.set_appearance_mode("Dark")

        # ROW 0
        self.title = "SETTINGS"
        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray40", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")
        
        # ROW 1 - Light and dark mode
        self.light_or_dark = "dark"
        self.light_dark_mode = customtkinter.CTkButton(self, text="Toggle Light/Dark Mode", command=self.light_dark_mode_cmd)
        self.light_dark_mode.grid(row=1, column=0, padx=10, pady=(10, 10), sticky="w")
        # gap
        
        # ROW 2, 3, 4 - Turn on/Off Pedals
        self.accellerator_on = customtkinter.CTkCheckBox(self, text="Turn Accellerator On", command=self.accellerator_on_cmd)
        self.accellerator_on.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="w")
        
        self.brake_on = customtkinter.CTkCheckBox(self, text="Turn Brake Pedal On", command=self.brake_on_cmd)
        self.brake_on.grid(row=3, column=0, padx=10, pady=(10, 0), sticky="w")
        
        self.steering_on = customtkinter.CTkCheckBox(self, text="Turn Brake Pedal On", command=self.brake_on_cmd)
        self.steering_on.grid(row=4, column=0, padx=10, pady=(10, 10), sticky="w")
        
    ### GENERAL COMMANDS
    
    def light_dark_mode_cmd(self): 
        if self.light_or_dark == "light":
            customtkinter.set_appearance_mode("Dark")
            self.light_or_dark = "dark"
        elif self.light_or_dark == "dark":
            customtkinter.set_appearance_mode("Light")
            self.light_or_dark = "light"
            
    def api_request(self, sub_address, message): 
        api_url = "http://" + self.ROOT_ADDRESS + sub_address
        print("Sending:", message, "TO:", api_url)
        data = {"value": message}
        requests.put(api_url, json=data)
        return None
        
    ### PEDAL ON COMMANDS
        
    def accellerator_on_cmd(self): 
        self.accellerator_on.get()
        if self.accellerator_on.get() == 1: 
            self.api_request("/accellerator/change_state", 'on')
        elif self.accellerator_on.get() == 0: 
            self.api_request("/accellerator/change_state", 'off')
            
    def brake_on_cmd(self): 
        self.brake_on.get()
        if self.brake_on.get() == 1: 
            self.api_request("/brake/change_state", 'on')
        elif self.brake_on.get() == 0: 
            self.api_request("/brake/change_state", 'off')
            
    def steering_on_cmd(self): 
        self.steering_on.get()
        if self.steering_on.get() == 1: 
            self.api_request("/steering/change_state", 'on')
        elif self.steering_on.get() == 0: 
            self.api_request("/steering/change_state", 'off')
            


def startApp(ROOT_ADDRESS):
    app = App(ROOT_ADDRESS=ROOT_ADDRESS)
    app.mainloop()
