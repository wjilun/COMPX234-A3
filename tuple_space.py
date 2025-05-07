import threading

class TupleSpace:
    def __init__(self):
        self.tuples={}
        self.lock = threading.Lock()
        self.number_of_tuples = 0
        self.average_tuples_size = 0
        self.average_key_size=0
        self.average_value_size=0
        self.connet_client_number=0
        self.total_oprations=0
        self.total_GET=0
        self.total_PUT=0
        self.total_READ=0
        self.error_count=0

    def read(self, key):
        with self.lock:
            if key in self.tuples:
                self.total_READ += 1
                self.total_oprations += 1
                return self.tuples[key]
            self.error_count += 1
            return None
        
    def get(self, key):
        with self.lock:
            if key in self.tuples:
                self.total_oprations+=1
                self.total_GET += 1
                return self.tuples.pop(key)
            self.error_count += 1
            return None

    def put(self, key, value):
        with self.lock:
            if key in self.tuples:
                self.error_count += 1
                return 1
            self.tuples[key] = value
            self.total_PUT += 1
            self.total_oprations += 1
            self.number_of_tuples += 1
            return 0
        
    def increment_client(self):
        with self.lock:
            self.connet_client_number += 1

    def decrement_client(self):
        with self.lock:
            self.connet_client_number -= 1

    def get_stats(self):
        with self.lock:
            if self.number_of_tuples > 0:
                self.average_tuples_size = sum(len(k) + len(v) for k, v in self.tuples.items()) / self.number_of_tuples
                self.average_key_size = sum(len(k) for k in self.tuples.keys()) / self.number_of_tuples
                self.average_value_size = sum(len(v) for v in self.tuples.values()) / self.number_of_tuples
            else:
                self.average_tuples_size = 0
                self.average_key_size = 0
                self.average_value_size = 0

            return {
                'number_of_tuples': self.number_of_tuples,
                'average_tuples_size': self.average_tuples_size,
                'average_key_size': self.average_key_size,
                'average_value_size': self.average_value_size,
                'connet_client_number': self.connet_client_number,
                'total_oprations': self.total_oprations,
                'total_GET': self.total_GET,
                'total_PUT': self.total_PUT,
                'total_READ': self.total_READ,
                'error_count':self.error_count
            }        

                   
            
