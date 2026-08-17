nome = input('Qual é o seu nome? ')
print(f'Olá {nome}, seja bem-vindo(a) a lista de exercícios! \n' ); #\n serve para pular uma linha

# Exercício 1: Faça um programa que peça dois números e imprima a soma, subtração, multiplicação, divisão e potência dos dois números.
n1 = float (input('EXERCÍCIO 1: Digite o primeiro número: '))
n2 = float (input ('Digite o segundo número: '))
s = n1 + n2 
m = n1 * n2
d = n1 / n2
e = n1 ** n2
print ('A soma é {}, o produto da multiplicação é {}, a divisão é {} e a potência é {} \n'.format(s, m, d, e));

#Exercício 2: Faça um programa que peça a temperatura em graus Celsius e converta para graus Fahrenheit.
c = float (input ('EXERCÍCIO 2: Informe a temperatura em graus celsius: '))
f = (c * 9/5) + 32
print ('A temperatura de {} ºC corresponde a {} ºF \n'.format(c, f));

#Exercício 3: Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
x = int (input ('EXERCÍCIO 3: Digite um número inteiro: '))
ant = x -1
suc = x +1
print ('O antecessor de {} é {} e o seu sucessor é {} \n'.format(x, ant, suc));


# Exercício 4: Faça um programa que leia um número e mostre o seu dobro, triplo e raiz quadrada.
y = float (input ('EXERCÍCIO 4: Digite um número:'))
d = y*2
t = y*3
r = y**2
print ('O dobro do número {} é {}, o triplo é {} e a raíz quadrada é {} \n'.format(y, d, t, r));

# Exercício 5: Faça um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
n1 = float (input ('EXERCÍCIO 5: Digite a primeira nota: '))
n2 = float (input ('Digite a segunda nota: '))
m = (n1 + n2) / 2
print ('A média do aluno é {} \n'.format(m));

#Exercício 6: Faça um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
p = float (input ('EXERCÍCIO 6: Digite o preço do produto: '))
np = p - (p * 5/100)
print ('O preço original do produto é {} e com 5% de desconto fica {} \n'.format(p,np));
           

# Exercício 7: Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária apara pintá-la, sabendo que cada litro de tinta pinta uma área de 2m2
lar = float(input('EXERCÍCIO 7: Informe a largura (m): '))
alt = float(input('Informe a altura (m): '))
area_total = lar * alt
qtd_tinta = area_total / 2

# Usando f-string e limitando a 2 casas decimais (:.2f)
print(
    f'A área total é de {area_total:.2f}m² e você precisará de'
    f' {qtd_tinta:.2f}L de tinta.'
)

#Exercício 8: Faça um programa que leia um número e gere sua taboada
num = int(input('Digite um número para ver sua tabuada: '))

print(f'--- TABUADA DO {num} ---')
for i in range(1, 11):
    print(f'{num} x {i:2} = {num * i}')