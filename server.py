import socket
import json

import time
from turtle import Screen, Turtle
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball

# ---------------------------------------------------------------------------------------------
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen()
#     conn, addr = s.accept()
#     with conn:
#         print(f"Connected by {addr}")
#         while True:
#             data = conn.recv(2048)
#             if not data:
#                 break
#             conn.sendall(data)


def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    print(f"Connected by {addr}")
    data = conn.recv(2048)
    conn.sendall(data)


# data_to_client = {"dane": "cos tam wysyla"}  # that should be JSON with data for client
#

#     # Function to encode and send json
#     def message_encoded(self, msg):
#         msg_json = json.dumps(msg)
#         msg_bytes = msg_json.encode("utf-8")
#         return msg_bytes
#
#     # Function to decode server commands
#     def message_decode(self, msg_bytes):
#         msg_json = msg_bytes.decode("utf-8")
#         msg = json.loads(msg_json)
#         return msg
#

# ---------------------------------------------------------------------------------------------

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball((0, 0))
scoreboard = Scoreboard()
screen.update()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")



while True:
    start_server()
    screen.update()
    ball.move()
    time.sleep(0.01)
    
    # Detect wall collision
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.y_bounce()
    
    # Detect r_paddle collision
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340:
        ball.x_bounce()
    
    # Detect l_paddle collision
    if ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.x_bounce()
    
    # Detect right miss
    if ball.xcor() > 390:
        time.sleep(0.5)
        ball.new_angle("right")
        ball.ball_speed = 4
        scoreboard.l_point()
    
    if ball.xcor() < -390:
        time.sleep(0.5)
        ball.new_angle("left")
        ball.ball_speed = 4
        scoreboard.r_point()
    
screen.exitonclick()


