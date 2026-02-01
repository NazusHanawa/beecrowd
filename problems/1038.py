code, quantity = map(int, input().split())

items = [4, 4.5, 5, 2, 1.5]

total = items[code-1] * quantity

print(f"Total: R$ {total:.2f}")
