"""
Aula 12 - Operadores Lógicos

Operadores lógicos são ferramentas importantes em programação que nos permitem combinar valores 
booleanos (True/False) para formar expressões mais complexas. Em Python, existem três operadores 
lógicos principais: "and", "or" e "not".

O operador "and" retorna True se ambos os valores comparados forem True, caso contrário, retorna False.

O operador "or" retorna True se pelo menos um dos valores comparados for True, caso contrário, 
retorna False. 

O operador "not" inverte o valor booleano, retornando True se o valor original era False e False 
se o valor original era True.

"""
# Exemplo de código:

# Operador "and"
x = 5
y = 10
z = 15

if x < y and z > y:
    print("Ambas as condições são verdadeiras")
else:
    print("Pelo menos uma das condições é falsa")

# Operador "or"
x = 5
y = 10
z = 15

if x > y or z > y:
    print("Pelo menos uma das condições é verdadeira")
else:
    print("Ambas as condições são falsas")

# Operador "not"
x = True

if not x:
    print("O valor original era verdadeiro, mas agora é falso")
else:
    print("O valor original era falso, mas agora é verdadeiro")

# Projeto 1: Verificar se um número é par ou ímpar:

def eh_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

num = int(input("Digite um número inteiro: "))

if eh_par(num):
    print(f"{num} é um número par")
else:
    print(f"{num} é um número ímpar")


# Projeto 2: Verificação de Senha:

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
     print('Entrar')
else:
     print('Sair')
 