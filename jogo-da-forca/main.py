"""
6. Escreva uma função forca que receba uma palavra secreta e gerencie
uma rodada do jogo da forca: peça letras ao usuário, revele as posições
corretas e encerre quando a palavra for descoberta ou após 6 erros.
"""
from forca import forca, sort_de_palavra


if __name__ == "__main__":
    forca(sort_de_palavra())
