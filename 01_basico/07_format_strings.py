'''
Aula 07 - Format String

Como aprendemos que não podemos combinar strings e números como este:

age = 36
txt = "My name is John, I am " + age
print(txt) 

Mas podemos combinar strings e números usando o método format ()!

O método format () pega os argumentos passados, formata-os e os coloca na string onde os marcadores de posição {} são:

'''
# Utilizando o {}
idade = 38
txt = 'Carlos tem {} anos de idade'
print (txt.format(idade)) 

# O método format () aceita um número ilimitado de argumentos e são colocados nos respectivos marcadores de posição:
nome = 'Luiz'
idade2 = 38
altura = 1.70
peso = 80
imc = peso//altura**2
print(f'{nome} tem {idade2} anos de idade e seu imc é {imc}')# Utilizando F-Strings
print('{} tem {} anos de idade e seu imc é {}'.format(nome, idade2, imc))