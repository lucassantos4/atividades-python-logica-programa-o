"""
Receba uma lista de 6 números (positivos e negativos) do usuário.
Crie uma nova lista contendo apenas os números positivos.
"""

lista = []
for i in range(6):
    numero = int(input("Digite numeros negativos e positivos: "))
    if (numero < 0):
        numero = numero * (-1)
    lista.append(numero)

print("Sua lista, mas todos numeros ficaram positivos", lista)
