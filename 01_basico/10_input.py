'''
Aula 09 - User Input (Entrada de Dados do Usuário)

Sempre recebemos uma string da função input!

Precisa fazer a conversão de tipo (typecasting) de dado para realizar uma operação depois!
'''

# Exemplo de aplicação com input:
nome = input ("Qual o seu nome ? ")
idade = input( "Qual a sua idade? ")
ano_nascimento = 2023 - int(idade) # colocar o ano corrente 2023
print (f'{nome} tem {idade} anos. {nome} nasceu em {ano_nascimento}')

# Exemplo de cálculo:

numero1 = int(input("Digite o número 1: "))
numero2 = int(input("Digite o número 2: "))
resultado = numero1 ** numero2
print(f'O resultado da operação é: {resultado}')