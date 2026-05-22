import turtle
import uuid


class Node:
    def __init__(self, key, color="lightblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def build_heap_tree(heap):
    if not heap:
        return None

    nodes = [Node(value) for value in heap]

    for index, node in enumerate(nodes):
        left_index = 2 * index + 1
        right_index = 2 * index + 2

        if left_index < len(nodes):
            node.left = nodes[left_index]
        if right_index < len(nodes):
            node.right = nodes[right_index]

    return nodes[0]


def draw_node(t, x, y, value, color):
    t.penup()
    t.goto(x, y - 20)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    t.penup()
    t.goto(x, y - 8)
    t.write(str(value), align="center", font=("Arial", 12, "normal"))


def draw_edges_and_nodes(t, node, x, y, dx):
    if node is None:
        return

    draw_node(t, x, y, node.val, node.color)

    if node.left is not None:
        t.penup()
        t.goto(x, y - 20)
        t.pendown()
        t.goto(x - dx, y - 80)
        draw_edges_and_nodes(t, node.left, x - dx, y - 80, dx / 2)

    if node.right is not None:
        t.penup()
        t.goto(x, y - 20)
        t.pendown()
        t.goto(x + dx, y - 80)
        draw_edges_and_nodes(t, node.right, x + dx, y - 80, dx / 2)


def draw_tree(root):
    screen = turtle.Screen()
    screen.title("Binary Heap")
    screen.setup(width=1000, height=700)

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.pensize(2)

    draw_edges_and_nodes(t, root, 0, 250, 200)
    print("Close the turtle window to finish.")
    turtle.done()


if __name__ == "__main__":
    heap = [10, 8, 6, 5, 3, 2, 4]
    root = build_heap_tree(heap)
    draw_tree(root)
