import turtle


def draw_tree(t, size, angle, level, thikness=8):
    if level > 0:
        turtle.colormode(255)
        t.pencolor(0, 255 // level, 0)
        t.pensize(thikness)
        t.forward(size)
        t.right(angle)

        # рекурсивний виклик для правого субдерева
        draw_tree(t, 0.8 * size, angle, level - 1, thikness * 0.8)
        t.pencolor(0, 255 // level, 0)
        t.left(2 * angle)

        # рекурсивний виклик для лівого субдерева
        draw_tree(t, 0.8 * size, angle, level - 1, thikness * 0.8)
        t.pencolor(0, 255 // level, 0)
        t.right(angle)

        # повернення назад після досягнення макимальної глибини
        t.forward(-size)


if __name__ == "__main__":
    recurcion_level = int(input("Введіть глибину рекурсії ==> "))
    angle = 30
    branch_length = 130
    window = turtle.Screen()
    t = turtle.Turtle()
    t.speed(20)
    t.left(90)
    t.up()
    t.goto(0, -window.window_height() / 2 + 40)
    t.down()
    try:
        draw_tree(t, branch_length, angle, recurcion_level)
        window.mainloop()
    except:
        print("Вікно було примусово закрито до завершення рекурсії.")
