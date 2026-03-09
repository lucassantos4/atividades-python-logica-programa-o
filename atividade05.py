"""
Peça ao usuário para digitar 10 números e armazene-os em uma lista.
Depois, peça um número extra e diga quantas vezes ele aparece na lista.
"""

lista = []

for i in range(10):
    numero = int(input("Digite um numero: "))
    lista.append(numero)

print(lista)

extranumero = int(input("Digite mais um numero: "))
print(lista.count(extranumero))
