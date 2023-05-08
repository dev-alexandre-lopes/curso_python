'''
Aula 10 - Condições com IF, ELIF e ELSE

Python suporta as condições lógicas usuais da matemática: 

-> Igual a: a == b 
-> Diferentes: a != b 
-> Menor que: a < b 
-> Menor ou igual a: a <= b 
-> Maior que: a > b 
-> Maior ou igual a: a >= b 

Essas condições podem ser usadas de várias maneiras, mais comumente em "instruções if" e loops. 
Uma "instrução if" é escrita usando a palavra-chave if.

elif:

A palavra-chave elif é a maneira de Python dizer: 
"se as condições anteriores não forem verdadeiras, tente esta condição".

else:
A palavra-chave else captura qualquer coisa que não seja capturada pelas condições anteriores.

AND 
A palavra-chave and é um operador lógico e é usado para combinar declarações condicionais.

OR 
A palavra-chave or é um operador lógico e é usado para combinar instruções condicionais.

NOT 
A palavra-chave not é um operador lógico e é usado para inverter o resultado da instrução condicional.

PASS 
As instruções if não podem estar vazias, mas se por algum motivo você tiver uma instrução if 
sem conteúdo, coloque a instrução pass para evitar erros.
'''

# Exemplo utilizando somente o if:
a = 33
b = 200
if b > a:
  print("b é menor do que a")
  
# Exemplo de elif:
a = 33
b = 33
if b > a:
  print("b é maior do que a")
elif a == b:
  print("a e b são iguais")

#Exemplo de else:
a = 200
b = 33
if b > a:
  print("b é maior do que a")
elif a == b:
  print("a e b são iguais")
else:
  print("a é maior do que b")
  
#Exemplo em uma única linha:
a = 330
b = 630
print("A") if a > b else print("=") if a == b else print("B")

#Exemplo de teste de duas condições verdadeiras com o AND:
a = 200
b = 3300
c = 500
if a > b and c > a:
  print("Ambas condições são verdadeiras")
else:
  print("Uma condição é falsa")
  
#Exemplo de tests com pelo menos uma condição verdadeira com o OR:
a = 200
b = 33
c = 500
if a > b or a > c:
  print("Pelo menos uma condição é verdadeira")
else:
  print("As duas condições são falsas")
  
#Exemplo do uso do NOT:
a = 33
b = 200
if not a > b:
  print("a não é maior do que b")
  
#Exemplo do uso do PASS:
a = 33
b = 200

if b > a:
  pass

#Exemplo com vários testes condicionais:
condicao1 = False
condicao2 = False
condicao3 = False
condicao4 = False

if condicao1:
    print('Código para condição 1')
    print('Código para condição 1')
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else:
    print('Nenhuma condição foi satisfeita.')

if 10 == 10:
    print('Outro if')

print('Fora do if') 