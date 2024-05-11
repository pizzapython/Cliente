tamanho = int(input("Digite o tamanho do vetor: "))
lista1 = []
lista2 = []
lista3 = []
for i in range(tamanho):
    valor = int(input(f"Digite o elemento {i+1}: "))
    (lista1.append(valor))

    valor2 = int(input(f"Digite o elemneto {i+1}: da lista 1: "))
    lista2.append(valor2)

    lista3.append(lista1[i] + lista2[i])

print("Lista 1 :", lista1)
print("Lista 2 :",lista2)
print("Lista preenchida: ", lista1)