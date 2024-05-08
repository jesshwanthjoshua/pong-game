from turtle import Turtle
from random import choice


class Ball(Turtle):

    def __init__(self):
        super().__init__()

        self.heading_list = [45, 135, 225, 315]
        self.shape("circle")
        self.color("light sky blue")
        self.penup()
        self.setheading(choice(self.heading_list))
        self.move_speed = 0.1

    def reset_position(self, heading):
        self.setpos(0, 0)
        r_head = [45, 315]
        l_head = [135, 225]

        if heading == 45 or heading == 315:
            self.setheading(choice(l_head))

        elif heading == 135 or heading == 225:
            self.setheading(choice(r_head))

    def play(self):
        x = self.xcor()
        y = self.ycor()
        # print(f"x = {x}, y = {y}")

        if self.heading() == 45 or self.heading() == 135:
            if self.heading() == 45:
                if self.xcor() <= 390 and self.ycor() < 280:
                    self.goto(x + 10, y + 10)

                elif self.ycor() == 280:
                    self.setheading(315)

            elif self.heading() == 135:
                if self.xcor() >= -390 and self.ycor() < 280:
                    self.setpos(x - 10, y + 10)

                elif self.ycor() == 280:
                    self.setheading(225)

        elif self.heading() == 225 or self.heading() == 315:
            if self.heading() == 225:
                if self.xcor() >= -390 and self.ycor() > -280:
                    self.setpos(x - 10, y - 10)

                elif self.ycor() == -280:
                    self.setheading(135)

            elif self.heading() == 315:
                if self.xcor() <= 390 and self.ycor() > -280:
                    self.setpos(x + 10, y - 10)

                elif self.ycor() == -280:
                    self.setheading(45)
