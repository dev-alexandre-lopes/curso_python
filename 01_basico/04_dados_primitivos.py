'''

Aula 04 - Tipos de Dados Primitivos em Python:

Tipo Texto: 	            str
Tipos Numéricos: 	        int, float, complex
Tipos de Sequência:         list, tuple, range
Tipo de Mapeamento: 	    dict
Tipo de Conjuntos (Set):    set, frozenset
Tipo Booleano: 	            bool
Tipo Binário:        	    bytes, bytearray, memoryview
Tipo None:	                NoneType

'''

print ('Helio', type ('Helio'))

print(20, type(20))

print(40.67, type(40.67))

print(2+10j, type(10j))

print(["apple", 50, "cherry"], type(["apple", 50, "cherry"]))

# Coerção de tipos = Typecasting

#Convertendo string em inteiro
print (int('1')+ 1)
print (type(int('1')+ 1))

#Convertendo string em float
print (float('1')+ 5)
print (type(float('1')+ 5))

#Convertendo string em bool
print ('')
print (type(bool('')))



