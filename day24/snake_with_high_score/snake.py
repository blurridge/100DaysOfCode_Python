# Snake

from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0 

class Snake:

    def __init__(self):
        self.snake_body = list()
        self.create_snake()
        self.head = self.snake_body[0]
        self.tail = self.snake_body[-1]

    def add_pixel(self, position):
        new_pixel = Turtle("square")
        new_pixel.color("white")
        new_pixel.penup()
        new_pixel.setpos(position)
        self.snake_body.append(new_pixel)
    
    def create_snake(self):
        for i in range(3):
            self.add_pixel((i+-20, 0))

    def extend(self):
        for i in range(2):
            self.add_pixel(self.snake_body[-1].position())
    
    def wall_collision(self):
        if self.head.xcor() > 285 or self.head.xcor() < -290 or self.head.ycor() > 290 or self.head.ycor() < -285:
            return True
        return False
    
    def tail_collision(self):
        for i in range(1, len(self.snake_body)):
            if self.head.distance(self.snake_body[i]) <= 1:
                return True
        return False
    
    def move(self):
        for i in range(len(self.snake_body) - 1, 0, -1):
            x = self.snake_body[i - 1].xcor()
            y = self.snake_body[i - 1].ycor()
            self.snake_body[i].setpos(x, y)
        self.head.forward(10)
    
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

    def reset(self):
        for pixels in self.snake_body:
            pixels.setpos(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]