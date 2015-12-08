# server.py 
import socket                                         
import pickle

devID = 1

# create a socket object
serversocket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = 9999                                           

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests
serversocket.listen(2)

clients = {}
positions = {}
while devID <= 2:
    # establish a connection
    clients[devID],addr = serversocket.accept()      
    print("Got a connection from %s" % str(addr))
    clients[devID].send(str(devID).encode('ascii'))
    devID += 1

while True:
    for key, value in clients.items():
        data = pickle.loads(value.recv(1024))
        positions[key] = data
        value.send(pickle.dumps(positions))