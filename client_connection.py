from constants import DEPOSIT_ID, RETRIEVE_ID, SIZE, FORMAT
from satellite_connection import retrieve_file_from_satellites, send_file_to_satellites


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
        handle_retrieve(conn)

    # Closing the connection with the client
    conn.close()
    print(f"# {addr} disconnected #")
    print("# Server is listening again #")


def handle_deposit(conn):
    """ Receiving the filename from the client. """
    filename = conn.recv(SIZE).decode(FORMAT)
    print(f"# Receiving the filename: {filename} #")

    file = open(filename, "wb")
    conn.send("Filename received.".encode(FORMAT))

    """ Receiving the file data from the client. """
    data = conn.recv(SIZE)
    print(f"# Receiving the file data #")
    file.write(data)
    conn.send("File data received".encode(FORMAT))

    # Closing the file
    file.close()

    # Receiving the fault tolerance level for the file
    tolerance_level = conn.recv(SIZE).decode(FORMAT)
    print(
        f"[RECV] Receiving the fault tolerance level ({tolerance_level}).")
    conn.send(
        f"Fault tolerance level received ({tolerance_level}).".encode(FORMAT))

    # Enviar o arquivo para os N servidores satelites
    send_file_to_satellites(filename, tolerance_level)


def handle_retrieve(client_conn):

    print("# Retrieve operation began... #")

    # Recebe o nome do arquivo do cliente
    filename = client_conn.recv(SIZE).decode(FORMAT)
    print(f"# Receiving the filename: {filename} #")
    client_conn.send("Filename received".encode(FORMAT))

    # Procura o arquivo em no máximo <MAX_SATELLITE_INSTANCES> servidores satelites
    # Caso não ache em nenhum deles, retorna uma string vazia
    file_data = retrieve_file_from_satellites(filename)
    
    # Envia de volta pro cliente os dados do arquivo
    # Caso não tenha encontrado, envia uma string vazia
    if file_data:
        client_conn.send("OK".encode(FORMAT))
        msg = client_conn.recv(SIZE).decode(FORMAT)
        print(f"# Client: {msg}#")

        client_conn.send(file_data)
        msg = client_conn.recv(SIZE).decode(FORMAT)
        print(f"# Client: {msg}#")


        
