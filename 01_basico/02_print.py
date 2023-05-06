'''
Aula 02 - Função print();

A função print() é uma das funções mais importantes e usadas na linguagem Python. 
Sua função é, basicamente, exibir mensagens na tela ou enviá-las para outro dispositivo, como imprimir dentro de arquivos de texto.

No Python 3, print() é uma função interna, de modo que não é necessário importar nenhuma biblioteca para poder utilizá-la. 
Basta chamá-la e passar os argumentos necessários.

Sintaxe:

print(objeto(s), argumentos_de_palavra-chave)

Onde:

objeto(s): Qualquer objeto, em qualquer quantidade. Os mais comuns são strings de texto e variáveis. 
Independente do tipo, sempre são convertidos em strings antes da impressão.

argumentos_de_palavra-chave: Argumentos opcionais. Permitem controlar como os objetos são separados, o que é impresso no final da linha, 
se a impressão ocorre em um arquivo, etc.


Os argumentos de palavra-chave são:

sep=’separador‘ – Especifica como os objetos serão separados, se houver mais do que um. O padrão é um espaço em branco.
end=’caractere‘ – Especifica o caractere que é impresso no final da linha. O padrão é \n, uma quebra de linha.
file – Especifica um objeto com um método write, com um arquivo. O padrão é o dispositivo sys.stdout (saída padrão – a tela).
flush – Valor booleano que especifica se a saída é eliminada (True) ou gravada em buffer (False). O padrão é False.

'''
#Exemplo de aplicação da função print com números:

print(12345); 

print ('Carlos', 'Magno', sep='-', end='\n');# Exemplo de parâmetros para a função print;

print ('João', 'Carlos', sep='-');


# Exercício: Fazer uma função com print para imprimir um cpf:

print('766','290','822',sep='.', end='-');
print('18'); 


#Exemplo utilizando a impressão de uma variável:

texto = "Olá Estudante! Bem-vindo ao curso de Python."

print(texto);


# Exemplo utilizando argumentos posicionais:

nome1 = 'Carlos dos Reis'

print("Wakie", "Treinamentos", "em Tecnologia -", nome1)

# Exemplo de Concatenação de Strings:

nome2 = input("Digite seu nome: ")

print("Olá " + nome2 + "! Bem-vindo ao curso de Python!\n")

# Exemplo de desabilitar a quebra de linha:

print('Imprime a mensagem e muda de linha\n')

print('Imprime a mensagem e permanece na linha. ',end='')

print('Continuei na mesma linha!')

# Exemplo do uso de Docstring para documentação do projeto

"""
DocString
Linha 1
Linha 2
Linha 3

"""