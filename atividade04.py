"""
Implemente um programa com o seguinte menu:
1 - Adicionar item
2 - Remover item
3 - Mostrar lista
4 - Sair
Use uma lista para armazenar os itens.
O programa deve continuar até que o usuário escolha a opção 4.
"""


lista = []

print("""
1 - Adicionar item
2 - Remover item
3 - Mostrar lista
4 - Sair
""")

while True:
    selec = int(input("Escolha uma opção: "))

    if (selec < 1 or selec > 4):
        print("Digite um valor valido.")
    elif (selec == 1):
        item = input("Oque deseja adicionar? ")
        lista.append(item)
    elif (selec == 2):
        item = int(input("Qual o valor do item que deseja remover?"))
        lista.pop(item)
    elif (selec == 3):
        print(lista)
    else:
        break
