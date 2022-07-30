# socket import
# Course work by Ekaka Emmanuel 19/ITD/2926/PD
import socket
from func import sendDistortedMessage, reArrageMessage

HOST = '127.0.0.1'
PORT = 5555
print('Initializing Client')
# Ensuring connection to the server
with  socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Server details
    server = (HOST, PORT)
    # Establishing connection to the server
    s.connect(server)
    while True:
        # input information to send
        sent = input("Enter Text File>>")
        sent = sendDistortedMessage(sent).encode()
        s.sendall(sent)
        # Waiting to receive information
        data = s.recv(1024)
        print(f'Distorted Recieved: {data.decode()}')
        refined = reArrageMessage(data.decode())
        print(f'Refined: {refined}')
