"""
Author: Lucas Queiroz
*** DESAFIO 03 ***
Escreva um programa que lê 2 matrizes A e B, cada uma com 3 linhas e 2 colunas. Construir uma matriz C de mesma dimensão (3x2) onde C é formada pela soma dos elementos da matriz A com os elementos da matriz B (exemplo: C[1][1] = A[1][1] + B[1][1]). Apresentar ao final as 3 matrizes (A, B e C).
"""

def preencheMatriz(n, m):
  mat = [[0 for j in range(m)] for i in range(n)]
  for i in range(n):
    for j in range(m):
        mat[i][j] = int(input(f"Digite o valor do elemento na linha {i} e coluna {j}: "))

  return mat

def exibeMatriz(mat):
    [print(*line) for line in mat]


lin = 3
col = 2

print("Preencha a matriz A")
matA = preencheMatriz(lin, col)

print("Preencha a matriz B")
matB = preencheMatriz(lin, col)

matC = [[matA[i][j] + matB[i][j] for j in range(col)] for i in range(lin)]

print("Matriz A:")
exibeMatriz(matA)
print("Matriz B:")
exibeMatriz(matB)
print("Matriz C:")
exibeMatriz(matC)

