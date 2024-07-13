import matplotlib.pyplot as plt
import numpy as np

def koch_snowflake(order, size):
    def koch_curve(order, p1, p2):
        if order == 0:
            return [p1, p2]
        else:
            p3 = (2 * p1 + p2) / 3
            p4 = (p1 + 2 * p2) / 3
            angle = np.pi / 3
            p5 = p3 + np.array([np.cos(angle) * (p4[0] - p3[0]) - np.sin(angle) * (p4[1] - p3[1]),
                                np.sin(angle) * (p4[0] - p3[0]) + np.cos(angle) * (p4[1] - p3[1])])
            return (koch_curve(order-1, p1, p3) +
                    koch_curve(order-1, p3, p5)[1:] +
                    koch_curve(order-1, p5, p4)[1:] +
                    koch_curve(order-1, p4, p2)[1:])

    p1 = np.array([0, 0])
    p2 = np.array([size, 0])
    p3 = np.array([size / 2, np.sqrt(size**2 - (size / 2)**2)])
    return (koch_curve(order, p1, p2)[:-1] +
            koch_curve(order, p2, p3)[:-1] +
            koch_curve(order, p3, p1))

def draw_koch_snowflake(order, size):
    points = np.array(koch_snowflake(order, size))
    plt.figure(figsize=(8, 8))
    plt.plot(points[:, 0], points[:, 1], 'b')
    plt.axis('equal')
    plt.title(f"Сніжинка Коха рівня {order}")
    plt.show()

def main():
    order = int(input("Введіть рівень рекурсії для сніжинки Коха: "))
    size = 400
    draw_koch_snowflake(order, size)

if __name__ == "__main__":
    main()