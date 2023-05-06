'''
Aula 05 - Operadores Aritméticos

+	Addition        x + y

-	Subtraction     x - y

*	Multiplication  x * y

/	Division        x / y

%	Modulus         x % y

**	Exponentiation	x ** y

//	Floor division  x // y  (Arrendondamento para baixo - Divisão Inteira)

'''
print('\nAdição',2 + 5)

print('Concatenação', '2' + '5')

print ('Subtração', 2 - 4)

print ('Multiplicação', 3 * 7)

print ('Repetição', 3 * '7')

print ('Divisão', 9 / 3)

print ('Módulo', 9 % 2) # Resto da divisão entre 9 e 2

print ('Divisão Inteira', 56.9 // 3) # Resultado seria 18.96666667

print('***********************************************************************************************')

'''
Precedência igual na Matemática:

Assim como aprendemos na matemática, operadores têm uma certa precedência que pode ser alterada usando os parênteses (como descrito na aula anterior).

Abaixo, segue uma lista mais precisa de quais operadores tem maior prioridade na hora de realizar contas mais complexas (de maior para menor precedência).

1) ( n + n ) - Os parênteses têm a maior precedência, contas dentro deles são realizadas primeiro

2) ** - Depois vem a exponenciação

3) * / //  % - Na sequência multiplicação, divisão, divisão inteira e módulo

4) +  -  Por fim, soma e subtração

Contas com operadores de mesma precedência são realizadas da esquerda para a direita.

'''

print (5+2*10)# Resultado esperado 25


print ((5+2)*10)# Resultado esperado 70

# Exemplo de conta:

conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)

print(conta_1)