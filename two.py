import matplotlib.pyplot as plt
import numpy as np

def koch_snowflake(order, size):
    if order == 0:
        return [(0, 0), (size, 0)]
    
    x1, y1 = koch_snowflake(order - 1, size / 3)[0]
    x2, y2 = koch_snowflake(order - 1, size / 3)[1]
    x3, y3 = (x1 + (x2 - x1) / 2 - np.sqrt(3) * (y2 - y1) / 2,
              y1 + (y2 - y1) / 2 + np.sqrt(3) * (x2 - x1) / 2)
    x = [x1, x3, (x1 + x2) / 2, x3, x2]
    y = [y1, y3, (y1 + y2) / 2, y3, y2]
    return list(zip(x, y))

def draw_koch_snowflake(order, size):
    points = np.array(koch_snowflake(order, size))
    plt.figure(figsize=(6, 6))
    plt.axis('equal')
    plt.fill(points[:, 0], points[:, 1], 'b')
    plt.title(f"Сніжинка Коха рівня {order}")
    plt.show()

def main():
    order = int(input("Введіть рівень рекурсії для сніжинки Коха: "))
    size = 400
    draw_koch_snowflake(order, size)

if __name__ == "__main__":
    main()