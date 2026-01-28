a_code, a_quantity, a_price = map(float, input().split())
b_code, b_quantity, b_price = map(float, input().split())

total_value = a_quantity * a_price + b_quantity * b_price
print(f"VALOR A PAGAR: R$ {total_value:.2f}")
