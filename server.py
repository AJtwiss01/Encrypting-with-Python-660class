
import socket


def socketServer():
    host = socket.gethostname()
    port = 9500  
    print(host)
    serverSocket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    serverSocket.bind((host, port))  # bind host address and port together
    # configure how many client the server can listen simultaneously
    serverSocket.listen(2)
    conn, address = serverSocket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        print(data)
        if not data:
            # if data is not received break
            break
        if data.lower() == "hello": # turn to lower case 
            print("from connected user: " + str(data))
            myData = 'hi'
            conn.send(myData.encode())  # send data to the client
        else:
            goodbye = "Not 'Hello' then Goodbye"
            conn.send(goodbye.encode())
            conn.close()

    conn.close()  # close the connection

if __name__ == '__main__':
    socketServer()
