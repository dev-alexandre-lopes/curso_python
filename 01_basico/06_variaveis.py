'''
Aula 06  - Variáveis

Iniciar com Letras, pode conter números, separar _, letras minúsculas

'''
nome = 'Luiz'
idade = 38
altura = 1.70
peso = 80
e_maior = idade > 18
imc = peso//(altura ** 2) # Operação de potenciação
print ('Nome:', nome)
print ('Idade:', idade)
print ('Altura:', altura)
print ('É maior:', e_maior)
print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc}')