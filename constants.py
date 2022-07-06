import socket

SERVER_IP = socket.gethostbyname(socket.gethostname())
SERVER_PORT = 4455
SERVER_ADDRESS = (SERVER_IP, SERVER_PORT)

SATELLITE_IP = socket.gethostbyname(socket.gethostname())
SATELLITE_BASE_PORT = 4456
MAX_SATELLITE_INSTANCES = 5

SIZE = 262144 # 72kb
FORMAT = "utf-8"
# FORMAT = "mbcs"

DEPOSIT_ID = "deposit"
RETRIEVE_ID = "retrieve"
DELETE_ID = "delete"