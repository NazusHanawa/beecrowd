PI = 3.14159
a, b, c = map(float, input().split())

triangle = a * c / 2
circle = c ** 2 * PI
trapezium = c * (a + b) / 2 
square = b ** 2
rectangle = a * b

print(f"TRIANGULO: {triangle:.3f}")
print(f"CIRCULO: {circle:.3f}")
print(f"TRAPEZIO: {trapezium:.3f}")
print(f"QUADRADO: {square:.3f}")
print(f"RETANGULO: {rectangle:.3f}")
