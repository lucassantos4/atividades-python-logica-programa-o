"""
8. Escreva uma função analisar_notas que receba uma lista de notas e
retorne um dicionário contendo a média, a maior nota, a menor nota e
a quantidade de aprovados (nota ≥ 7). Exiba cada informação formatada
na main.
"""


def analisar_notas(notas):
    if not notas:
        return dict(media=0, maior=0, menor=0, aprovados=0)

    return dict(media=sum(notas) / len(notas),
                maior=max(notas),
                menor=min(notas),
                aprovados=sum(1 for nota in notas if nota >= 7))


if __name__ == "__main__":

    try:
        quantidadeProvas = int(input("Quantidade provas a corrigir: "))
    except ValueError:
        print("Quantidade inválida")
        quantidadeProvas = 0

    notas = []
    for i in range(quantidadeProvas):
        while True:

            try:
                notasAdicionar = float(input("Digite a nota: "))

                if 0 <= notasAdicionar <= 10:
                    notas.append(notasAdicionar)
                    break
                print("Nota inválida (0 a 10).")
            except ValueError:
                print("Digite numero válido.")

    print(f"{analisar_notas(notas=notas):.2f}")
