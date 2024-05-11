def juros_de_dividas(divida, parcelas):
    if parcelas == 1:
     juros = 0

    elif parcelas == 3:
     juros = 0.10

    elif parcelas == 6:
     juros = 0.15

    elif parcelas == 12:
     juros = 0.20

    juros = divida * juros
    valor_parcelado = (divida + juros) / parcelas
    print('Dívida  :{0:.2f}')
    print("Juros  :")