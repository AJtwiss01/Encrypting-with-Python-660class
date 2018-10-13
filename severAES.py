import socket
import hashlib
import os
import sys
import Crypto.Cipher.AES as AES
from Crypto.PublicKey import RSA

#server address and port number input from admin
host = socket.gethostname()
port = 9500 

#setting up socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen(5)


print('WAITING FOR CLIENT TO CONNECT ')


#binding client and address
client,address = server.accept()
print ("CLIENT IS CONNECTED. CLIENT'S ADDRESS ->",address)
print ("\n-----WAITING FOR PUBLIC KEY & PUBLIC KEY HASH-----\n")

#client's message(Public Key)
gettingKlientSecret = client.recv(2048)

#conversion of string to KEY
server_public_key = RSA.importKey(gettingKlientSecret)

#hashing the public key in server side for validating the hash from client
hash_object = hashlib.sha1(gettingKlientSecret)
hex_digest = hash_object.hexdigest()

if gettingKlientSecret != "":
    print (gettingKlientSecret)
    client.send("YES")
    gethash = client.recv(1024)
    print ("\n-----HASH OF PUBLIC KEY----- \n"+gethash)
if hex_digest == gethash:
    # creating session key
    key_128 = os.urandom(16)
    #encrypt CTR MODE session key
    en = AES.new(key_128,AES.MODE_CTR,counter = lambda:key_128)
    encrypto = en.encrypt(key_128)
    #hashing sha1
    en_object = hashlib.sha1(encrypto)
    en_digest = en_object.hexdigest()

    print ("\n-----SESSION KEY-----\n"+en_digest)

    #encrypting session key and public key
    E = server_public_key.encrypt(encrypto,16)
    print ("\n-----ENCRYPTED PUBLIC KEY AND SESSION KEY-----\n"+str(E))
    print ("\n-----HANDSHAKE COMPLETE-----")
    client.send(str(E))
    print(client.recv(1024))
    # while True:
    #     #message from client
    #     newmess = client.recv(1024)
    #     #decoding the message from HEXADECIMAL to decrypt the ecrypted version of the message only
    #     decoded = newmess.decode("hex")
    #     #making en_digest(session_key) as the key
    #     key = en_digest[:16]
    #     print ("\nENCRYPTED MESSAGE FROM CLIENT -> "+newmess)


    # client.close()
else:
    print ("\n-----PUBLIC KEY HASH DOESNOT MATCH-----\n")