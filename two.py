import turtle

# Функція для малювання кривої Коха
def fractal_curve(t, level, length):
    if level == 0:
        t.forward(length)
    else:
        for angle in [60, -120, 60, 0]:
            fractal_curve(t, level - 1, length / 3)
            t.left(angle)

# Функція для малювання сніжинки Коха
def fractal_snowflake(t, level, length):
    for _ in range(3):
        fractal_curve(t, level, length)
        t.right(120)

# Функція для налаштування екрану і початку малювання сніжинки Коха
def draw_fractal_snowflake(level, length=300):
    screen = turtle.Screen()
    screen.bgcolor("white")

    pen = turtle.Turtle()
    pen.speed(0)
    pen.penup()
    pen.goto(-length / 2, length / 3)
    pen.pendown()

    fractal_snowflake(pen, level, length)

    screen.mainloop()

if __name__ == "__main__":
    try:
        level = int(input("Введіть рівень рекурсії для сніжинки Коха: "))
        draw_fractal_snowflake(level)
    except ValueError:
        print("Некоректний ввід. Будь ласка, введіть ціле число для рівня рекурсії.")