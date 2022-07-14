import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import winsound

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("The Turtle Crossing")

player = Player()
carmanager = CarManager()
scoreboard = Scoreboard()

winsound.PlaySound("music/slow-trap.wav",winsound.SND_ASYNC)

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.create_car()
    carmanager.car_move()

    for car in carmanager.all_car:
        if car.distance(player) < 22:
            game_is_on=False
            winsound.PlaySound("music/mixkit-sad-game-over.wav",winsound.SND_ASYNC)
            scoreboard.game_over()    

    if player.is_at_finish_line():
        player.go_to_start()
        carmanager.level_up()
        scoreboard.increase_level()
        
screen.exitonclick()
