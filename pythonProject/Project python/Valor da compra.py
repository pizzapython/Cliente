compra = float(input("Digite o valor da compra: R$ "))
if compra <= 2000:
    desconto = compra * 0.10
elif compra <= 3000:
    desconto = compra * 0.05
elif compra <= 5000:
    desconto = compra * 0.03
else:
    desconto = compra * 0.02

pagar = compra-desconto
print("\n Valor da compra: R$ ",compra)
print("\n Valor do desconto: R$ ",desconto)
print("Total a pagar: R$ ",pagar)


