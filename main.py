'''1.	Você resolveu fazer um programa que receba números do usuário e os guarde em uma lista. A quantidade de elementos da lista é variável, já que o usuário dirá se deseja parar ao ser questionado. Após receber todos os números do usuário, seu programa mostra a lista completa, a ordenação dos elementos, a soma e a média deles, além do maior e do menor valor inserido. Lembre-se que você utilizou o laço de repetição WHILE.  Escreva o código na caixa indicada.
numeros = []
n=0
while True:
  num = int(input("Digite um número: "))
  numeros.append(num)
  desejo = input("Quer continuar? (sim/não)")
  if desejo == "não":
    break
  if desejo == "sim":
    continue
numeros.sort()
for y in range(len(numeros)):
  contador=n+1
print(contador,"° numero: ",numeros[y])
total = sum(numeros)
print("A soma dos elementos é ",total)
valor = len(numeros)
media = total/valor
print("A média dos elementos é ",media)
´´
2.	Tentando auxiliar seu irmãozinho a aprender o uso da vírgula quando há separação de elementos com a mesma função sintática. Dessa forma, você fez uma função que recebe uma sentença que é separada nas vírgulas. A sentença de teste é a seguinte:
Fui à padaria comprar pão, manteiga, ovos, leite e chocolate.

Frase='Fui à padaria comprar pão, manteiga, ovos, leite e chocolate.'
Lista=Frase.split(',')
print(Lista)

3.Após a atividade de português, você passou a ajudar seu irmão com matemática e, para isso, criou um programa que recebe dois números e, por meio de uma função, faz e mostra a soma, subtração, multiplicação e divisão deles. Invoque a função. Escreva o código na caixa indicada.

n1 = int(input('Primeiro número:')) 
n2 = int(input('Segundo número:'))
def conta(num1,num2): 
 print(num1+num2) 
 print(num1-num2) 
 print(num1*num2) 
 print(num1/num2) 
conta(num1,num2)
''
4.Lembra que nos primórdios da disciplina você fez, ou deveria ter feito, um programa que recebe uma temperatura em graus Celsius e a converte para Fahrenheit? Agora você deverá fazer a conversão de temperatura por meio de uma função. Continue recebendo do usuário o valor em Celsius, passe isso como argumento para a função e exiba o resultado para o usuário e invoque a função. 
''
def f__():
  c=int(input('Digite um número pata fazer a conersão:'))
  f = (c * 9/5) + 32
  print("A temperatura ", c," em Celsius equivale à ", f, " graus Fahrenheit.")
f__()
''
Você fez um programa que recebe um número do usuário e esse é passado como argumento de uma função que testa quais números de 0 ao número informado é par e qual é ímpar. O resultado do teste é exibido para o usuário.
'''
def numero__():
  pares=[]
  impares=[]
  N=int(input('digite um número:'))
  for x in range (0,N):
    if N%2==0:
      pares.append(x)
    else:
      impares.append(x)
  print('a lista de números pares é:',pares)
  print('a lista de números ímpares é:',impares)
numero__()