import turtle


def draw_branch(t, length, level):
    if level == 0:
        return

    t.forward(length)
    t.left(45)
    draw_branch(t, length * 0.7, level - 1)
    t.right(90)
    draw_branch(t, length * 0.7, level - 1)
    t.left(45)
    t.backward(length)


def main():
    level = int(input("Enter recursion level: "))

    screen = turtle.Screen()
    screen.title("Pythagoras Tree")
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.color("green")
    t.speed(0)
    t.left(90)
    t.penup()
    t.goto(0, -250)
    t.pendown()

    draw_branch(t, 100, level)

    print("Close the turtle window to finish.")
    turtle.done()


if __name__ == "__main__":
    main()
