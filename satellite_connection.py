import socket
import os
from constants import DELETE_ID, DEPOSIT_ID, FORMAT, MAX_SATELLITE_INSTANCES, RETRIEVE_ID, SATELLITE_IP, SATELLITE_BASE_PORT, SIZE


def send_file_to_satellites(filename, tolerance_level):
    delete_file_from_satellites(filename)

    send_count = 0
    for i in range(0, int(tolerance_level)):
        server_satellite = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
        port = SATELLITE_BASE_PORT + i
        print(f"# Tentando se conectar à porta {port}... #")
        satellite_address = (SATELLITE_IP, port)
        try:
            server_satellite.connect(satellite_address)

            print("# Sucesso! #")

            file = open(f"{filename}", "rb")
            data = file.read()

            # Sending the operation identifier to the satellite server
            server_satellite.send(DEPOSIT_ID.encode(FORMAT))
            msg = server_satellite.recv(SIZE).decode(FORMAT)
            print(f"# Satellite Server: {msg}")

            # Sending the file name to the satellite server
            server_satellite.send(filename.encode(FORMAT))
            msg = server_satellite.recv(SIZE).decode(FORMAT)
            print(f"# Satellite Server: {msg}")

            # Sending the file data to the satellite server
            server_satellite.send(data)
            msg = server_satellite.recv(SIZE).decode(FORMAT)
            print(f"# Satellite Server: {msg}")

            # Closing the file
            file.close()
            send_count = send_count + 1

        except:
            print("-- Não existem mais servidores satelites disponíveis.")
            print(f"-- Arquivo replicado em apenas {send_count} servidores.")
            server_satellite.close()
            break

        # Closing the connection from the satellite server_satellite
        server_satellite.close()
        
    # Removing the file from the main server, after sending the N copies
    os.remove(filename)

def retrieve_file_from_satellites(filename):
    retrieve_count = 0
    for i in range(0, MAX_SATELLITE_INSTANCES):
        
        server_satellite = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
        port = SATELLITE_BASE_PORT + i
        print(f"# Tentando se conectar à porta {port}... #")
        satellite_address = (SATELLITE_IP, port)

        try:
            server_satellite.connect(satellite_address)

            print("# Sucesso! #")

            # Sending the operation identifier to the satellite server
            server_satellite.send(RETRIEVE_ID.encode(FORMAT))
            msg = server_satellite.recv(SIZE).decode(FORMAT)
            print(f"# Satellite Server: {msg}")

            # Sending the file name to the satellite server
            server_satellite.send(filename.encode(FORMAT))
            msg = server_satellite.recv(SIZE).decode(FORMAT)
            print(f"# Satellite Server: {msg}")

            # Receiving response from satellite
            # OK - File found
            # NOT_FOUND - File not found
            ack = server_satellite.recv(SIZE).decode(FORMAT)
            server_satellite.send("Acknowledgment received".encode(FORMAT))

            if ack == "OK":
                # Receiving file data from the satellite server
                file_data = server_satellite.recv(SIZE)
                server_satellite.send("File data received".encode(FORMAT))
                server_satellite.close()
                return file_data
            else:
                retrieve_count = retrieve_count + 1

        except:
            print(f"# Servidor satélite indisponível na porta {port} #")

        # Closing the connection from the satellite server_satellite
    server_satellite.close()
    return None

def delete_file_from_satellites(filename):
    for i in range(0, int(MAX_SATELLITE_INSTANCES)):

        server_satellite = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
        port = SATELLITE_BASE_PORT + i
        satellite_address = (SATELLITE_IP, port)

        try:
            server_satellite.connect(satellite_address)

            # Sending the operation identifier to the satellite server
            server_satellite.send(DELETE_ID.encode(FORMAT))
            msg = server_satellite.recv(SIZE).decode(FORMAT)
            print(f"# Satellite Server: {msg}")

            # Sending the file name to the satellite server
            server_satellite.send(filename.encode(FORMAT))
            msg = server_satellite.recv(SIZE).decode(FORMAT)
            print(f"# Satellite Server: {msg}")

            #Receiving result of delete operation
            msg = server_satellite.recv(SIZE).decode(FORMAT)
            server_satellite.send("OK".encode(FORMAT))
            print(f"# Satellite Server: {msg}")

        except:
            server_satellite.close()
            break

        # Closing the connection from the satellite server_satellite
        server_satellite.close()
