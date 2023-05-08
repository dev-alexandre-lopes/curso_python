'''
Exercício 01:

* Criar variáveis para nome (str), idade (int), altura (float) e peso (float) de uma pessoa;
* Criar variável com o ano atual
* Obter o ano de nascimento da pessoa
* Obter o IMC da pessoa com 2 casas decimais
* Exibir um texto com todos os valores na tela utilizando F-strings 
'''

nome = 'Paulo'
idade = 38
altura = 1.70
peso = 80.0
ano_atual = 2020
imc = peso//(altura ** 2) # Cálculo do IMC
ano_nasc = ano_atual - idade # Cálculo do ano de nascimento
print (nome, type(nome))
print (idade, type(idade))
print (altura, type(altura))
print (peso, type(peso))
print(f'{nome} tem {idade} anos de idade, {altura} de altura e pesa {peso}Kg.')
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {ano_nasc}.')