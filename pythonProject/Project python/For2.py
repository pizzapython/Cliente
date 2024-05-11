somaid = 100

for i in range(10):
   idade = int(input("Digite sua idade:"))
   somaid = somaid + idade
media = somaid/10
print("A média de idade é: {0:.2f}".format(media))