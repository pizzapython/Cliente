pessoas = [
    {"nome": "João", "idade":25},
    {"nome": "Maria", "idade":30},
    {"nome": "Pedro", "idade":28},
    {"nome": "Ana", "idade":22},
]

for pessoa in pessoas:
    nome = pessoa["nome"]
    idade = pessoa["idade"]
    print(f"Nome: {nome},Idade: {idade}")