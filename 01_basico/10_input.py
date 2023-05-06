'''
Aula 09 - Input (Entrada de Dados do Usuário)

'''
'''
# Exemplo de aplicação com input:
nome = input ("Qual o seu nome ? ")
idade = input( "Qual a sua idade? ")
ano_nascimento = 2021 - int(idade)
print (f'{nome} tem {idade} anos. {nome} nasceu em {ano_nascimento}')
'''
# Exemplo de cálculo:

numero1 = int(input("Digite o número 1: "))
numero2 = int(input("Digite o número 2: "))
resultado = numero1 ** numero2
print(f'O resultado da operação é: {resultado}')