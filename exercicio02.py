"""
Author: Lucas Queiroz
*** DESAFIO 02 ***
Escreva um programa que, dada uma matrix 3x3, armazena em cada posição da matriz, a soma dos valores da linha e coluna que definem a posição. Por exemplo, na posição [1][2] você deverá armazenar o valor 1+2 = 3 e assim por diante. Imprima a matriz na tela.
"""

n = 3
m = 3

mat = [[i + j for i in range(m)] for j in range(n)]

print('Matriz')
[print(*line) for line in mat]
