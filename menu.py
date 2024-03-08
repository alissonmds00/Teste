from q1 import questao1
from q2 import questao2
from q3 import questao3
from q4 import questao4
from q5 import questao5
from SobreMim import sobreMim

def opcoes():
  print (f'-=-='*5, 'Opções', '-=-='*5)
  print('1- Para visualizar a resolução da questão 1')
  print('2- Para visualizar a resolução da questão 2')
  print('3- Para visualizar a resolução da questão 3')
  print('4- Para visualizar a resolução da questão 4')
  print('5- Para visualizar a resolução da questão 5')
  print('6- Para visualizar as razões pelas quais eu deveria ser contratado por vocês ♥')
  print('-=-=-' * 11)

def capturarEscolha(escolha):
  match escolha:
    case 1:
      return questao1()
    case 2:
      return questao2()
    case 3:
      return questao3()
    case 4:
      return questao4()
    case 5:
      return questao5()
    case 6:
      return sobreMim()


def obterInput():
  resp = input('Escolha um número válido: ')
  return resp

def validarInput():
  resp = obterInput()
  while(not resp.isnumeric() or (int(resp) < 0 or int(resp) > 6)):
    resp = input('O valor digitado não é um número válido: ')
  resp = int(resp)
  capturarEscolha(resp)
  return resp
  

def iniciarMenu():
  while True:
    opcoes()
    resp = validarInput()
    if resp == 0:
      break








