# ADIÇÃO +
# SUBTRAÇÃO -
# MULTIPLICAÇÃO *
# DIVISÃO /
# DIVISÃO INTEIRA // (é o quociente da divisão, o resultado sem o resto)
# RESTO DA DIVISÃO % (é o que sobra da divisão)
# EXPONENCIAÇÃO ** (potência)


## ORDEM DE PRECEDÊNCIA
# 1. () 
# 2. **
# 3. *, /, //, %
# 4. +, -

## EXEMPLOS
# 1. 2 + 3 * 5 = 17
# 2. (2 + 3) * 5 = 25 
# 3. 2 ** 3 * 5 = 40
# 4. 2 ** (3 * 5) = 32768
# 5. 2 + 3 * 5 ** 2 = 77
# 6. 2 + 3 * 5 ** 2 / 4 = 20.25

# CALCULADORA DE EXEMPLOS
5+2 == 7
5-2 == 3
5*2 == 10
5/2 == 2.5
5//2 == 2
5%2 == 1
5**2 == 25

#CALCULADORA DE EXEMPLOS COM ORDEM DE PRECEDÊNCIA
2 + 3 * 5 == 17 # 3 * 5 é calculado primeiro, depois a adição
(2 + 3) * 5 == 25 # 2 + 3 é calculado primeiro, depois a multiplicação
2 ** 3 * 5 == 40 # 2 ** 3 é calculado primeiro, depois a multiplicação
2 ** (3 * 5) == 32768 # 3 * 5 é calculado primeiro, depois a exponenciação
2 + 3 * 5 ** 2 == 77  # 5 ** 2 é calculado primeiro, depois a multiplicação, e por último a adição