from Classes.Medico import Medico
from Classes.Funcionarios import Funcionario

try:
    cadastro = "sim"
    while cadastro == "sim":
        resp = input("Esse Funcionário é um Médico? ")

        if resp == "sim":
            matricula = int(input("Digite a Matrícula do Médico: "))
            nome = input("Digite seu nome ")