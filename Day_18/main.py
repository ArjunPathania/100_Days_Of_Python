import random
from turtle import Turtle, Screen
import colorgram

def random_color():
    """Generates a random RGB color."""
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


class ShapeDrawer:
    def __init__(self, turtle):
        self.turtle = turtle
        self.screen = Screen()
        self.screen.colormode(255)
        self.damien_hirst_palette = None
        self.screen.setup(width=800, height=600)  # Set up the screen size
        self.min_x = -self.screen.window_width() // 2
        self.max_x = self.screen.window_width() // 2
        self.min_y = -self.screen.window_height() // 2
        self.max_y = self.screen.window_height() // 2

    def check_boundary(self):
        """Checks if the turtle is near the screen boundary and makes it bounce back."""
        x, y = self.turtle.xcor(), self.turtle.ycor()
        if x < self.min_x or x > self.max_x or y < self.min_y or y > self.max_y:
            self.turtle.setheading(self.turtle.heading() + 180)  # Turn around

    def draw_square(self, size):
        """Draws a square of a given size."""
        for _ in range(4):
            self.turtle.forward(size)
            self.turtle.left(90)

    def draw_dotted_line(self, size):
        """Draws a dotted line of a given size."""
        self.turtle.pencolor(240, 160, 80)
        for _ in range(size):
            self.turtle.forward(10)
            self.turtle.penup()
            self.turtle.forward(10)
            self.turtle.pendown()

    def draw_shape(self, no_of_sides, length=100):
        """Draws a polygon with a given number of sides."""
        start_x, start_y = -80, -100
        self.turtle.teleport(start_x, start_y)
        self.turtle.pensize(2)
        angle = 360 / no_of_sides
        for _ in range(no_of_sides):
            self.turtle.color(random_color())
            self.turtle.forward(length)
            self.turtle.left(angle)

    def random_walk(self, steps):
        """Turtle takes a random walk with specified steps."""
        angles = [0, 90, 180, 270]
        self.turtle.pensize(10)

        for _ in range(steps):
            self.turtle.color(random_color())
            self.turtle.setheading(random.choice(angles))
            self.turtle.forward(50)
            self.check_boundary()  # Check boundary after every move

    # def drunk_walk(self, steps):
    #     """Turtle takes a random walk with random angles."""
    #     self.turtle.pensize(10)
    #
    #     for _ in range(steps):
    #         self.turtle.color(random_color())
    #         self.turtle.setheading(random.randint(0, 355))
    #         self.turtle.forward(10)
    #         self.check_boundary()  # Check boundary after every move

    # def leap_of_faith(self, steps):
    #     """Turtle takes larger random steps."""
    #     self.turtle.pensize(10)
    #
    #     for _ in range(steps):
    #         self.turtle.color(random_color())
    #         self.turtle.setheading(random.randint(0, 355))
    #         self.turtle.forward(200)
    #         self.check_boundary()  # Check boundary after every move

    def spirograph(self, circles, radius):
        """Draws a spirograph pattern."""
        phase_change = 360 / circles
        for _ in range(circles):
            self.turtle.pensize(2)
            self.turtle.color(random_color())
            self.turtle.circle(radius)
            self.turtle.right(phase_change)

    def draw_damien_hirst_pattern(self, size, dot_size=15, spacing=30):
        """Draws a dot pattern inspired by Damien Hirst."""
        if self.damien_hirst_palette is None:
            try:
                self.damien_hirst_palette = colorgram.extract('damienHirst.png', 100)
            except FileNotFoundError:
                print("The file 'damienHirst.png' was not found.")
                return

        rgb_colors = [color.rgb for color in self.damien_hirst_palette]

        self.turtle.hideturtle()
        self.turtle.speed("fastest")

        self.screen.tracer(0)  # Disable screen updates for faster drawing

        start_x, start_y = -300, -250
        self.turtle.teleport(start_x, start_y)

        for row in range(size):
            for col in range(size):
                rgb = random.choice(rgb_colors)
                self.turtle.color(rgb)
                self.turtle.dot(dot_size)
                self.turtle.forward(spacing)

            # Move to the next row
            self.turtle.goto(start_x, start_y + (row + 1) * spacing)

        self.screen.update()  # Re-enable screen updates after drawing is done


# Set up the turtle and screen
timmy = Turtle(shape="turtle")
timmy.speed("fastest")
screen = Screen()

shape_drawer = ShapeDrawer(timmy)

# Uncomment below to test various functionalities

# shape_drawer.draw_dotted_line(15)
# shape_drawer.draw_square(100)

for sides in range(3, 11):
    shape_drawer.draw_shape(sides)

# shape_drawer.random_walk(1000)

# shape_drawer.spirograph(36, 200)

# shape_drawer.draw_damien_hirst_pattern(size=25, dot_size=15, spacing=25)

# shape_drawer.drunk_walk(1000)

# shape_drawer.leap_of_faith(2000)


screen.exitonclick()
