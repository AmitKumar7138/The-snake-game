from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.updarte_scoreboard()

    def updarte_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT,
                   font=FONT)

    def inc_score(self):
        self.score += 1
        self.clear()
        self.updarte_scoreboard()

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", align=ALIGNMENT,
                   font=FONT)
