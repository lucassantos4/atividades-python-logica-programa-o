"""
Peça ao usuário para digitar uma lista de 10 nomes.
Em seguida, pergunte qual nome ele deseja procurar
e diga se o nome está ou não na lista.
"""

lista = []

for i in range(10):
    nome = str(input("Digite um nome: "))
    lista.append(nome)

print(lista)
percorrer = int(input("Qual numero do item quer da lista? "))
print(lista[percorrer])
