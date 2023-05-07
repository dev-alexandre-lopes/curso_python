'''
Aula 08 - f-strings

F-strings foram criados para facilitar a formatação de strings.

Também chamadas de “strings literais formatadas” (formatted string literals), 

f-strings são strings com a letra f no início e chaves {} para realizar a interpolação de expressões.

As expressões são processadas em tempo de execução e formatadas utilizadas o protocolo __format__.

'''

#Exemplo de f-strings básico:

nome = 'Python'

print(f"Qual a melhor linguagem de programção? {nome}!\n")

#Mais um exemplo:

import math

x = 30

print(f'sin({x}) = {math.sin(x)}')

#Também é possível acessar dicionários dentro de f-strings:

dicionario = dict({'nome': 'Carlos', 'ocupacao': 'Machine Learning Engineer'})

print(f"{dicionario['nome']} é um {dicionario['ocupacao']}")

#Também podemos criar f-strings multilinha:

site = 'www.python.org'
titulo = 'Python'
curso = 'Básico'

print(
  f"Site: {site}\n"
  f"Título: {titulo}\n"
  f"Curso: {curso}"
)
