value = int(input())

cashs = [100, 50, 20, 10, 5, 2, 1]

print(value)
for cash in cashs:
    banknotes = value // cash
    print(f"{banknotes} nota(s) de R$ {cash},00")
    
    value %= cash
