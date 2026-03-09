"""
Substituir Elementos
Peça uma lista de nomes ao usuário. Em seguida, pergunte qual nome ele deseja
substituir e pelo quê. Faça a substituição e mostre a nova lista.

"""

listanome = []

for i in range(5):
    nome = input("Digite os nomes de usuario. ")
    listanome.append(nome)
print(listanome)

nomeselecionado = input("Qual nome deseja remover na lista? ")
posicaoindex = listanome.index(nomeselecionado)
novonome = input("Qual nome deseja substituir na lista? ")
listanome[posicaoindex] = novonome
print(listanome)
