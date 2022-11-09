import socket
import json


HOST = "127.0.0.1"
PORT = 65432
BUFFER = 2048

data_to_client = {}  # that should be JSON with data for client


class Server:
    def __init__(self, host, port, buffer):
        self.host = host
        self.port = port
        self.buff = buffer

    def server_connection(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            # print("Server started.")
            while True:
                conn, addr = s.accept()
                with conn:
                    # print(f"Connected by {addr}")
                    data = conn.recv(self.buff)
                    # self.message_decode(data)
                    conn.sendall(self.message_encoded(data_to_client))

    # Function to encode and send json
    def message_encoded(self, msg):
        msg_json = json.dumps(msg)
        msg_bytes = msg_json.encode("utf-8")
        return msg_bytes

    # Function to decode server commands
    def message_decode(self, msg_bytes):
        msg_json = msg_bytes.decode("utf-8")
        msg = json.loads(msg_json)
        return msg


def start_server():
    server = Server(HOST, PORT, BUFFER)
    server.server_connection()
 
 
# start_server()