from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.r_paddle=Turtle()
        self.r_paddle.shape('square')
        self.r_paddle.color('white')
        self.r_paddle.shapesize(stretch_wid=5,stretch_len=1)
        self.r_paddle.penup()
        self.r_paddle.goto(350,0)

        self.l_paddle = Turtle()
        self.l_paddle.shape('square')
        self.l_paddle.color('white')
        self.l_paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.l_paddle.penup()
        self.l_paddle.goto(-350, 0)

        self.screen.update()

    def rgo_up(self):
        newy = self.r_paddle.ycor() + 20
        newx = self.r_paddle.xcor()
        self.r_paddle.goto(newx, newy)
        self.screen.update()

    def rgo_down(self):
        newy = self.r_paddle.ycor() - 20
        newx = self.r_paddle.xcor()
        self.r_paddle.goto(newx, newy)
        self.screen.update()

    def lgo_up(self):
        newy = self.l_paddle.ycor() + 20
        newx = self.l_paddle.xcor()
        self.l_paddle.goto(newx, newy)
        self.screen.update()

    def lgo_down(self):
        newy = self.l_paddle.ycor() - 20
        newx = self.l_paddle.xcor()
        self.l_paddle.goto(newx, newy)
        self.screen.update()