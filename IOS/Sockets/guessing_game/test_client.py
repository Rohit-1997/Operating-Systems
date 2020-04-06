import socket
import sys
import random

# TODO: Set the name variable to your roll number.
name = "Rohit"

if name:

  # Create a TCP/IP socket
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  # Connect the socket to the port where the server is listening
  server_address = ('127.0.0.1', 10002)
  print ('connecting to %s port %s' % server_address)
  sock.connect(server_address)
  print ('Connection to the server meets the specification')

else:
  print ("Fail: To run the test cases set the name variable to your rollnumber")