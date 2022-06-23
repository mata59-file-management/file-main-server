from constants import SIZE, FORMAT

def receive_file_from_client(server_client):
    conn, addr = server_client.accept()
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
    return filename, tolerance_level, conn, addr
