from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.x_move = 10  # x-coordinate movement
        self.y_move = 10  # y-coordinate movement
        self.move_speed = 0.1  # speed of the ball
        self.width = 20  # width of the bounding box
        self.height = 20  # height of the bounding box

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1  # bounce off the wall on y-axis

    def bounce_x(self):
        self.x_move *= -1  # bounce off the wall on x-axis
        self.move_speed *= 0.9  # increase speed after bounce

    def reset_position(self):
        self.goto(0, 0)  # reset to center
        self.move_speed = 0.1  # reset speed
        self.bounce_x()  # bounce off the wall

    def bounding_box(self):
        x1, y1 = self.xcor() - (self.width / 2), self.ycor() + (self.height / 2)
        x2, y2 = self.xcor() + (self.width / 2), self.ycor() - (self.height / 2)
        return x1, y1, x2, y2  # return the bounding box coordinates
