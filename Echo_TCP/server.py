import socket

hostname = 'localhost'
details_payload = 1000
Back_Log = 2

conn_port = int(input("Enter a port number :"))

""" TCP ECHO SERVER """
# first Create a TCP socket
sock_creation = socket.socket(socket.AF_INET,
                              socket.SOCK_STREAM)
# Now Enable reuse address/port
sock_creation.setsockopt(socket.SOL_SOCKET,
                         socket.SO_REUSEADDR, 1)
# Now Bind the socket to the port
Server_Address = (hostname, conn_port)
print("Starting up TCP ECHO server on %s port % s" % Server_Address)
sock_creation.bind(Server_Address)
# Listen to clients, backlog argument specifies the max no. of queued connections
sock_creation.listen(Back_Log)
while True:
    print("Waiting to receive message from client ")
    Client, Address = sock_creation.accept()
    Client_details = Client.recv(details_payload)
    if Client_details:
        print("details: %s" % Client_details)
    Client.send(Client_details)
    print("sent %s Bytes Back to % s " % (Client_details, Address))
    # end connection
    Client.close()
