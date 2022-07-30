# socket import
# Course work by Ekaka Emmanuel 19/ITD/2926/PD
import socket
from func import sendDistortedMessage, reArrageMessage
# Host Ip address and port number to share resources
HOST = '127.0.0.1'
PORT = 5555
print('Initializing Server')
# Ensuring connection of server to socket
with  socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    server = (HOST, PORT)
    s.bind(server)
    # Listening for any connection
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f'Connected to {addr}')
        while True:
            # Waiting to receive information
            data = conn.recv(1024)
            if not data:
                print('Disconnected')
                break
              
            print(f'Distorted: {data.decode()}')
            refined = reArrageMessage(data.decode())
            print(f'Refined: {refined}')
            # Feed Back
            sent = input("Enter Text File>>")
            try:
                sent = sendDistortedMessage(sent).encode()
                conn.sendall(sent)
            except ConnectionResetError as e:
                break