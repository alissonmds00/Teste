def questao1():
  indice = 13
  soma = 0
  k = 0
  while (k < indice - 1):
    k = k + 1
    soma = soma + k
  print(f'O resultado é: {soma}')
  return True

"""
Iteração ocorre 12 vezes (indice - 1) -> 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 = 78
RESP = 78 
"""