import socket
print("Host Name ", socket.gethostname())
print("IP Address(Internal) : ", socket.gethostbyname(socket.gethostname()))