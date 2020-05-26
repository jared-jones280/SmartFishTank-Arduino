import os
import socket
import threading
import pickle
import json

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((socket.gethostname(), 80))
serversocket.listen(5)

# while True:
(clientsocket, address) = serversocket.accept()

data = clientsocket.recv(10240).decode('utf-8')
print(data)

clientsocket.send(json.dumps({'test' : 4}))
    # ct = client_thread(clientsocket)
    # ct.run()
