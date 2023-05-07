'''
Aula 05  - Variáveis

Iniciar com Letras, pode conter números, separar _, letras minúsculas

Variáveis são usadas para salvar algo na memória do computador.

PEP8: inicie variáveis com letras minúsculas, pode usar

números e underline _.

O sinal de = é o operador de atribuição. Ele é usado para

atribuir um valor a um nome (variável).

Uso: nome_variavel = expressão

'''

nome = 'Paulo'
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
print(f'{nome} tem {idade} anos de idade e seu imc é {imc}\n')

print(f"{nome}:\n")
print(f"tem {idade} anos de idade\n") 
print(f"E o seu imc é {imc}\n")