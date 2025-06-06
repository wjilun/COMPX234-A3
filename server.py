import socket
from tuple_space import TupleSpace  
import threading
import time

tuples = TupleSpace()

def print_stats(tuple_space):
    while True:
        time.sleep(10)
        stats = tuple_space.get_stats()
        print(f"statistics:")
        for a,b in stats.items():
              print(f"{a}: {b}")
              print("")
        

def handle_client(conn, addr, tuple_space):
    print(f"Connected by {addr}")
    tuple_space.increment_client()
    try:
         while True:
            data = conn.recv(1024)
            if not data:
                break
            data_str = data.decode('utf-8')
            length_prefix = data_str[:3]
            try:
                length = int(length_prefix)
                cmd = data_str[3]
                key_end_idx = data_str.find(' ', 4)
                if key_end_idx == -1:
                    key = data_str[4:]
                else:
                    key=data_str[4:key_end_idx]
                if cmd=="P":
                    value = data_str[key_end_idx + 1:].strip()
                else:
                    value = None    
                if len(key) > 999 or (value and len(value) > 999):
                    response = "ERR key or value too long"
                    tuple_space.error_count += 1
                elif cmd == 'P' and len(f"{key} {value}") > 970:
                    response = "ERR key and value combined too long"
                    tuple_space.error_count += 1
                else:
                    if cmd == 'G':
                        result = tuple_space.get(key)
                        if result:
                            response = f"OK ({key},{result}) removed"
                        else:
                            response = f"ERR {key} does not exist"
                    elif cmd == 'P':
                        if not value:
                            response = "ERR missing value"
                            tuple_space.error_count += 1
                        else:
                            result = tuple_space.put(key, value)
                            if result == 0:
                                response = f"OK ({key},{value}) added"
                            else:
                                response = f"ERR {key} already exists"
                    elif cmd == 'R':
                        result = tuple_space.read(key)
                        if result:
                            response = f"OK ({key},{result}) read"
                        else:
                            response = f"ERR {key} does not exist"
                    else:
                        response = "ERR invalid command"
                        tuple_space.error_count += 1
                response = f"{len(response):03d}{response}"
                conn.sendall(response.encode('utf-8'))
            except ConnectionError:
                print(f"Connection error with {addr}")
                break
    except Exception as e:
        print(f"Error handling client {addr}: {e}")
    finally:
        conn.close()
        tuple_space.decrement_client()
        print(f"Connection closed by {addr}")

def main():
    hostname = str(input("please input hostname(such as localhost): "))
    port = int(input("please input port(This has to be a high port, such as 51234 (50000 <= port <= 59999)): "))
    if port < 50000 or port > 59999:
        raise ValueError("Port must be between 50000 and 59999")
    else:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (hostname, port) 
        server_socket.bind(server_address)
        server_socket.listen(5)
        print_stats_thread=threading.Thread(target=print_stats, args=(tuples,))
        print_stats_thread.start()
        print(f"Server is listening on {server_address}")
        while True:
            conn, addr = server_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(conn, addr, tuples))
            client_thread.start()
        
    
if __name__ == "__main__":
    main()
                        