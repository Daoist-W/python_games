import random
import turtle
import winsound

window = turtle.Screen()
window.title("My first Python game!")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# scores
point_a = 3
point_b = 3
paddle_a_points = turtle.Turtle()
paddle_a_points.speed(0)
paddle_a_points.color('white')
paddle_a_points.penup()
paddle_a_points.hideturtle()
paddle_a_points.goto(0, 260)
style = ('Courier', 20, 'normal')
paddle_a_points.write("Player A: {} VS Player B: {}".format(point_a, point_b), font=style, align="center")

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # speed of animation, 0 sets is to the max possible refresh speed
paddle_a.shape("square")  # 20px 20px default
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # width is vertical, length horizontal
paddle_a.color("white")
paddle_a.penup()  # stops trailing animation (like drawing with a pen)
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)  # speed of animation, 0 sets is to the max possible refresh speed
paddle_b.shape("square")  # 20px 20px default
paddle_b.shapesize(stretch_wid=5, stretch_len=1)  # width is vertical, length horizontal
paddle_b.color("white")
paddle_b.penup()  # stops trailing animation (like drawing with a pen)
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)  # speed of animation, 0 sets is to the max possible refresh speed
ball.shape("square")  # 20px 20px default
ball.shapesize(stretch_wid=1, stretch_len=1)  # width is vertical, length horizontal
ball.color("white")
ball.penup()  # stops trailing animation (like drawing with a pen)
ball.goto(0, 0)

sign_x = [-1, 1][random.randrange(2)]
sign_y = [-1, 1][random.randrange(2)]
ball.dx = 0.2 * sign_x
ball.dy = 0.2 * sign_y


## Functions ##

def paddle_a_up():
    y = paddle_a.ycor()  # need to know y coordinate
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()  # need to know y coordinate
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()  # need to know y coordinate
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()  # need to know y coordinate
    y -= 20
    paddle_b.sety(y)


def is_touchingA(paddle: turtle.Turtle, x, y) -> bool:
    if paddle.xcor() < x < paddle.xcor() + 20:
        if paddle.ycor() + 40 > y > paddle.ycor() - 40:
            return True
    return False


def is_touchingB(paddle: turtle.Turtle, x, y) -> bool:
    if paddle.xcor() - 20 < x < paddle.xcor():
        if paddle.ycor() + 40 > y > paddle.ycor() - 40:
            return True
    return False


## Bindings ##
window.listen()
window.onkeypress(paddle_b_up, "8")
window.onkeypress(paddle_b_down, "5")
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")

# Main game loop
while True:
    window.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    score_a = "A: {}".format(point_a)
    score_b = "B: {}".format(point_b)

    # Border checking
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1
        winsound.PlaySound("../sounds/boing3.wav", winsound.SND_ASYNC)

    if ball.xcor() > 400:
        ball.setx(0)
        ball.sety(0)
        ball.dx *= -1
        point_a -= 1
        paddle_a_points.clear()
        paddle_a_points.write("Player A: {} VS Player B: {}".format(point_a, point_b), font=style, align="center")

    if ball.xcor() < -400:
        ball.setx(0)
        ball.sety(0)
        ball.dx *= -1
        point_b -= 1
        paddle_a_points.clear()
        paddle_a_points.write("Player A: {} VS Player B: {}".format(point_a, point_b), font=style, align="center")

    # paddle and ball collisions

    if is_touchingA(paddle_a, ball.xcor(), ball.ycor()):
        ball.dx *= -1
        winsound.PlaySound("../sounds/bounce.wav", winsound.SND_ASYNC)

    if is_touchingB(paddle_b, ball.xcor(), ball.ycor()):
        ball.dx *= -1
        winsound.PlaySound("../sounds/bounce.wav", winsound.SND_ASYNC)

    # automated tracking
    if ball.xcor() < 0:
        paddle_a.sety(ball.ycor())

    if ball.xcor() > 0:
        paddle_b.sety(ball.ycor())

    if point_a <= 0 or point_b <= 0:
        break
