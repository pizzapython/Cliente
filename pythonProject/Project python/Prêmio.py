total = float(input("Digite o valor total do prêmio: R$ "))

imposto = (total * 7)/100
liquido = (total - imposto)
primeiro= (liquido * 46)/100
segundo = (liquido * 32)/100
terceiro = liquido - primeiro - segundo - imposto

print("Total do prêmio: R$", total)
print("Prêmio descontado o imposto (7%): R$", liquido)
print("Valor recebido pelo primeiro ganhador: R$", primeiro)
print("Valor recebido pelo segundo ganhador: R$", segundo)
print("Valor recebido pelo terceiro ganhador: R$", terceiro)


