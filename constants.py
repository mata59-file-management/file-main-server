import socket

SERVER_IP = socket.gethostbyname(socket.gethostname())
SERVER_PORT = 4455
SERVER_ADDRESS = (SERVER_IP, SERVER_PORT)

SATELLITE_IP = socket.gethostbyname(socket.gethostname())
SATELLITE_PORT = 4456
SATELLITE_ADDRESS = (SATELLITE_IP, SATELLITE_PORT)

SIZE = 1024
FORMAT = "utf-8"

DEPOSIT_ID = "deposit"
RETRIEVE_ID = "retrieve"