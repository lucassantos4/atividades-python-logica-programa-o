"""
Lista Intercalada
Peça ao usuário duas listas com 5 números cada. Crie uma terceira lista
intercalando os elementos das duas.
Exemplo:
Lista A: [1, 3, 5]
Lista B: [2, 4, 6]
Resultado: [1, 2, 3, 4, 5, 6]
"""

lista1 = []
lista2 = []
lista3 = []
for i in range(4):
    valor = int(input("Digite valores para primeira lista "))
    lista1.append(valor)

for i in range(4):
    valor = int(input("Digite valores para segunda lista "))
    lista2.append(valor)

for i in range(4):
    valor = lista1[i]
    lista3.append(valor)
    valor = lista2[i]
    lista3.append(valor)

print("Sua lista intercalada ficou assim : " + lista3)
