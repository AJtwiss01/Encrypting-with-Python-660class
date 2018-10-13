import socket
import hashlib
import sys
from Crypto import Random
from Crypto.PublicKey import RSA

#animating loading

#public key and private key
random_generator = Random.new().read
key = RSA.generate(1024,random_generator)
public = key.publickey().exportKey()
private = key.exportKey()

#hashing the public key
hash_object = hashlib.sha1(public)
hex_digest = hash_object.hexdigest()

#Setting up socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#host and port input user
host = socket.gethostname()
port = 9500 
#binding the address and port
server.connect((host, port))
# printing "Server Started Message"



def send(name,key):
    mess = raw_input(name + " : ")
    key = key[:16]
    #merging the message and the name
    whole = name+" : "+mess




server.send(public)
confirm = server.recv(1024)
if confirm == "YES":
    
    server.send(hex_digest)

#connected msg
msg = server.recv(1024)
en = eval(msg)
decrypt = key.decrypt(en)
# hashing sha1
en_object = hashlib.sha1(decrypt)
en_digest = en_object.hexdigest()

print ("\n-----ENCRYPTED PUBLIC KEY AND SESSION KEY FROM SERVER-----")
print (msg)
print ("\n-----DECRYPTED SESSION KEY-----")
print (en_digest)
print ("\n-----HANDSHAKE COMPLETE-----\n")
server.close()