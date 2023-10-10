from multiprocessing import Process

import gaming_controller
import settingsApp
import cameraStream

# IP = '10.0.0.202'
IP = "192.168.195.54"
IP_ROOT = IP + ":5000"

def countdown(n): 
    print("Start")
    while n > 0:
        n = n - 1
    print("Stop")

front_camera = cameraStream.CameraStream("Front Camera", IP, 8152, 1.5)
left_camera = cameraStream.CameraStream("Left Camera", IP, 8160, 1.5)
# right_camera = cameraStream.CameraStream("Right Camera", "10.0.0.202", 8170, 2)


if __name__=="__main__":
    print(IP_ROOT)
    print()
    print()
    p1 = Process(target = countdown, args=[2000000])
    p2 = Process(target = gaming_controller.run_gaming_controller, args=[IP_ROOT, 1], ) #kwargs={'host': "0.0.0.0", 'port': 5000, 'reload':True}
    p3 = Process(target = settingsApp.startApp, kwargs={"ROOT_ADDRESS" : IP_ROOT} )
    
    p4 = Process(target = front_camera.listen)
    p5 = Process(target = left_camera.listen)
    # p6 = Process(target = right_camera.listen)
    
    p2.start()
    p1.start()
    p3.start()
    p4.start()
    p5.start()
    # p6.start()
    
    p2.join()
    p1.join()
    p3.join()
    p4.join()
    p5.start()
    # p6.start()