value = int(float(input())*100)

notes = [100, 50, 20, 10, 5, 2]
coins = [1, 0.5, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for cash in notes:
    cash_cents = cash*100
    banknotes = int(value // cash_cents)
    print(f"{banknotes} nota(s) de R$ {cash:.2f}")
    
    value %= cash_cents
    
print("MOEDAS:")
for cash in coins:
    cash_cents = cash*100
    banknotes = int(value // cash_cents)
    print(f"{banknotes} moeda(s) de R$ {cash:.2f}")
    
    value %= cash_cents
