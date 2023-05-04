from turtle import Turtle


START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in START_POS:
            self.add_seg(pos)


    def add_seg(self, pos):
        new_seg = Turtle('square')
        new_seg.color('white')
        new_seg.penup()
        new_seg.goto(pos)
        self.segments.append(new_seg)

    def extend(self):
        self.add_seg(self.segments[-1].pos())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg_num - 1].xcor()
            y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x, y)
        self.head.forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def off_board(self):
        x = self.head.xcor()
        y = self.head.ycor()
        if self.head.xcor() > 280:
            self.head.goto(-280, y)
        elif self.head.xcor() < - 280:
            self.head.goto(280, y)
        elif self.head.ycor() > 280:
            self.head.goto(x, -280)
        elif self.head.ycor() < -280:
            self.head.goto(x, 280)

