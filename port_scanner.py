import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = " 137.74.187.103" # this is the ip address of a site called hackthissite.org 
port = 443 # you can try different ports to know which one is open or not

def portscanner(port):
    if s.connect_ex((host,port)): # the connect_ex is meant to handle exceptions if s.connect() throws an error in the output
        print("the port is closed")
    else:
        print("the port is open")

portscanner(port)
