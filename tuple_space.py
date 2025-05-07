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
