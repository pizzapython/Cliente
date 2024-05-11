paes = int(input("Digite a quantidade de pães vendidos: "))
broas = int(input("Digite a quantidade de broas vendidas: "))
poupanca = 0.43 * 0.15
euros = 0.15/4.5
total = (paes * 0.80) + (broas * 2.50)
custofbc = total * 0.43
restante = total - custofbc

print("Venda total de pães e broas: R$", total)
print("Custos de fabricação: R$", custofbc)
print("Valor guardado na poupança: R$", poupanca)
print("Quantidade de euros comprados: €", euros)