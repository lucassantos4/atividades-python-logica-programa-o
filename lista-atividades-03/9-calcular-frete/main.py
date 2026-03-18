"""
9.
Crie uma função calcular_frete que receba o peso de um pacote
(em kg) e a distância (em km) e retorne o valor do frete com base
nas regras abaixo. Na main, leia os dados e exiba o valor calculado.
"""


def calcular_frete(peso, distancia):

    valorPorKm = 0
    if peso < 0 or distancia < 0:
        return "Valor inválido"
    elif peso < 1:
        valorPorKm = 10
    elif peso >= 1 and peso < 5:
        valorPorKm = 18
    elif peso >= 5:
        valorPorKm = 30

    total = distancia * valorPorKm

    if distancia >= 100:
        total += distancia * 0.5

    return total


if __name__ == "__main__":

    print(calcular_frete(100, 100))
