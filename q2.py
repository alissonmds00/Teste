def questao2(alvo=None):
  anterior = 1 #Começa invertido, para a contagem respeitar o 0 e os primeiros dois "1"s da sequência
  atual = 0
  if alvo == None: 
    alvo = input('Informe qual valor você deseja testar na sequência de Fibonacci: ')
  while(not alvo.isnumeric() or int(alvo) < 0):
    alvo = input('O valor digitado não é um número válido. Digite um valor maior ou igual a 0: ')
  alvo = int(alvo) 
  #Transformação para número sem tratamentos de erro
  while (atual <= alvo and atual != alvo): 
    #Enquanto o número atual da contagem de Fibonacci for menor ou igual ao alvo
    #E o atual não for o alvo, então o loop continua gerando outros números da sequência
    atual, anterior = (atual + anterior), (atual)
    #Para não ser necessária uma terceira variável, utilizei a instância das duas variáveis
    #E atribuí a elas respectivamente, Atual passa a ser o valor do somatório do valor atual com anterior, 
    #e "anterior" passa a ter o valor que antes era o atual
  if (atual == alvo or alvo == 0):
    print(f'O número {alvo} está incluso na sequência de Fibonacci')
  else: 
      print(f'O número {alvo} não está incluso na sequência de Fibonacci')
  return True
  #A função para ou quando o valor é encontrado, ou quando o próximo valor é maior que o alvo
  #Então ocorre a verificação