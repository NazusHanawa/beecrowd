a, b, c = map(int, input().split())

x = max_ab = (a + b + abs(a - b)) / 2
max_xc = (x + c + abs(x - c)) / 2

print(f"{max_xc:.0f} eh o maior")
