from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from carmanager import Carmanager
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.title(titlestring="Turtle Cross")
screen.tracer(n=0)

player = Player()
scoreboard = Scoreboard()
cars = Carmanager()


def next_level():
    player.reset_position()
    scoreboard.next_level()
    cars.next_level()


screen.listen()
screen.onkeypress(fun=player.move_player, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.move_cars()

    if player.finish_line():
        next_level()

    if cars.detect_collisions(player):
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()
