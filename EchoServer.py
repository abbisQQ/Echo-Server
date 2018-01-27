import socket

def server():
    host = "0.0.0.0" #listen at all interfaces
    port = 4444
    
    mySocket = socket.socket()
    mySocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
    mySocket.bind((host,port))

    mySocket.listen(1)#only 1 client can connect
    print("Listening for incoming connections")
    conn,addr = mySocket.accept()


    print('Connection from: {}'.format(addr))

    sending_message = "welcome"

    while sending_message!= 'quit':
        conn.send(sending_message.encode())
        received_message = conn.recv(4096).decode()
        print(received_message)
        sending_message = received_message
       
    conn.close()
    print("Server shut down...")


  
if __name__ == "__main__":
    while True:
        try:
            server()
        except:
            print("Stop serving")
