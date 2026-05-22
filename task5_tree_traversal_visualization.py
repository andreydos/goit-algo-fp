import time
import turtle
import uuid
from collections import deque


class Node:
    def __init__(self, key, color="#1f4e79"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def build_heap_tree(values):
    if not values:
        return None

    nodes = [Node(value) for value in values]

    for index, node in enumerate(nodes):
        left_index = 2 * index + 1
        right_index = 2 * index + 2

        if left_index < len(nodes):
            node.left = nodes[left_index]
        if right_index < len(nodes):
            node.right = nodes[right_index]

    return nodes[0]


def get_all_nodes(root):
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node)

        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

    return result


def reset_colors(root):
    for node in get_all_nodes(root):
        node.color = "#1f4e79"


def generate_color(step, total_steps):
    if total_steps <= 1:
        return "#d6ebff"

    start = 40
    end = 220
    value = start + int((end - start) * step / (total_steps - 1))
    return f"#{value:02x}{value:02x}ff"


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
    t.pencolor("black")
    t.write(str(value), align="center", font=("Arial", 12, "normal"))


def draw_tree(t, node, x, y, dx):
    if node is None:
        return

    draw_node(t, x, y, node.val, node.color)

    if node.left is not None:
        t.penup()
        t.goto(x, y - 20)
        t.pendown()
        t.goto(x - dx, y - 80)
        draw_tree(t, node.left, x - dx, y - 80, dx / 2)

    if node.right is not None:
        t.penup()
        t.goto(x, y - 20)
        t.pendown()
        t.goto(x + dx, y - 80)
        draw_tree(t, node.right, x + dx, y - 80, dx / 2)


def bfs_order(root):
    if root is None:
        return []

    order = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        order.append(node)

        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

    return order


def dfs_order(root):
    if root is None:
        return []

    order = []
    stack = [root]

    while stack:
        node = stack.pop()
        order.append(node)

        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)

    return order


def animate_traversal(screen, t, root, title, order):
    reset_colors(root)
    total_steps = len(order)

    for step, node in enumerate(order):
        node.color = generate_color(step, total_steps)
        t.clear()
        screen.title(f"{title} - step {step + 1}")
        draw_tree(t, root, 0, 250, 200)
        screen.update()
        time.sleep(1)


if __name__ == "__main__":
    screen = turtle.Screen()
    screen.setup(width=1000, height=700)
    screen.tracer(0, 0)

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.pensize(2)

    values = [0, 4, 1, 5, 10, 3]
    root = build_heap_tree(values)

    animate_traversal(screen, t, root, "DFS", dfs_order(root))
    animate_traversal(screen, t, root, "BFS", bfs_order(root))

    print("Close the turtle window to finish.")
    turtle.done()
