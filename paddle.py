from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)
        self.width = 10  # width of the bounding box
        self.height = 50  # height of the bounding box

    def go_up(self):
        new_y = self.ycor() + 20  # move up
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20  # move down
        self.goto(self.xcor(), new_y)

    def bounding_box(self):
        x1, y1 = self.xcor() - (self.width / 2), self.ycor() + (self.height / 2)
        x2, y2 = self.xcor() + (self.width / 2), self.ycor() - (self.height / 2)
        return x1, y1, x2, y2  # return the bounding box coordinates

