# Criando variáveis em Python
# nome = conteúdo da variável
# int nome = 10
valora = 10
valorb = 20
resultado = valora+valorb
print("O resultado foi: ", resultado)
valorc = "10"
valord = "20"
resultadonovo = valorc + valord
print("O resultado foi: ", resultadonovo)
#COnvertendo String para inteiro
resultadonovo2 = int(valorc) + int(valord)
print("O resultado foi: ", resultadonovo2)
#Outros conversores: int() = inteiro; float() = números reais, str() = String

#Contando quantidade de caracteres
nome = "Fabio Gomes"
len(nome)
# Deixando a primeira letra maiuscúla
print("Nome")
print(nome2.capitalize())
# Contando um termo dentro do bloco de texto
dados = "SSH (porta de destino 22, protocolo TCP) para a interface de rede eni-1235b8ca123456789 na conta 123456789010foi permitido SSH"
print(dados.count("12"))
# islower ou isupper verifica se é maísculo ou minuscúlo
print(nome2.islower())
print(nome2.isupper())
#Convertendo para maiuscúla ou minuscúla
print(nome2.lower())
print(nome2.upper())
nome = "fabio gomes"
#Converte cada primeira letra para maiuscúla
print(nome.title())
# Transformar um texto - String em uma lista, usando o espaço como forma de quebrar o texto
print(dados.split())
#Substitui o texto da primeira string pela segunda, exemplo gomes pelo rocha
print(nome.replace("gomes", "rocha"))
# Busccando um conteúdo
print(dados.find("56"))
# Remover espaço 
print(dados.strip())
#exibir informação com base no início e fim desejado
print(dados[82:91])
print(dados[82:])
print(dados[:82])


#Trabalhando com operadores
# + = soma, - = subtração, * = multiplicação, / = divisão, // = divisão de numeros resultado inteiro, % = resto da divisão, ** = exponenciação
x = 10
y = 3
#Divisão normal
print(x/y)
#Divisão com resultado inteiro
print(x//y)
# Soma, subtração e multiplicação
print(x+y)
print(x-y)
print(x*y)
# Resto de divisão
print(x%y)
#Exponenciação
print(x**y)
#Calculos abreviados
x = x + 6
print(x)
x += 6
print(x)
# Comparar
print(x > y)
print(x < y)
y= 22
print(x >= y)
print(x <= y)
print(x == y)
y=21
print(x >= y)
print(x <= y)
print(x == y)
print(x != y)
# Outros operadores lógicos
print("Outros operadores")
print(not x != y)
print(x > 10 and y <30)
print(x > 10 and y >30)  
print(x > 10 or y <30)
print(x > 10 or y >30)  


print("Meu nome é: \nFabio Gomes")

x = float(input("Informe o numero 1: "))
y = float(input("Informe o numero 2: "))
print(type(x))
print(type(y))
print(x/y)
#Divisão com resultado inteiro
print(x//y)
# Soma, subtração e multiplicação
print(x+y)
print(x-y)
print(x*y)
# Resto de divisão
print(x%y)
#Exponenciação
print(x**y)



opc = int(input("Digite 1 para soma e 2 para subtração: "))
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
# if = se
if opc == 1:
  print("Soma")
  print("Resultado:")
  print(a+b)
  #elif = else if ou senão se
elif opc == 2:
  print("Subtração")
  print("Resultado:")
  print(a-b)


  var_10 = 10
var10 = 10
Var10 = 13
vAr10 = 12
VaR10 = 11
print(VaR10)
nome_protocolo = "TCP"
nomeProtocolo = "TCP"

#Arredondamento de dados após a virgula
pi = 3.14159265
valor = 10/3
print(round(pi, 3))
print(round(valor, 2))


import time
#Estrutura de repetição
for i in [1, 3, 5, 7, 9]:
  print(i)

#Exemplo de for para exibir textos
for texto in dados.split():
  print(texto)
#Indo de 0 a 10
for n in range(10):
  print(n)
  time.sleep(2)
for n in range(10, 0, -1):
  print(n)
  time.sleep(2)


  x = 0
while x <= 20:
  print(x)
  x +=1
  time.sleep(2)
x = 0
while x <= 20:
  print(x)
  x +=1
  if x == 5:
    print("Five")
  elif x == 10:
    print("Ten")


   for n in range(20, 30, 1):
  print(n)
for n in range(20, 30, 2):
  print(n)


#Listas: Estrutura primitiva do Python que permite armazenar uma coleção de dados
nome_lista = [1, 2, 3, 4, 5, 6]
for n in nome_lista:
  print(n)
print(nome_lista[4])
nome_lista.append(7)
nome_lista.insert(2, 10)
nome_lista.remove(6)
for n in nome_lista:
  print(n)
lista = []
print(len(nome_lista))
nome_lista[0] = 20
#Mudando dados na lista
print('---')
for n in nome_lista:
  print(n)


 # tupla: estrutura de dados primitiva do python, similar a lista, porém imutável
nome_tupla = (1, 2, 3, 4, 5, 6)
for n in nome_tupla:
  print(n)    