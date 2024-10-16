from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.playerScore = 0
        self.color("white")
        self.teleport(0,280)
        self.ht()
        self.write(arg=f"Score:{self.playerScore}",move=False,align="center",font= ("Arial",12,"normal"))

    def update_score(self):
        self.clear()
        self.playerScore +=1
        self.write(arg=f"Score:{self.playerScore}",move=False,align="center",font= ("Arial",12,"normal"))