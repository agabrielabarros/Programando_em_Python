# INPUT E OUTPUT
nome = input ('Qual é o seu nome? ') # nome recebe input da "= (recebe)"
idade = input ('Qual é sua idade? ')
print ('Boas vindas', nome, end='')  # printa boas vindas e o nome do usuário o end='' faz com que o print não pule linha
print ('! Tudo bem com você?') # printa a idade do usuário
print ('Você tem', idade, 'anos!') # printa a idade do usuário;


#CONCATENAÇÃO E NÃO SOMA DOS NÚMEROS - Sem conversão para inteiro
n1 = input ('Digite um número: ') # n1 recebe input do usuário
n2 = input ('Digite outro número: ') # n2 recebe input do usuário
soma = n1 + n2 # soma recebe a soma de n1 e n2
print ('A UNIÃO entre', n1, 'e', n2, 'é igual a', soma) # printa a soma de n1 e n2;


#CONVERTENDO O INPUT PARA INTEIRO 
n1 = int(input('Digite um número: ')) # n1 recebe input do usuário
n2 = int(input('Digite outro número: ')) # n2 recebe input do usuário
soma = n1 + n2 # soma recebe a soma de n1 e n2
print ('A soma entre', n1, 'e', n2, 'é igual a', soma) # printa a soma de n1 e n2;

#OUTRA FORMA DE CONVERTER O INPUT PARA INTEIRO
n1 = input ('Digite um número: ') # n1 recebe input do usuário
n2 = input ('Digite outro número: ') # n2 recebe input do usuário
soma = int(n1) + int(n2) # soma recebe a soma de n1 e n2
print ('A soma entre', n1, 'e', n2, 'é igual a', soma) # printa a soma de n1 e n2
print ('A soma vale,', soma) # printa a soma de n1 e n2; #outra forma de printar a soma de n1 e n2; 

#FORMA MAIS SIMPLES DE CONVERTER O INPUT PARA INTEIRO
n1 = int(input('Digite um número: ')) # n1 recebe input do usuário
n2 = int(input('Digite outro número: ')) # n2 recebe input do usuário
print ('A soma vale {}'.format(n1+n2)) # printa a soma de n1 e n2
print ('A soma entre {} e {} vale {}'.format(n1, n2, n1+n2)) # printa a soma de n1 e n2 eu informo dentro dos parenteses o que quero que apareça no lugar das chaves {};

