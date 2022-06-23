import socket, os
from constants import FORMAT, SIZE, SATELLITE_ADDRESS

def send_file_to_satellites(filename, tolerance_level):
    server_satellite = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
    server_satellite.connect(SATELLITE_ADDRESS)

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

    """ Sending the fault tolerance level to the satellite server_satellite. """
    server_satellite.send(tolerance_level.encode(FORMAT))
    msg = server_satellite.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")

    """ Closing the file. """
    file.close()

    """ Closing the connection from the satellite server_satellite. """
    server_satellite.close()

    # Removendo arquivo do servidor principal, após ter enviado as N cópias
    os.remove(filename)
