import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))            # here we are binding the server socket to the local machince
s.listen(5)                                     # We will limit the size of the listening queue to 5

while True:
    # If we get a connection
    client_socket, address = s.accept()
    print(f"Connection from {address} has been established!")
    # sending info to the client socket
    client_socket.send(bytes("Hey there, howdy?", "utf-8"))