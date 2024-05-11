temp = float(input("Escreva a temperatura"))

if temp >= 30:
    print("Muito calor")
elif temp >= 24:
    print("Calor")
elif temp >= 17:
    print("Temperatura Amena")
elif temp >= 7:
    print("Temperatura Fria")
elif temp <= 0:
    print("Temperatura igual a 0 ou abaixo de 0")
else:
    print("Temperatura muito fria")