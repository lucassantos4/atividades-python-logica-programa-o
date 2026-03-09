"""
Solicite uma lista de números ao usuário e depois peça um valor.
Exiba todos os índices em que esse valor aparece.
"""


lista = []

for i in range(6):
    valor = input("Digite valores para lista: ")
    lista.append(valor)

print(lista)
count = (input("Digite o valor que vc quer saber quantas vezes aparece:a "))
print("O valor que quer saber aparece " + lista.count(count) + " vezes.")
