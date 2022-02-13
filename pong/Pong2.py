import time
import turtle
from Paddle import Paddle
from Ball import Ball
from ScoreBoard import ScoreBoard
import winsound

if __name__ == '__main__':
    # user input expected
    mode = input("Select Mode (0P, 1P, 2P): ")

    # window configuration
    window = turtle.Screen()
    window.title("My first Python game!")
    window.bgcolor("black")
    window.setup(width=800, height=600)
    window.tracer(0)

    # objects
    paddle_right = Paddle((350, 0))
    paddle_left = Paddle((-350, 0))
    score = ScoreBoard()
    pong = Ball()

    ## Bindings ##
    window.listen()
    window.onkeypress(paddle_right.paddle_up, "8")
    window.onkeypress(paddle_right.paddle_down, "5")
    window.onkeypress(paddle_left.paddle_up, "w")
    window.onkeypress(paddle_left.paddle_down, "s")

    # Main game loop
    while True:
        window.update()

        # move the ball
        pong.setx(pong.xcor() + pong.dx)
        pong.sety(pong.ycor() + pong.dy)

        # Border checking
        if pong.ycor() > 290 or pong.ycor() < -280:
            pong.dy *= -1
            winsound.PlaySound("../sounds/boing3.wav", winsound.SND_ASYNC)

        if pong.xcor() > 400:
            pong.setx(0)
            pong.sety(0)
            pong.dx *= -1
            score.player_A_lives -= 1
            score.clear()
            score.update()

        if pong.xcor() < -400:
            pong.setx(0)
            pong.sety(0)
            pong.dx *= -1
            score.player_B_lives -= 1
            score.clear()
            score.update()

        # paddle and ball collisions
        if pong.is_touching_a(paddle_left):
            pong.dx *= -1
            pong.setx(pong.xcor() + 5)
            winsound.PlaySound("../sounds/bounce.wav", winsound.SND_ASYNC)

        if pong.is_touching_b(paddle_right):
            pong.dx *= -1
            pong.setx(pong.xcor() - 5)
            winsound.PlaySound("../sounds/bounce.wav", winsound.SND_ASYNC)

        # automated tracking
        if mode.upper() == "1P":
            paddle_right.auto_track(pong)
        elif mode.upper() == "0P":
            paddle_left.auto_track(pong)
            paddle_right.auto_track(pong)

        if score.player_A_lives <= 0 or score.player_B_lives <= 0:
            break
