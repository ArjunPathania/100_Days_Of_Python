from turtle import Turtle;STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)];MOVE_DISTANCE = 20;UP = 90;DOWN = 270;LEFT = 180;RIGHT = 0
class SnakeBody:
    def __init__(self):
        """Initialise the  snake"""
        self.segments = [] #Lit of Turtle type objects, each representing a segment of the snakes main body
        self.create_snake() #Class method th create snake
        self.head = self.segments[0] #first segments is considered as head rest as tail

    def create_snake(self):
        """Creating the initial body of the snake"""
        for position in STARTING_POSITIONS: # initialising the body of the snake for each coordinate in the starting position
            self.add_segment(position) # passing position to add_segment method

    def add_segment(self, position):
        """Adding individual turtle typ objects to the segment list to represent the snake body"""
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position) #postion is tuple from the list STARTING_POSITIONS (x-coordinate,y-coordinate)
        self.segments.append(segment)

    def move(self):
        """Function to move the snake in manner that the last segment takes place of the second last segment in front of it and so on this way the whole snake will follow thw head"""
        # Move each segment to the position of the segment in front of it, starting from the last segment
        # for segment in self.segments:
        #     segment.fd(20)
        for seg_num in range(len(self.segments) - 1,0,-1): #start at last element,end at 0th element, step one place backwards
            new_x = self.segments[seg_num - 1].xcor() #x - coordinate
            new_y = self.segments[seg_num - 1].ycor() # y - coordinate
            self.segments[seg_num].goto(new_x, new_y) # the follower segments moves to the position of the segment leading it
        # Move the first segment forward
        self.head.forward(MOVE_DISTANCE)

    # def left(self):
    #     """move snake head to up"""
        # for segment in self.segments:
        #     segment.left(90)
        #     self.move()
        # if self.head.heading() == 270:
        #     pass
        # else:
        #     self.head.setheading(90)

    def up(self):
        """move snake head to up"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        # if self.head.heading() == 270:
        #     pass
        # else:
        #     self.head.setheading(90)

    def down(self):
        """moves snake head to down"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        # if self.head.heading() == 90:
        #     pass
        # else:
        #     self.head.setheading(270)

    def left(self):
        """move snake head to left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        # if self.head.heading() == 0:
        #     pass
        # else:
        #     self.head.setheading(180)

    def right(self):
        """moves snake head to right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        # if self.head.heading() == 180:
        #     pass
        # else:
        #     self.head.setheading(0)

    def extend(self):
        """Add a new segment to the snake after eating food."""
        self.add_segment(self.segments[-1].position())  # Add a new segment at the last segment's position

    def detect_collision_with_wall(self):
        if self.head.xcor() > 290 or self.head.xcor() < -290 or self.head.ycor() > 290 or self.head.ycor() < -290:
            return True
        return False

    def detect_collision_with_self(self):
        """Check if the snake collides with its own body."""
        for segment in self.segments[1:]:  # Ignore the head
            if self.head.distance(segment) < 10:
                return True
        return False
    #
    # def reset_snake(self):
    #     self.segments = []  # Lit of Turtle type objects, each representing a segment of the snakes main body
    #     self.create_snake()  # Class method th create snake
    #     self.head = self.segments[0]  # first segments is considered as head rest as tail