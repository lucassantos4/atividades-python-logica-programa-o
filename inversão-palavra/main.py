"""
4. Escreva uma função inverter_palavra que receba uma string e retorne ela
invertida sem usar [::-1]. Em seguida, crie uma função eh_palindromo que
use inverter_palavra para verificar se uma palavra é um palíndromo.
"""


def inverter_palavra(palavra):
    palavrainvertida = "".join(reversed(palavra))
    return palavrainvertida


def eh_palidromo(palavra):
    palavra = palavra.lower().replace(" ", "")
    return palavra == inverter_palavra(palavra)


if __name__ == "__main__":
    palavra = input("Digite uma palavra: ")
    resultado = inverter_palavra(palavra)
    print(f"A palavra '{palavra}' invertida é '{resultado}'.")
    if eh_palidromo(palavra):
        print(f"A palavra'{palavra}' é um palíndromo.")
    else:
        print(f"A palavra '{palavra}' não é um palíndromo.")
