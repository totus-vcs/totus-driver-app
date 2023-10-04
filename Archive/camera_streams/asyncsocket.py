import socket
import pickle
import struct
import requests
import cv2


class CameraSocketReciever():

    def __init__(self, name, port, ip):
        # Init Variables
        self.name = name
        self.port = port
        self.ip = ip

        # Create Socket
        self.createSocket()

    def check_cam_on(self):
        url = "http://" + self.ip + ":5000/" + self.name + "/getstate"
        print("URL", url)
        return requests.get(url).json()

    def createSocket(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            print("Attempting Websocket Connection")
            client_socket.connect((host_ip, port))  # a tuple
        except:
            pass

        self.data = b""
        # Q: unsigned long long integer(8 bytes)
        self.payload_size = struct.calcsize("Q")

        while True:
            
            if self.check_cam_on == 'off': 
                self.createSocket()

            while len(data) < payload_size:
                # 4K, range(1024 byte to 64KB)
                packet = client_socket.recv(4 * 1024)
                if not packet:
                    break
                data += packet  # append the data packet got from server into data variable
            # will find the packed message size i.e. 8 byte, we packed on server side.
            packed_msg_size = data[:payload_size]
            data = data[payload_size:]  # Actual frame data
            msg_size = struct.unpack("Q", packed_msg_size)[0]  # meassage size
            # print(msg_size)

            while len(data) < msg_size:
                # will receive all frame data from client socket
                data += client_socket.recv(4 * 1024)
            frame_data = data[:msg_size]  # recover actual frame data
            data = data[msg_size:]
            # de-serialize bytes into actual frame type
            frame = pickle.loads(frame_data)
            cv2.imshow("Left Camera", frame)  # show video frame at client side
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):  # press q to exit video
                break
            


### Variables ###
host_ip = '10.0.0.202'  # paste your server ip address here
port = 8123
window_title = "Left Camera"

### Create Socket ###
while True:
    client_socket = socket.socket()

    try:
        print("Attempting Websocket Connection")
        client_socket.connect((host_ip, port))  # a tuple
    except:
        continue

    data = b""
    # Q: unsigned long long integer(8 bytes)
    payload_size = struct.calcsize("Q")

    # Recieve and Unpack Frames
    while True:
        while len(data) < payload_size:
            # 4K, range(1024 byte to 64KB)
            packet = client_socket.recv(4 * 1024)
            if not packet:
                break
            data += packet  # append the data packet got from server into data variable
        # will find the packed message size i.e. 8 byte, we packed on server side.
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]  # Actual frame data
        msg_size = struct.unpack("Q", packed_msg_size)[0]  # meassage size
        # print(msg_size)

        while len(data) < msg_size:
            # will receive all frame data from client socket
            data += client_socket.recv(4 * 1024)
        frame_data = data[:msg_size]  # recover actual frame data
        data = data[msg_size:]
        # de-serialize bytes into actual frame type
        frame = pickle.loads(frame_data)
        cv2.imshow("Left Camera", frame)  # show video frame at client side
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):  # press q to exit video
            break
