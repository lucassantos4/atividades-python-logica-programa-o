def eh_primo(numero):
    return numero > 1 and all(numero % i != 0 for i in
                              range(2, int(numero**0.5) + 1))


if __name__ == "__main__":
    numero = int(input("Digite um número: "))
    if eh_primo(numero):
        print(f"O número {numero} é primo.")
    else:
        print(f"O número {numero} não é primo.")
