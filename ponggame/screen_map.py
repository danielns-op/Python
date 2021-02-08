from turtle import Turtle


class LineMiddle:
    def __init__(self):
        self.middle_line = []
        self.draw_line()

    def draw_line(self):
        for y in range(-235, 250, 45):
            self.line_add_seg(position=y)

    def line_add_seg(self, position):
        new_seg = Turtle(shape='square')
        new_seg.shapesize(stretch_wid=1, stretch_len=0.5)
        new_seg.color('DarkGrey')
        new_seg.penup()
        new_seg.goto(x=0, y=position)
        self.middle_line.append(new_seg)
