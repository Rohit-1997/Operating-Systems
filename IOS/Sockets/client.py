import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# We will connect to the server
s.connect((socket.gethostname(), 1234))
message = s.recv(1024)
print(message.decode("utf-8"))