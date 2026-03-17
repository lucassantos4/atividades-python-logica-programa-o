import random


def sort_de_palavra():
    lista_sort = [
        "python", "javascript", "typescript", "kotlin", "swift", "csharp",
        "php", "rust", "assembly", "estagiario", "gambiarra", "deploy",
        "refatorar", "depurar", "sprint", "reuniao", "feedback", "burnout",
        "coffee-break", "produtividade", "documentacao", "legado", "bug",
        "feature", "algoritmo", "variavel", "heranca", "polimorfismo",
        "encapsulamento", "backend", "frontend", "fullstack", "banco-de-dados",
        "servidor", "middleware", "framework", "biblioteca", "recursividade",
        "compilador", "interpretador", "sintaxe", "imutabilidade"
    ]
    return random.choice(lista_sort)


def forca(palavra_secreta):
    palavra_secreta = palavra_secreta.lower()
    letras_descobertas = ["_" for _ in palavra_secreta]
    tentativas = 6
    letras_tentativas = []

    print("jogo da forca!")
    while tentativas > 0 and "_" in letras_descobertas:
        print(f"\nPalavra: {' '.join(letras_descobertas)}")
        print(f"tentativas restantes: {tentativas}")
        print(f"letras erradas: {', '.join(letras_tentativas)}")

        chute = input("Digite uma letra: ").lower().strip()

        if len(chute) != 1 or not chute.isalpha():
            print("Por favor, digite apenas uma letra.")
            continue

        if chute in letras_tentativas:
            print(f"ja tentou essa letra' {chute}'")

        letras_tentativas.append(chute)

        if chute in palavra_secreta:
            print(f"a letra '{chute}' ta certa!")
            for i in range(len(palavra_secreta)):

                if palavra_secreta[i] == chute:
                    letras_descobertas[i] = chute

        else:
            tentativas -= 1
            print(f"\nIncorreto. '{chute}' não existe")

    if "_" not in letras_descobertas:
        print(f"\n voce venceu. palavra: '{palavra_secreta}'")
    else:
        print(f"\nVoce perdeu. palavra era '{palavra_secreta}'")
