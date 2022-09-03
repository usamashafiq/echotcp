# import a library
import socket

# define a server address
hostname = 'localhost'

conn_port = int(input("Enter a port number : "))

# define a function

"""  TCP ECHO Client """
# Create a TCP/IP socket
socket_creation = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the server
Server_Address = (hostname, conn_port)
print("Connecting to %s port %s" % Server_Address)
# connect with ip address
socket_creation.connect(Server_Address)

# Send details
try:
    # Send details
    message = "s rtt  25 100  0 "
    print("Sending %s" % message)
    socket_creation.sendall(message.encode('utf-8'))
    # Look for the response
    size_accept = 0
    # find a length of message
    size_anticipate = len(message)
    print("size of message: " + str(size_anticipate))
    # check to accept message length
    while size_accept < size_anticipate:
        details = socket_creation.recv(15)
        size_accept += len(details)

        print("accept: %s" % details)

except socket.error as E:
    print("Socket error: %s" % str(E))
finally:
    print("The connection to the server is being terminated.")
socket_creation.close()
