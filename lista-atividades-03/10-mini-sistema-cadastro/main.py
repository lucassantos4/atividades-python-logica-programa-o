"""
10. Crie um mini sistema de cadastro com as funções cadastrar_usuario,
buscar_usuario e listar_usuarios, todas operando sobre uma lista de
dicionários. A main deve exibir um menu de opções e chamar a função
correspondente à escolha do usuário em um loop até que ele decida sair.
"""


def cadastrar_usuario(usuarios):
    print("\n--- Cadastro de Usuário ---")
    nome = input("Nome: ")
    email = input("Email: ")
    usuario = {"nome": nome, "email": email}
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!\n")


def buscar_usuario(usuarios):
    print("\n--- Buscar Usuário ---")
    buscador = input("Digite o nome ou email para buscar: ")
    encontrados = [u for u in usuarios if buscador.lower(
    ) in u["nome"].lower() or buscador.lower() in u["email"].lower()]
    if encontrados:
        print("Usuários encontrados:")
        for u in encontrados:
            print(f"Nome: {u['nome']}, Email: {u['email']}")
    else:
        print("Nenhum usuário encontrado.")
    print()


def listar_usuarios(usuarios):
    print("\n--- Lista de Usuários ---")
    if usuarios:
        for i, u in enumerate(usuarios, 1):
            print(f"{i}. Nome: {u['nome']}, Email: {u['email']}")
    else:
        print("Nenhum usuário cadastrado.")
    print()


def main():
    usuarios = []
    while True:
        print("Menu:")
        print("1. Cadastrar usuário")
        print("2. Buscar usuário")
        print("3. Listar usuários")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            cadastrar_usuario(usuarios)
        elif opcao == "2":
            buscar_usuario(usuarios)
        elif opcao == "3":
            listar_usuarios(usuarios)
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")


if __name__ == "__main__":
    main()
