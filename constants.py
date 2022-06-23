import socket

CLIENT_IP = socket.gethostbyname(socket.gethostname())
CLIENT_PORT = 4455
CLIENT_ADDRESS = (CLIENT_IP, CLIENT_PORT)

SATELLITE_IP = socket.gethostbyname(socket.gethostname())
SATELLITE_PORT = 4456
SATELLITE_ADDRESS = (SATELLITE_IP, SATELLITE_PORT)

SIZE = 1024
FORMAT = "utf-8"