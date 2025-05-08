import socket
from tuple_space import TupleSpace  
import threading
import time

tuples = TupleSpace()

def print_stats(tuple_space):
    while True:
        stats = tuple_space.get_stats()
        for a,b in stats.items():
              print(f"statistics:")
              print(f"{a}: {b}")
              print("")
        time.sleep(10)

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
                        