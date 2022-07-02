from constants import DEPOSIT_ID, RETRIEVE_ID, SIZE, FORMAT
from satellite_connection import send_file_to_satellites

def accept_client_connection(server):
    conn, addr = server.accept()
    print(f"# {addr} connected #")

    # Receive operation identifier (retrieve or withdraw)
    operation_id = conn.recv(SIZE).decode(FORMAT)
    print(f"# Receiving the operation id {operation_id} #")
    conn.send("# Operation id received #".encode(FORMAT))

    if operation_id == DEPOSIT_ID:
        handle_deposit(conn)
    elif operation_id == RETRIEVE_ID:
        print("em construção...")

    # Closing the connection with the client
    conn.close()
    print(f"# {addr} disconnected #")
    print("# Server is listening again #")

def handle_deposit(conn):
    filename, tolerance_level = receive_file_from_client(
            conn)
    if filename:
        # Enviar o arquivo para os N servidores satelites """
        send_file_to_satellites(filename, tolerance_level)

    else:
        print("# Arquivo inválido enviado pelo cliente! #")

def handle_retrieve(conn):
    # A FAZER
    # filename = receive_file_name_from_client(conn)
    return

def receive_file_from_client(conn):
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
    return filename, tolerance_level
