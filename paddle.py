from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()

        self.x = 0
        self.y = 0
        self.pos_list = [(-380, 0), (380, 0)]
        self.pad_list = []
        self.bat()


    def bat(self):

        for pos in self.pos_list:
            self.paddle = Turtle("square")
            self.paddle.penup()
            self.paddle.color("white")
            self.paddle.shapesize(stretch_wid=1, stretch_len=5)
            self.paddle.setpos(pos)
            self.paddle.setheading(90)
            self.pad_list.append(self.paddle)

    def fwd_r(self):
        self.pad_list[1].forward(20)

    def bwd_r(self):
        self.pad_list[1].backward(20)

    def fwd_l(self):
        self.pad_list[0].forward(20)

    def bwd_l(self):
        self.pad_list[0].backward(20)
