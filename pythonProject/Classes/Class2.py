class Produto:
    def __init__(self, codproduto, nome, descricao, tamanho, preco):
        self.codproduto = codproduto
        self.nome = nome
        self.descricao = descricao
        self.tamanho = tamanho
        self.preco = preco

    def caldesconto(self, precomedio):
        calcular = self.preco - (precomedio * 10/100)
        print(f"Preco: {self.preco} Desconto de:  {calcular}")


produto1 = Produto("047121547867", "Bala de Morango", "Açúcar, Xarope de Glicose", "3cm", 2.50)
produto2 = Produto("024585159854", "Bala de Uva", "Açúcar, Xarope de Glicose", "3cm", 2.5)
produto3 = Produto("208451101554", "Salgado de Frango", "Frango, massa, orégano", "9cm", 3.8)

print("Codproduto:", produto1.codproduto, "Nome:", produto1.nome, "Descrição:", produto1.descricao, "Tamanho:", produto1.tamanho, "Preço:", produto1.preco)
print("Codproduto:", produto2.codproduto, "Nome:", produto2.nome, "Descrição:", produto2.descricao, "Tamanho:", produto2.tamanho, "Preço:", produto2.preco)
print("Codproduto:", produto3.codproduto, "Nome:", produto3.nome, "Descrição:", produto3.descricao, "Tamanho:", produto3.tamanho, "Preço:", produto3.preco)

produto1.caldesconto(produto1.preco)
produto2.caldesconto(produto2.preco)
produto3.caldesconto(produto3.preco)