import socket
from client_connection import accept_client_connection
from constants import SERVER_ADDRESS


def main():
    print("# Server is starting #")
    # Starting a TCP socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the SERVER_IP and SERVER_PORT to the server
    server.bind(SERVER_ADDRESS)

    # Server is listening
    server.listen()
    print("# Server is listening #")

    while True:
        accept_client_connection(server)


if __name__ == "__main__":
    main()
