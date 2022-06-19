
import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDRESS = (IP, PORT)

SIZE = 1024
FORMAT = "utf-8"


def main():
    print("[STARTING] Server is starting.")
    """ Staring a TCP socket. """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """ Bind the IP and PORT to the server. """
    server.bind(ADDRESS)

    """ Server is listening, i.e., server is now waiting for the client to connected. """
    server.listen()
    print("[LISTENING] Server is listening.")

    while True:
        """ Server has accepted the connection from the client. """
        conn, addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected.")

        """ Receiving the filename from the client. """
        filename = conn.recv(SIZE).decode(FORMAT)
        print(f"[RECV] Receiving the filename: {filename}")

        if filename:
            file = open(filename, "w")
            conn.send("Filename received.".encode(FORMAT))

            """ Receiving the file data from the client. """
            data = conn.recv(SIZE).decode(FORMAT)
            print(f"[RECV] Receiving the file data.")
            file.write(data)
            conn.send("File data received".encode(FORMAT))

            """ Closing the file. """
            file.close()

            """ Receiving the fault tolerance level for the file """
            tolerance_level = conn.recv(SIZE).decode(FORMAT)
            print(
                f"[RECV] Receiving the fault tolerance level ({tolerance_level}).")
            # print(f"FAULT TOLERANCE: {tolerance_level}")
            conn.send(
                f"Fault tolerance level received ({tolerance_level}).".encode(FORMAT))

            """ In here we'll send the file to N sattelite servers """

        else:
            print("Arquivo inválido enviado pelo cliente!")

        """ Closing the connection from the client. """
        conn.close()
        print(f"[DISCONNECTED] {addr} disconnected.")
        print("[LISTENING] Server is listening again.")


if __name__ == "__main__":
    main()
