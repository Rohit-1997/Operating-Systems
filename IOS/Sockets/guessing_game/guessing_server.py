'''
    Write a python server program that
        0. initialized a socket connection on localhost and port 10000
        1. accepts a connection from a  client
        2. receives a "Hi <name>" message from the client
        3. generates a random numbers and keeps it a secret
        4. sends a message "READY" to the client
        5. waits for the client to send a guess
        6. checks if the number is
            6.1 equal to the secret then it should send a message "Correct! <name> took X attempts to guess the secret"
            6.2 send a message "HIGH" if the guess is greater than the secret
            6.3 send a message "LOW" if the guess is lower than the secrent
        7. closes the client connection and waits for the next one
'''
import socket
from random import randint

HOST = '127.0.0.1'
PORT = 10002


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    client_socket, address = server.accept()
    with client_socket:
        print("Connection established from ", address)
        data = client_socket.recv(1024)
        client_socket.sendall(b'READY')                         # sending the ready message to the client
        actual_number = randint(1,100)                           # Generating the random number
        print(actual_number)
        while True:
            client_guess = client_socket.recv(1024)                 # receving the guessed number
            if not client_guess:
                break
            guessed = client_guess.decode()
            guessed_number = int(guessed)
            if guessed_number > actual_number:
                client_socket.sendall(b'HIGH')
            elif guessed_number < actual_number:
                client_socket.sendall(b'LOW')
            else:
                client_socket.sendall(b'Correct! guess')

            

            
