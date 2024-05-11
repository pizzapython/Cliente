totdesconto = 0.0

for i in range(10):
    nome = input("Digite seu nome:")
    compra = float(input("Digite o valor da compra:"))
    if compra >= 1500:
    desconto = compra * 0.2
    else:
    desconto = compra * 0.15

    print("Nome :", nome)
    print("Compra : R${0:.2f}".format(compra))
    print("Desconto: R${0:.2f}".format(desconto))
    print("Pagar : R${0:.2f}".format(compra - desconto))
totdesconto = desconto + desconto
print("total descontos: R${0:.2f}".format(totdesconto))