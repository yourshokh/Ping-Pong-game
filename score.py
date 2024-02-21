from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()


        self.color('white')
        self.penup()
        self.hideturtle()


        self.lscore=0
        self.rscore=0
        self.update_screen()


    def update_screen(self):
        self.clear()
        self.goto(50, 270)
        self.write(f'Score: {self.lscore}', True, align="left", font=("Arial",10,"normal"))

        self.goto(-50, 270)
        self.write(f'Score: {self.rscore}', True, align="left", font=("Arial", 10, "normal"))

    def lincrease(self):
        self.lscore+=1
        self.update_screen()
    def rincrease(self):
        self.rscore+=1
        self.update_screen()



