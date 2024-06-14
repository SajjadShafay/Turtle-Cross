from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(random.choice(COLORS))
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.speed = 5
        self.reset_position()
        self.setheading(180)

    def detect_collision(self, player):
        if self.distance(player) < 20:
            return True

    def reset_position(self):
        self.goto(x=(random.randint(a=290, b=1090)), y=(random.randint(a=-250, b=250)))

    def move(self):
        self.forward(self.speed)
        if self.xcor() < -300:
            self.reset_position()

    def next_level(self):
        self.speed += 5
