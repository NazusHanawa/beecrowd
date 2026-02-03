a, b = map(int, input().split())

def is_multiple(a, b):
    if a // b == a / b:
        return True
    if b // a == b / a:
        return True
    
    return False

if is_multiple(a, b):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
    