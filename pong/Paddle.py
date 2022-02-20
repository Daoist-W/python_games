import turtle


class Paddle(turtle.Turtle):
    lives = 3
    velocity = 0.25

    def __init__(self, position):
        super(Paddle, self).__init__()
        self.shape("square")
        self.speed(0)
        self.shapesize(stretch_wid=5, stretch_len=1)  # width is vertical, length horizontal
        self.color("white")
        self.penup()
        self.goto(position)



    def paddle_up(self):
        y = self.ycor()  # need to know y coordinate
        y += 20
        self.sety(y)

    def paddle_down(self):
        y = self.ycor()  # need to know y coordinate
        y -= 20
        self.sety(y)

    def auto_track(self, pong: turtle.Turtle):
        # automated tracking
        if pong.xcor() < 0 and self.xcor() < 0:
            if self.ycor() > pong.ycor():
                self.sety(self.ycor() - self.velocity)
            else:
                self.sety(self.ycor() + self.velocity)

        if pong.xcor() > 0 and self.xcor() > 0:
            if self.ycor() > pong.ycor():
                self.sety(self.ycor() - self.velocity)
            else:
                self.sety(self.ycor() + self.velocity)

