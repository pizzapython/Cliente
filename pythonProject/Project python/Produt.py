def money(produtos):

    for produto in lista:
        nome = produto["produto"]
    marca = produto["marca"]
    print(f"Produto: {nome}, Marca: {marca}")


lista = [
{"produto": "tv 50 polegadas" , "marca": "Samsung"},
{"produto": "micro-ondas 10 litros", "marca": "Panasonic"},
{"produto": "Iphone 15 pro max", "marca": "Apple"},
{"produto": "smartphone redmi note 13", "marca": "Xiaomi"},
{"produto": "lavadora 10 kg", "marca": "Brastemp"}
]
money(lista)