import socket
import os
from constants import FORMAT, SATELLITE_IP, SATELLITE_PORT, SIZE, SATELLITE_ADDRESS


def send_file_to_satellites(filename, tolerance_level):
    print("TOLERANCE: ", int(tolerance_level))
    send_count = 0
    for i in range(0, int(tolerance_level)):
        server_satellite = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
        port = SATELLITE_PORT + i
        print("Valor de port:", port)
        satellite_address = (SATELLITE_IP, port)
        try:
            server_satellite.connect(satellite_address)

            file = open(f"{filename}", "r")
            data = file.read()

            """ Sending the filename to the satellite server_satellite. """
            server_satellite.send(filename.encode(FORMAT))
            msg = server_satellite.recv(SIZE).decode(FORMAT)
            print(f"[SERVER]: {msg}")

            """ Sending the file data to the satellite server_satellite. """
            server_satellite.send(data.encode(FORMAT))
            msg = server_satellite.recv(SIZE).decode(FORMAT)
            print(f"[SERVER]: {msg}")

            """ Closing the file. """
            file.close()
            send_count = send_count + 1

        except:
            print("-- Não existem mais servidores satelites disponíveis.")
            print(f"-- Arquivo replicado em apenas {send_count} servidores.")
            server_satellite.close()
            break

        # """ Closing the connection from the satellite server_satellite. """
        server_satellite.close()

    # Removendo arquivo do servidor principal, após ter enviado as N cópias
    os.remove(filename)
