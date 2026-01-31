a, b, c = map(float, input().split())

delta = b ** 2 - 4 * a * c

if delta < 0 or a == 0:
    print("Impossivel calcular")
else:
    d = delta ** 0.5

    root_1 = (-b + d) / (2 * a)
    root_2 = (-b - d) / (2 * a)
    
    print(f"R1 = {root_1:.5f}")
    print(f"R2 = {root_2:.5f}")
