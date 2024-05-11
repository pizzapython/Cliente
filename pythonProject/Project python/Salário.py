mes = input("Digite o mês");
salbruto = float(input("Digite o salário bruto"));
desimposto = salbruto * 11/100;
desinss = salbruto * 8/100;
dessindicato = salbruto * 5/100;
soma = salbruto - desimposto - desinss - dessindicato;
print("O salário líquido é de", soma);
