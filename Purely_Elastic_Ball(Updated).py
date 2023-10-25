import turtle 
import random
import time
import numpy as np
import threading

#Constant Downwards Acceleration Factor
gravity = 0.1

def create_window(setup=(800, 600)):
    wn = turtle.Screen()
    wn.bgcolor(0, 0, 0)
    wn.title("Ball Simulator")
    wn.setup(800,600)
    wn.colormode(255)
    wn.tracer(0)
    return wn

class Ball:
    def __init__(self, window, pos=(0, 200), penDown=False):
        self.wn = window
        self.ball = turtle.Turtle()
        self.ball.color(random.choice(["red", "blue", "yellow", "white", "purple"]))
        self.ball.shape("circle")
        if not penDown: self.ball.penup()
        self.ball.shapesize(2,2)
        self.startpos = pos
        self.ball.goto(self.startpos[0],self.startpos[1])
        self.ball.dy = 0
        self.ball.dx = 0
        self.ball.speed(0)
        self.wn.listen()
        self.wn.onkeypress(self.goup,"Up")
        self.wn.onkeypress(self.goleft,"Left")
        self.wn.onkeypress(self.goright,"Right")
        self.wn.onkeypress(self.godown,"Down")
    
    def goup(self):
        self.ball.dy = self.ball.dy + 1

    def goleft(self):
        self.ball.dx = self.ball.dx - 1

    def goright(self):
        self.ball.dx = self.ball.dx + 1

    def godown(self):
        self.ball.dy = self.ball.dy - 1

    def reset(self):
        self.ball.setx(0)
        self.ball.sety(200)
        self.ball.dx = 0
        self.ball.dy = 0

    def play(self):
        while True:
            time.sleep(0.01)
            self.wn.bgcolor(0,0,0)
            self.wn.update()
            self.ball.dy -= gravity
            self.ball.sety(self.ball.ycor() + self.ball.dy)
            self.ball.setx(self.ball.xcor() + self.ball.dx)
            

            if self.ball.ycor() <= -270 or self.ball.ycor() >= 280:
                self.ball.dy *= -1
            if self.ball.xcor() <= -380 or self.ball.xcor() >= 380:
                self.ball.dx *= -1
            
        self.wn.mainloop()

#For simulating multiple balls simultaneously
class Simulate:
    def __init__(self, wn, balls):
        self.wn = wn
        self.balls = balls
        self.gravity = gravity * len(balls) * 2
        self.wn.listen()
        self.wn.onkeypress(self.goup,"Up")
        self.wn.onkeypress(self.goleft,"Left")
        self.wn.onkeypress(self.goright,"Right")
        self.wn.onkeypress(self.godown,"Down")

    def goup(self):
        for Ball in self.balls:
            Ball.ball.dy = Ball.ball.dy + 1

    def goleft(self):
        for Ball in self.balls:
            Ball.ball.dx = Ball.ball.dx - 1

    def goright(self):
        for Ball in self.balls:
            Ball.ball.dx = Ball.ball.dx + 1

    def godown(self):
        for Ball in self.balls:
            Ball.ball.dy = Ball.ball.dy - 1

    def play(self):
        while True:
            for Ball in self.balls:
                time.sleep(0.00001)
                self.wn.bgcolor(0,0,0)
                self.wn.update()
                Ball.ball.dy -= self.gravity
                Ball.ball.sety(Ball.ball.ycor() + Ball.ball.dy)
                Ball.ball.setx(Ball.ball.xcor() + Ball.ball.dx)

                #Wall Collision
                if Ball.ball.ycor() <= -280 or Ball.ball.ycor() >= 280:
                    if Ball.ball.ycor() <= -320:
                        Ball.reset()
                    Ball.ball.dy *= -1
                if Ball.ball.xcor() <= -380 or Ball.ball.xcor() >= 380:
                    Ball.ball.dx *= -1
            
        self.wn.mainloop()

if __name__ == "__main__":

    wn = create_window()

    ball1 = Ball(wn, pos=(-50, 250))
    ball2 = Ball(wn, pos=(50, 150))
    ball3 = Ball(wn)

    """
    Single-Ball Simulation 

    simulation = Simulate(wn, [ball1])
    simulation.play()
    
    or

    simulation = ball1.play()
    """

    #Simulating Multiple Balls :)
    simulation = Simulate(wn, [ball1, ball2, ball3])
    simulation.play()
