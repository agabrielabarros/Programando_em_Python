#TIPOS PRIMITIVOS
algo = input ('Digite algo: ') # algo recebe input do usuário
print ('O tipo primitivo desse valor é', type(algo)) # printa o tipo de algo
print ('Só tem espaços?', algo.isspace()) # printa se algo é espaço
print ('É um número?', algo.isnumeric()) # printa se algo é número
print ('É alfabético?', algo.isalpha()) # printa se algo é alfabético
print ('É alfanumérico?', algo.isalnum()) # printa se algo é alfanumérico
print ('Está em maiúsculas?', algo.isupper()) # printa se algo está em maiúsculas
print ('Está em minúsculas?', algo.islower()) # printa se algo está em minúsculas
print ('Está capitalizada?', algo.istitle()) # printa se algo está capitalizada (primeira letra maiúscula e as demais minúsculas)
