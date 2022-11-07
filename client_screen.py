import socket
import json
import time
from turtle import Screen
from paddle import Paddle
from ball import Ball


# Function to encode and send json
def send_encoded(msg):
    msg_json = json.dumps(msg)
    msg_bytes = msg_json.encode("utf-8")
    s.sendall(msg_bytes)


# Function to decode server commands
def message_decode(msg_bytes):
    msg_json = msg_bytes.decode("utf-8")
    msg = json.loads(msg_json)
    return msg

HOST = "127.0.0.1"  # To change later, maybe input to ask for host ip address
PORT = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

connection_up = True
data = s.recv(2048)

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

first_message = message_decode(data)
opponent_paddle_pos = first_message.get("other_paddle_pos")
opponent_paddle = Paddle(opponent_paddle_pos)
your_paddle = Paddle((350, 0))  # Changed to constant start position
screen.update()

while connection_up:
    if not data:
        print("Connection failure")
        connection_up = False

# Example data structure we want to receive from the server:
# {"connection": "up/down",
#  "ball_pos": (x, y) /tuple/,
#  "left_paddle": (x, y) /tuple/,
#  "score": (x, y) /left, right/}

    incoming = message_decode(data)
    opponent_paddle_pos = incoming.get("left_paddle")
    ball_pos = incoming.get("ball_pos")
    connection = incoming.get("connection")
    ball = Ball(ball_pos)
    screen.listen()
    screen.onkey(your_paddle.go_up, "Up")
    screen.onkey(your_paddle.go_down, "Down")
    screen.update()
    time.sleep(0.01)
    paddle_pos = your_paddle.pos()
    # Sending your paddle pos to the server
    # Example data structure we want to send to the server:
    # {"paddle_pos": (x, y) /tuple/}
    command = {"paddle_pos": paddle_pos}
    send_encoded(command)

    screen.exitonclick()
