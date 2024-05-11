def calcular_juros_simples(divida, parcelas, juros):
    valor_juros = divida * (juros / 100)
    valor_unico = divida + valor_juros
    valor_parcela = valor_unico / parcelas
    return valor_juros, valor_parcela

def main():
    while True:
        divida = float(input("Digite o valor da dívida (ou -1 para sair): "))
        if divida == -1:
            print("Programa encerrado.")
            break

        parcelas = int(input("Digite a quantidade de parcelas: "))
        taxa_juros = float(input("Digite a taxa de juros (em %): "))

        valor_juros, valor_parcela = calcular_juros_simples(divida, parcelas, taxa_juros)

        print("\n### Detalhes da Dívida ###")
        print(f"Valor da dívida: R${divida:.2f}")
        print(f"Valor dos juros: R${valor_juros:.2f}")
        print(f"Quantidade de parcelas: {parcelas}")
        print(f"Valor da parcela: R${valor_parcela:.2f}\n")


if __name__ == "__main__":
    main()