def questao3():
  perguntas = [
    'a) 1, 3, 5, 7, ___',
    'b) 2, 4, 8, 16, 32, 64, ____',
    'c) 0, 1, 4, 9, 16, 25, 36, ____',
    'd) 4, 16, 36, 64, ____',
    'e) 1, 1, 2, 3, 5, 8, ____',
    'f) 2,10, 12, 16, 17, 18, 19, ____',
  ]
  respostas = [
    'RESP: 1, 3, 5, 7, 9 -> Regra = n + 2',
    'RESP: 2, 4, 8, 16, 32, 64, 128 -> Regra = 2^n',
    'RESP: 0, 1, 4, 9, 16, 25, 36, 49 -> Regra = o intervalo entre os números é o ímpar sucessor',
    'RESP: 4, 16, 36, 64, 100 -> Regra = n² onde n é par',
    'RESP: 1, 1, 2, 3, 5, 8, 13 -> Regra = Sequência de Fibonacci',
    'RESP: 2,10, 12, 16, 17, 18, 19, 200 -> Regra = números que começam com D em sequência'
  ]
  quantidadePerguntas = len(perguntas) - 1
  for cont in range(quantidadePerguntas):
     print(f'{perguntas[cont]}\n{respostas[cont]}\n')
