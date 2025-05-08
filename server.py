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