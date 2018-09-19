
import socket


def client():
    host = socket.gethostname()  # as both code is running on same pc
    port = 9500  # socket server port number

    clientSocket = socket.socket()  # instantiate
    clientSocket.connect((host, port))  # connect to the server
    message = input("Type Hello :  ")  # take input
    clientSocket.send(message.encode())   # send message
    while message.lower() == 'hello': #turn to lower case 
        print(clientSocket.recv(1024).decode())  # show in terminal
        message = input("Send another message: ")  # again take input
        clientSocket.send(message.encode())   # send message
    print(clientSocket.recv(1024).decode())  # show in terminal
    clientSocket.close()  # close the connection


if __name__ == '__main__':
    client()
