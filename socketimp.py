"""http://joaoventura.net/blog/2017/python-webserver/"""



import socket

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000

#create a socket instance
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#socket.AF_INET is address family ipv4
#socket.STREAM means the connection oriented TCP protocol.
#familar with cmd : ping www.google.ca ? we can do it in python:
##ip = socket.gethostbyname('www.google.ca')
##print(ip)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
#bind server with specified ip and port
server_socket.listen(1)
#only listen to one connection, reject further connection
print('Listening on port %s ...' % SERVER_PORT)

while True:
    # Wait for client connections
    client_connection, client_address = server_socket.accept()
#accept method will initiate a connection with the client.
    # Get the client request
    request = client_connection.recv(1024).decode()
    print(request)

    # Send HTTP response
    response = 'HTTP/1.0 200 OK\n\nHello World'
    client_connection.sendall(response.encode())
    client_connection.close()
#close method will closes the connection with the client

# Close socket
server_socket.close()
