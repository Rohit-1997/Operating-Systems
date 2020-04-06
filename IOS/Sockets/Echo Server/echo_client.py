import socket

# initializing the host and the port values
HOST = "127.0.01"
PORT = 1234

# creating the client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connecting to the host
client.connect((HOST, PORT))
client.sendall(b'Hey there, Howdy?')
client.sendall(b'Great, How you doing?')
client.sendall(b'')
data = client.recv(1024)
print("Received, ", repr(data))
client.close()



# Creating another client
client_two = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connecting to the host
client_two.connect((HOST, PORT))
client_two.sendall(None)

    
