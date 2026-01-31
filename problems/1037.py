value = float(input())

if not(0 <= value <= 100):
    print("Fora de intervalo")
else:
    if value <= 25:
        print("Intervalo [0,25]")
    elif value <= 50:
        print("Intervalo (25,50]")
    elif value <= 75:
        print("Intervalo (50,75]")
    else:
        print("Intervalo (75,100]")
