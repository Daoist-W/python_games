import turtle
import random


class Ball(turtle.Turtle):
    sign_x = [-1, 1][random.randrange(2)]
    sign_y = [-1, 1][random.randrange(2)]
    dx = 0.4 * sign_x
    dy = 0.4 * sign_y

    def __init__(self):
        super(Ball, self).__init__()
        self.shape("square")
        self.speed(0)
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(0, 0)

    def is_touching_b(self, paddle: turtle.Turtle) -> bool:
        if paddle.xcor() - 20 < self.xcor() < paddle.xcor():
            if paddle.ycor() + 50 > self.ycor() > paddle.ycor() - 50:
                return True
        return False

    def is_touching_a(self, paddle: turtle.Turtle) -> bool:
        if paddle.xcor() < self.xcor() < paddle.xcor() + 20:
            if paddle.ycor() + 50 > self.ycor() > paddle.ycor() - 50:
                return True
        return False

    def border_control(self):
        if self.ycor() > 290 or self.ycor() < -280:
            self.dy *= -1
            return "top-bottom"
        elif self.xcor() > 400:  # if the ball crosses the right border, return "right"
            self.setx(0)
            self.sety(0)
            self.dx *= -1
            return "right"

        elif self.xcor() < -400:  # if the ball crosses the left border, return "left"
            self.setx(0)
            self.sety(0)
            self.dx *= -1
            return "left"
