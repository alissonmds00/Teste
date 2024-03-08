def questao5(string=None):
  res = '' 
  #Valor que irá armazenar os caracteres da string
  if string == None:
      #Caso não seja definida a string durante o callback da função
      string = input('Digite a frase que deseja inverter: ')
  for posCaracter in range(len(string)-1, -1, -1):
     #"Varre" a string de trás para a frente. 
     res += f'{string[posCaracter]}'
     #Acumula cada caracter da string e no final retorna o resultado
  return res
      