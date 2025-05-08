import socket
import re

class User:
    def __init__(self):
        pass

    def encode_request(self, cmd, key, value=None):
        if cmd == 'PUT':
            payload = f"P{key} {value}"
            return f"{len(payload) + 6:03d}{payload}"
        elif cmd == 'GET':
            payload = f"G{key}"
            return f"{len(payload) + 6:03d}{payload}"
        elif cmd == 'READ':
            payload = f"R{key}"
            return f"{len(payload) + 7:03d}{payload}"
        else:
            raise ValueError("Invalid command")

    def handle_client_file(self, filename, server_address):
        with open(filename, 'r') as file:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(server_address)    



     