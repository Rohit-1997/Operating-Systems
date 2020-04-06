'''
    Write a python client program that
        0. connects to localhost and port 10000
        1. send a "Hi <name>" message
        2. waits for the server to send the "READY" message
        3. guess a number and send to the server
        4. wait for the server to send the message
        5. Read the message and make a decision based on the following
            4.1 Close the client if the message is of the form "Correct! <name> took X attempts to guess the secret"
            4.2 Use the clue given by the server and repeat from step 3
'''
import socket

HOST = '127.0.0.1'
PORT = 10002

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    client.sendall(b'Hi')
    ready_message = client.recv(1024)
    if ready_message == b'Ready':
        # We can guess after the server sends a ready message
        counter = 0
        while True:
            # ask the user to guess a number
            number = input("Please enter a number: ")
            if number == "Q":
                break
            client.sendall(number.encode('ascii'))
            received_message = client.recv(1024).decode('ascii')
            if received_message == 'Correct guess':
                print("You have guessed it right")
                print("Your guess count is: ", counter)
                break
            print(received_message)
            counter += 1


