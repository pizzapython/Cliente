nivel = float(input("Digite o nivel do profesor"))
hrs = float(input("Dgite quantas horas o professor da aula"))

if nivel == 1:
    cal = 56
    sal = cal * hrs
    total = sal + (sal * 15/100)
    print("Parabéns!! Você e um professor de nivel 1, o senhor(a) irá ganhar R$56,00 por horas/aula")
elif nivel <= 2:
    cal = 66
    sal = cal * hrs
    total = sal + (sal * 15/100)
    print("Parabéns!! Você e um professor de nivel 2, o senhor(a) irá ganhar R$66,00 por horas/aula")
else:
    print("Você não trabalha!")

salt = (sal * 15/100) + salAprender.py
print("Você recebeu o salário de", salt)