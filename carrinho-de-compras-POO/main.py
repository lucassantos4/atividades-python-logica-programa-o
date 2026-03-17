"""
5. Crie uma função calcular_desconto que receba o preço de um produto e
o percentual de desconto, e retorne o preço final. Na main, simule um
carrinho com 3 produtos diferentes, aplique descontos distintos em
cada um e exiba o total a pagar.
"""


class Produto:

    def __init__(self, nome, preco):

        self.nome = nome
        self.preco = preco

    def calcular_desconto(self, percentual):

        desconto = self.preco * (percentual / 100)
        return self.preco - desconto


class CarrinhoDeCompras:

    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)


if __name__ == "__main__":

    produto1 = Produto(input("Digite o nome do produto: "), float(
        input("Digite o preço do produto: ")))
    produto2 = Produto(input("Digite o nome do produto: "), float(
        input("Digite o preço do produto: ")))
    produto3 = Produto(input("Digite o nome do produto: "), float(
        input("Digite o preço do produto: ")))

    CarrinhoDeCompras = CarrinhoDeCompras()
    CarrinhoDeCompras.adicionar_produto(produto1)
    CarrinhoDeCompras.adicionar_produto(produto2)
    CarrinhoDeCompras.adicionar_produto(produto3)

    print(f"O preço do produto {produto1.nome} com desconto é: R${
        produto1.calcular_desconto(10):.2f}")
    print(f"O preço do produto {produto2.nome} com desconto é: R${
        produto2.calcular_desconto(35):.2f}")
    print(f"O preço do produto {produto3.nome} com desconto é: R${
        produto3.calcular_desconto(15):.2f}")

    print("Produtos no carrinho:")
    for produto in CarrinhoDeCompras.produtos:
        print(f"- {produto.nome}: R${produto.preco:.2f}")
