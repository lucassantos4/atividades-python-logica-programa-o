"""
1. Crie uma função chamada contar_vogais que receba uma string
 e retorne a quantidade de vogais encontradas.
Na main, peça uma frase ao usuário e exiba o resultado.
"""


def ordenar_vogais(palavra):
    vogais = ['a', 'e', 'i', 'o', 'u']
    quantidade_vogais = 0
    for letra in palavra:
        if letra.lower() in vogais:
            quantidade_vogais += 1
    return quantidade_vogais


if __name__ == "__main__":

    palavra = input("Digite uma palavra: ")
    resultado = ordenar_vogais(palavra)
    print(f"A palavra '{palavra}' tem {resultado} vogais.")
