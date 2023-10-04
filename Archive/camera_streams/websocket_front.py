import socket, pickle, struct
import cv2


### Variables ###
host_ip = '10.0.0.202'  # paste your server ip address here
port = 9999
window_title = "Front Camera"

### Create Socket ###
while True: 
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        print("Attempting Websocket Connection")
        client_socket.connect((host_ip, port))  # a tuple
    except:
        continue

    data = b""
    payload_size = struct.calcsize("Q") # Q: unsigned long long integer(8 bytes)


    ## Recieve and Unpack Frames
    while True:
        while len(data) < payload_size:
            packet = client_socket.recv(4 * 1024)  # 4K, range(1024 byte to 64KB)
            if not packet: break
            data += packet # append the data packet got from server into data variable
        packed_msg_size = data[:payload_size] #will find the packed message size i.e. 8 byte, we packed on server side.
        data = data[payload_size:] # Actual frame data
        msg_size = struct.unpack("Q", packed_msg_size)[0] # meassage size
        # print(msg_size)

        while len(data) < msg_size:
            data += client_socket.recv(4 * 1024) # will receive all frame data from client socket
        frame_data = data[:msg_size] #recover actual frame data
        data = data[msg_size:]
        frame = pickle.loads(frame_data) # de-serialize bytes into actual frame type
        cv2.imshow("Front Camera", frame) # show video frame at client side
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'): # press q to exit video
            break
    