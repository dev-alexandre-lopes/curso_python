'''
Aula 03 - Strings são dados primitivos em Python

str - string

Strings - São cadeias de caracteres (textos) que estão entre aspas, a leitura do interpretador é da esquerda para direita de cima para baixo;

'''
#Uso das aspas simples

print('Exemplo de String')

print ('123456')

#Uso das aspas duplas

print("Joãozinho")

# Utilizando separadore sep =  e end =

print(2, "Joãozinho", sep='-', end='!\n')

print ("Jogador de futebol!!\n")

print ('Uso da aspas duplas dentro do texto "É dessa forma" ok!\n')

# Uso do r

print (r"Essa é um texto com \n (str)\n") # Colocando a letra r antes das aspas duplas tudo que é \n ou outro é desconsiderado dentro

# Atribuindo múltiplas strigs a uma variável e pulando linha no final usando aspas dulplas

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a,'\n')

# Strigns são arrays e pode ser acessados por elementos

b = 'Python é uma linguagem de programação!'
print (b[2]) # letra t
print (b[13]) # letra l

# Exemplo de Loop dentro da String para imprimir as letras

'''for x in b:
    print (x)
'''

# Verificar o tamanho de uma string:

print (len(b)) # resposta = 38

# Fazendo o check se está na string 

txt = "Hoje é um dia chuvoso no Brasil!"

print ('chuvoso' in txt,'\n') # resposta = True

# Fazendo o check se está na string com if

if 'chuvoso' in txt:
    print ('chuvoso está no texto!\n')
    
# Fazendo o teste se não está na string

print ('Ar' not in txt) # resposta = true
print ('Hoje'not in txt) # resposta = false

# Fazendo o teste se não está com if na string

if 'Ar' not in txt:
    print ('A palavra Ar não está no texto!')
    
    
