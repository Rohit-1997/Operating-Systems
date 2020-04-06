import socket

# initializing the host and the port values
HOST = "127.0.01"
PORT = 1234

# creating the server socket and binding it
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

while True:
    client_socket, address = server.accept()
    if client_socket is not None:
        print("The connection has been established from", address)
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            client_socket.sendall(data)
        client_socket.close()
server.close()


