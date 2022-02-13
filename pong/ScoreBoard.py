from turtle import Turtle


class ScoreBoard(Turtle):
    player_A_lives = 3
    player_B_lives = 3
    style = ('Courier', 20, 'normal')

    def __init__(self):
        super().__init__()
        self.speed(0)
        self.color("green")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.write(
            "Player 1: {} VS Player 2: {}".format(self.player_A_lives, self.player_B_lives),
            font=self.style,
            align="center"
        )

    def update(self):
        self.write(
            "Player 1: {} VS Player 2: {}".format(self.player_A_lives, self.player_B_lives),
            font=self.style,
            align="center"
        )
