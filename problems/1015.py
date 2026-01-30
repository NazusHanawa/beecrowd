x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

dist_x = x1 - x2
dist_y = y1 - y2
distance = (dist_x ** 2 + dist_y ** 2) ** 0.5

print(f"{distance:.4f}")
