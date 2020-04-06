Socket:
    It's an API Through which we can acheive Inter process communication
Generally we have a client server model.
A Socket takes in two things
1 - The IP Adress / The local host address
2 - The port
In the server section we bind the socket with this address and port number
Now in the client section we connect to the servers socket by providing the host address
and the port number on which the server socket has been built.

The Buffer size:
Generally when we receive a response from the server we are going to provide a buffer size in the client
to file. So if the response is within that buffer size things are expected to work fine but what happens
when the response is more than buffer size? 

-- To solve this problem we use the concept of headers in which the server will inform the client about
how big the response is going to be. So the client waits until it receives that size then completes it's task.