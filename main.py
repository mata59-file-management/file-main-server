import socket
import os
from client_connection import receive_file_from_client
from satellite_connection import send_file_to_satellites
from constants import CLIENT_ADDRESS, SATELLITE_ADDRESS, SIZE, FORMAT


def main():
    print("[STARTING] Server is starting.")
    """ Staring a TCP socket. """
    server_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """ Bind the CLIENT_IP and CLIENT_PORT to the server_client. """
    server_client.bind(CLIENT_ADDRESS)

    """ Server is listening, i.e., server_client is now waiting for the client to connected. """
    server_client.listen()
    print("[LISTENING] Server is listening.")

    while True:
        filename, tolerance_level, conn, addr = receive_file_from_client(
            server_client)
        if filename:
            # A partir deste ponto começaremos a enviar o arquivo para os N servidores satelites """
            send_file_to_satellites(filename, tolerance_level)

        else:
            print("Arquivo inválido enviado pelo cliente!")

        """ Closing the connection from the client. """
        conn.close()
        print(f"[DISCONNECTED] {addr} disconnected.")
        print("[LISTENING] Server is listening again.")


if __name__ == "__main__":
    main()
