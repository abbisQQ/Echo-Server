import socket



def client():

    #Creating the socket passing the ip and port as parameters and trying to connect
    host = "127.0.0.1"
    port = xxxx
    mySocket = socket.socket()
    mySocket.connect((host,port))
    received_message=mySocket.recv(4096).decode()
    print(received_message)
    while(True):
        sending_message = input("Enter you message: ").encode()
        mySocket.send(sending_message)
        print("message send waiting for responce....")
        received_message=mySocket.recv(4096).decode()
        print(received_message)

        
if __name__ == "__main__":
    client()
        
