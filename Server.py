import socket
import sys
import json

server_address = ('localhost', 10000)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(server_address)
sock.listen()
while True:
    print('waiting for connection')
    connection, client_address = sock.accept()
    try:
        print('client connected: ', client_address)
        jsonReceived =connection.recv(2048)
        print(jsonReceived.decode('utf-8'))
        my_list = json.loads(jsonReceived.decode('utf-8'))
        print(my_list)
        if my_list[0].upper() == "UPLOAD":
            print("upload")
            print(type(my_list[1]))
        else:
            print("Other action")     
    finally:
        connection.close()
