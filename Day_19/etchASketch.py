from turtle import Turtle,Screen

class EtchASketch:
    def __init__(self,turtle):
        self.turtle = turtle
        self.screen = Screen()
        self.turtle.speed("fastest")
        self.screen.colormode(255)

    def move_fd(self):
        self.turtle.fd(10)

    def move_bk(self):
        self.turtle.bk(10)

    def move_l(self):
        self.turtle.left(5)

    def move_r(self):
        self.turtle.right(5)

    def clear(self):
        self.turtle.reset()

    def draw_dot(self,x, y):
        self.turtle.teleport(x, y)
        self.turtle.pendown()
        self.turtle.dot(10)

    def draw(self,x,y):
        self.turtle.goto(x,y)

    def teleport_to(self,x,y):
        self.turtle.teleport(x,y)

tim = Turtle()
# screen = Screen()
tim.shape("classic")
tim.color("black")

sketch = EtchASketch(tim)

# sketch.screen.onscreenclick(sketch.draw_dot) # even listener  is active no need to call it actively

sketch.screen.listen()# even listener  is in - active , need to call it actively
sketch.screen.onkey(fun=sketch.move_fd, key="w")
sketch.screen.onkey(fun=sketch.move_bk, key="s")
sketch.screen.onkey(fun=sketch.move_l,key= "a")
sketch.screen.onkey(fun=sketch.move_r,key = "d")
sketch.screen.onkey(fun=sketch.clear,key = "c")

# sketch.screen.onscreenclick(sketch.teleport_to)
# sketch.turtle.ondrag(sketch.draw,1)


sketch.screen.mainloop()  # Keep the window open