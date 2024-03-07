import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = " 137.74.187.103"
port = 443

def portscanner(port):
    if s.connect_ex((host,port)): # the connect_ex is meant to handle exceptions if there are exception in the output
        print("the port is closed")
    else:
        print("the port is open")

portscanner(port)
