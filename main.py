import turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time
T=0.05

screen=turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

ball=Ball()
paddles=Paddle()
score=Score()

screen.listen()
screen.onkey(paddles.rgo_up,"Up")
screen.onkey(paddles.rgo_down, "Down")
screen.onkey(paddles.lgo_up,"w")
screen.onkey(paddles.lgo_down,"s")
t=[0.1 ,0.09 ,0.08, 0.07, 0.06, 0.05]
score_sum = [7, 10, 13, 16, 19, 21]

gameison=True
while gameison:
    if score.lscore+score.rscore<=7:
        T=t[0]
    elif score.lscore+score.rscore<=10 and score.lscore+score.rscore>7:
        T=t[1]
    elif score.lscore+score.rscore<=13 and score.lscore+score.rscore>10:
        T=t[2]
    elif score.lscore + score.rscore <= 16 and score.lscore + score.rscore > 13:
        T = t[3]
    elif score.lscore+score.rscore<=19 and score.lscore+score.rscore>16:
        T=t[4]
    elif score.lscore+score.rscore<=21 and score.lscore+score.rscore>19:
        T=t[5]

    time.sleep(T)
    screen.update()
    ball.move()

    if ball.xcor()>380:
        ball.reset()
        score.rincrease()


    if ball.xcor()<-380:
        ball.reset()
        score.lincrease()


    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    if ball.distance(paddles.r_paddle)<50 and ball.xcor()>320:
        ball.bounce_x()

    if ball.distance(paddles.l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()


screen.exitonclick()

