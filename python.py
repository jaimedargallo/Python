# Python.org
# https://docs.python.org/es/3/
# https://docs.python.org/es/3/library/functions.html


# <cadena>[inicio:]
# <cadena>[:fin]
# <cadena>[:]

sentence = "Hello World!"
sentence[3:7]
sentence[2:4:7]

# Métodos importantes

find
index
lower
upper

isalnum
isalpha
isdecimal
isdigit
islower
isupper

# Los métodos que comienzan por is devolerán un valor Booleano


#Operadores aritméticos

# Suma

5 + 6

3.4 + 5.6

"Hello" + " " + "World!" #Concadenar

# Resta

10 - 4
0 - 6
3.4 - 5.6
2 - 8.9
"Hello" + " " + "World!" #Concadenar


# Multiplicación

5 * 6
4 * 0
-5 * -8
-5 * 8
4.5 * 7.9 


# División (siempre devuelve un valor de coma flotante)

15 / 5
15 / 8
12.5 / 4
4 / 4.45
4.2 / 4.1

15 // 5
3 // 5
157 // 56
-4 // -6
-15 // -10

56 / 3.4
5.6 // 3.4
#Util en el algoritmo de busqueda binaria


# Exponente

5 ** 3
3 ** 8
2 ** 3
4.5 ** 4.7
16 ** (1/2)
5 ** 0

# Modulo
5 % 2
4 % 3
16 % 6 
18 % 4


# Orden de resolución
# ----> PEMDAS <----
# Parentesis
# Exponentes
# Multiplicación
# División
# Suma ( adición)
# Resta (sustracción)

# Condicionales

# if <condition>:
    # Code

temp = 15

if temp <= 0:
    print ("Muy Frio")
elif temp < 25:
    print ("Frio")
else:
    print ("Calor")


# Listas

letras = ["a", "b", "c", "d"]

letras[0]
# "a"

nums = [1, 2, 3, 4]
nums.append(5)
nums
# [1, 2, 3, 4, 5]

nums = [1, 2, 3, 5]
nums.insert(3, 4)
nums
# [1, 2, 3, 4, 5]


nums = [1, 2, 6, 3, 4, 5, 6]
nums.remove(6)
nums
# [1, 2, 3, 4, 5]


letras = ["a", "b", "c", "d"]
"a" in letras
# True
"z" in letras
# False


letras = ["a", "b", "c", "d"]
letras.index("c")
# 2

nums = [1, 2, 6, 3, 4, 5, 6]
nums[0] = -8
nums
# [-8, 2, 6, 3, 4, 5, 6]


# Metodos de las listas

.count(<elem>)
.extend(<lista>)
.pop
.reverse
.sort


a = [
a.pop()
# 6
a.reverse()
a.extend([8, 9, 0])

# [5, 4, 3, 8, 9, 0]


# Tuplas
# Las listas son mutables, las tuplas inmutables

letras = ("a", "b", "c", "d")
letras.index("a")
#0

nums = (3, 5, 2, 3, 4, 6, 3, 2, 3)
nums.count(3)
# 4


# Diccionarios

# Son colecciones de Pares Clave-Valor
# Las claves deben ser únicas e inmutables
# Los valores si son mutables


ages = {"Gino": 15, "Noa": 45}
ages["Gino"]

# 15


ages = {"Gino": 15, "Noa": 45}
ages["Talina"] = 67
ages
# {'Gino': 15, 'Noa': 45, 'Talina': 67}

ages["Talina"] = 77
ages
# {'Gino': 15, 'Noa': 45, 'Talina': 77}

del ages["Talina"]
ages
# {'Gino': 15, 'Noa': 45}

"Gino" in ages
# True

"Talina" in ages
# False



# Estructuras de Control

# Bucles For
# Se utilizan cuando se sabe con antelación cuantas veces se repite

for <var> in range (<inicio>, <fin>)
    # Code

for i in range(4):
    print(i)

#range(start, stop[, step])



#ciclos sobre iterables

for <var> in range <iterable>:
    # Code

for char in "Loops":
    print(char)


for num in [1, 2, 3):
    print(num)


letras = {"a": 1, "b": 2}
for valor in letras.values():
    print(valor)


for clave, valor in letras.items():
    print(clave, valor)



# Bucles While
# Continua mientras una condición sea verdadera y se detiene cuando es falsa


while <condición>
    # Códe


x = 20

while x < 35:
        print(x)
        x += 3 



# Funciones






 
