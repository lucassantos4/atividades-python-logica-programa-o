"""
7. Crie uma função converter_temperatura que receba um valor e dois parâmetros
de_unidade e para_unidade (ex: "C", "F", "K"), e retorne o valor convertido.
Trate as combinações possíveis e exiba uma mensagem de erro para conversões
inválidas.
"""


def converter_temperatura(valor, unidade_de, unidade_para):
    unidade_de = unidade_de.upper()
    unidade_para = unidade_para.upper()
    if unidade_de == "C":
        c = valor
    elif unidade_de == "F":
        c = (valor - 32) * 5/9
    elif unidade_de == "K":
        c = valor - 273.15
    else:
        return "Unidade origem inválida."

    if unidade_para == "C":
        return c
    elif unidade_para == "F":
        return (c * 9/5) + 32
    elif unidade_para == "K":
        return c + 273.15
    else:
        return "Unidade destino inválida"


if __name__ == "__main__":

    valor = float(input("Digite o valor da temperatura: "))
    unidade_de = input("Digite a unidade de origem (C, F, K): ")
    unidade_para = input("Digite a unidade de destino (C, F, K): ")
    resultado = converter_temperatura(valor, unidade_de, unidade_para)
    print(f"Resultado: {resultado}")
