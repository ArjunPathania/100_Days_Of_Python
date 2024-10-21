from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.speed(10)

        # Ball movement attributes
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 1 / 20  # The initial speed of the ball

    def move_ball(self):
        """Moves the ball by updating its position based on its current velocity."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def detect_collision_with_wall(self):
        """Reverses the ball's Y-axis direction when it collides with the top or bottom wall."""
        if self.ycor() > 280 or self.ycor() < -280:
            self.reverse_y_direction()

    def detect_collision_with_paddle(self, paddle):
        """
        Detects collision with paddles. If the ball collides with a paddle on the right or left side,
        it reverses the X-axis direction and increases speed.
        """
        is_near_right_paddle = self.distance(paddle) < 50 and self.xcor() > 320
        is_near_left_paddle = self.distance(paddle) < 50 and self.xcor() < -320

        if is_near_right_paddle or is_near_left_paddle:
            self.reverse_x_direction()
            self.increase_speed()

    def ball_out_of_bounds(self):
        """Checks if the ball goes out of bounds and resets its position."""
        if self.xcor() > 400 or self.xcor() < -400:
            self.reset_position()

    def reverse_x_direction(self):
        """Reverses the ball's X-axis direction."""
        self.x_move *= -1

    def reverse_y_direction(self):
        """Reverses the ball's Y-axis direction."""
        self.y_move *= -1

    def increase_speed(self):
        """Increases the ball's speed."""
        self.move_speed *= 0.9

    def reset_position(self):
        """Resets the ball to the center and restores its initial speed."""
        self.goto(0, 0)
        self.reverse_x_direction()
        self.move_speed = 1 / 20
