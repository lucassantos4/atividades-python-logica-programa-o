"""
2. Escreva uma função calcular_imc que receba peso e altura e retorne o IMC
 calculado.Crie uma segunda função classificar_imc que receba o valor do IMC
e retorne a classificação
("Abaixo do peso", "Normal", "Sobrepeso" ou "Obesidade").
Use a main para orquestrar as chamadas.
"""


def calcular_imc(peso, altura):

    imc = peso / (altura ** 2)
    return imc


def classificar_imc(imc):
    if imc < 0:
        return "IMC inválido. "
    elif imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"


if __name__ == "__main__":

    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em metros: "))
    imc = calcular_imc(peso, altura)
    print(f"Seu IMC é: {imc:.2f}, vocé esta {classificar_imc(imc)}.")
