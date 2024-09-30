from turtle import *  # Python Turtle Graphics Library
from random import randrange 
from freegames import square, vector

# Defining the global variables
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Creating the control variables

def change(x, y):
    # Change Snake Direction
    aim.x = x
    aim.y = y

def inside(head):
    # Return True if the head touches the boundary
    return -278 < head.x < 190 and -278 < head.y < 190

def move():
    # Move the snake in the forward direction
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return 
    snake.append((head))

    if head == food:
        print('snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'green')

    square(food.x, food.y, 9, 'red')
    update()
    ontimer(move, 100)


hideturtle()
tracer(False)
listen()
onkey(lambda : change(10, 0), 'Right')
onkey(lambda : change(-10, 0), 'Left')
onkey(lambda : change(0, 10), 'Up')
onkey(lambda : change(0, -10), 'Down')
move()
done()