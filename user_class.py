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
            for line in file:
                message = line.strip()
                parts = message.split()
                if len(parts) < 2:
                   print(f"Error: Invalid request format: {line}")
                   continue
                cmd = parts[0]
                key = parts[1]
                if(len(parts) > 2):
                    value = parts[2]
                else:
                    value = None
                if cmd not in ['READ', 'GET', 'PUT']:
                    print(f"Error: Invalid request format: {line}")
                    continue               
                if len(key) > 999 or (value and len(value) > 999):
                    print(f"Error: Key or value too long: {message}")
                    continue
                if value and len(f"{key} {value}") > 970:
                    print(f"Error: Key and value combined too long: {message}")
                    continue
                request = self.encode_request(cmd, key, value)
                client_socket.send(request.encode('utf-8'))
                response = client_socket.recv(1024).decode('utf-8')
                print(f"{message}: {response[3:]}")

    def read_one_client_file(self):
        print("which file do you want to read?please input the number")
        number = int(input())
        hostname = str(input("please input hostname(such as localhost): "))
        port = int(input("Enter the port(This has to be a high port, such as 51234 (50000 <= port <= 59999)): "))
        filename1 = f"client_{number}"
        filename = rf"d:\文件夹\test-workload\test-workload\{filename1}.txt"
        server_address = (hostname, port)
        self.handle_client_file(filename, server_address)

    def read_mutiple_client_files(self):
        hostname = str(input("please input hostname(such as localhost): "))
        port = int(input("Enter the port(This has to be a high port, such as 51234 (50000 <= port <= 59999)): "))
        print("how many files(start from client_1) do you want to read?")
        number = int(input())
        for i in range(1, number + 1):
            filename1 = f"client_{i}"
            filename = rf"d:\文件夹\test-workload\test-workload\{filename1}.txt"
            server_address = (hostname, port)
            self.handle_client_file(filename, server_address)                


                    



     