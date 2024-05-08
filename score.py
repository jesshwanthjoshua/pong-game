from turtle import Turtle

font_style = ("Comic Sans MS", 25, "italic")


class Score(Turtle):

    def __init__(self):
        super().__init__()

        self.pos_list = [(-50, 250), (50, 250)]
        self.score_list = []
        self.score_r_player = 0
        self.score_l_player = 0

        for pos in self.pos_list:
            self.score = Turtle("square")
            self.score.color("white")
            self.score.penup()
            self.score.hideturtle()
            self.score.setpos(pos)
            self.score_list.append(self.score)

        self.score_list[0].write(self.score_l_player, False, align="center", font=font_style)
        self.score_list[1].write(self.score_r_player, False, align="center", font=font_style)

    def r_score(self):
        self.score_r_player += 1
        self.score_list[1].clear()
        self.score_list[1].write(self.score_r_player, False, align="center", font=font_style)

    def l_score(self):
        self.score_l_player += 1
        self.score_list[0].clear()
        self.score_list[0].write(self.score_l_player, False, align="center", font=font_style)
