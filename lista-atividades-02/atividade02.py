"""
Crie um programa que receba 5 números e exiba a lista na ordem inversa.
"""

lista = []

for i in range(5):
    numero = int(input("Digite um numero: "))
    lista.append(numero)

lista.reverse()
print(lista)
