from multiprocessing import Process

import gaming_controller
import settingsApp

def countdown(n): 
    print("Start")
    while n > 0:
        n = n - 1
    print("Stop")

if __name__=="__main__":
    p1 = Process(target = countdown, args=[2000000])
    p2 = Process(target = gaming_controller.run_gaming_controller, args=['10.0.0.202:5000', 1], ) #kwargs={'host': "0.0.0.0", 'port': 5000, 'reload':True}
    p3 = Process(target = settingsApp.startApp, kwargs={"ROOT_ADDRESS" : "10.0.0.202:5000"} )
    
    p2.start()
    p1.start()
    p3.start()
    
    p2.join()
    p1.join()
    p3.join()