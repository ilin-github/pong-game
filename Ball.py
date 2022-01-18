from turtle import Turtle

INIT_MOVE_SPEED = 0.1
SPEED_REDUCE_STEP = 0.95


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(1, 1)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = INIT_MOVE_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move = self.y_move * -1
        self.move_speed *= SPEED_REDUCE_STEP

    def bounce_x(self):
        self.x_move = self.x_move * -1
        self.move_speed *= SPEED_REDUCE_STEP

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = INIT_MOVE_SPEED
