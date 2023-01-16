"""
Author: Lucas Queiroz
*** DESAFIO 01 ***
Faça um programa que preencha um vetor com 6 valores distintos digitados pelo usuário.
Em seguida, exiba o maior e o menor valor do vetor, indicando em qual posição eles se encontram.
Depois, imprima os itens no vetor em ordem crescente.
"""

vetor = []
n = 6
pos = 0

while (pos != n):
  num = input(f"Digite um valor inteiro da posição {pos}: ")
  try:
    numInt = int(num)
    if numInt in vetor:
        print(f"Número {numInt} já informado!")
        continue
    vetor.append(numInt)
    pos = pos + 1
  except ValueError:
    print("Digite um número inteiro!")


print(f'\nVetor original: {vetor}')

maxValue = max(vetor)
minValue = min(vetor)

maxValueIndex = vetor.index(maxValue)
minValueIndex = vetor.index(minValue)

print(f'O maior valor é {maxValue} na posição {maxValueIndex}')
print(f'O menor valor é {minValue} na posição {minValueIndex}')

print(f'Vetor em ordem crescente: {sorted(vetor)}')
