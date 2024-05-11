
# 1. función que recibe dos números y devuelva el menor.
a = 2
b = 4
minimum = min(a, b)
print("El número menor es:", minimum)
print("----------------- FIN DEL EJERCICIO 1 -----------------")

# 2. función que recibe un texto e invierte las palabras.
text = "Hola mundo"
reverse_text = text.split()[::-1] # Divide la cadena de texto en palabras y las invierte.
reverse_text = ' '.join(reverse_text) # Une las palabras invertidas en una sola cadena de texto.    
print("El texto invertido es:", reverse_text) # Imprime el texto invertido.

""" Esta función llamada `rev_words` toma un argumento `text`, que es una cadena de texto.
La función realiza las siguientes operaciones: """
def rev_words(text):
    words = text.split()# Divide la cadena de texto en palabras utilizando el método `split()`. 
    #Esto crea una lista de palabras.
    reverse_text = reversed(words)# Invierte el orden de las palabras utilizando la función `reversed()`.
    reverse_words= ''.join(reverse_text)# A continuación, utiliza el método `join()` para unir las palabras invertidas en una sola cadena de texto.
    return reverse_words # Finalmente, devuelve la cadena de texto con las palabras invertidas.
if __name__ == "__main__":# se verifica si el archivo actual es el archivo principal que se está ejecutando.
    text = "Hola mundo" # se define una variable `text` que contiene la cadena de texto `"Hola mundo"`. 
    print(rev_words(text)) # se llama a la función `rev_words()` con el argumento `text` y se imprime el resultado.
print("----------------- FIN DEL EJERCICIO 2 -----------------")
    
#  3. Realiza una suma de los elementos de una tupla.
tupla = (1, 2, 3, 4, 5)
print("La tupla es:" + str(tupla))
suma = sum(tupla)
print("La suma de los elementos de la tupla es:", suma)
print("----------------- FIN DEL EJERCICIO 3 -----------------")

# 4. Realiza un código que calcula una lista de números proporcionados por el usuario.
num = int(input("Ingrese un número: ")) # Solicito que ingrese un número con la función input(), lo convierto a número con int().
lista = [] # Crea una lista vacía.
for i in range(num): # Se crea un bucle for que recorre el rango de números ingresados por el usuario.
    lista.append(i) # Se añade cada número ingresado a la lista con la función append().    
print("La lista de números es:", lista) # Imprime la lista de números ingresados.

def lista_numeros(num): # Se define una función llamada `lista_numeros` que toma un argumento `num`.
    if len(num) == 1:
        return num[0] # Si la longitud de la lista es igual a 1, devuelve la lista.
    else:
        return num[0] + lista_numeros(num[1:])
print(lista_numeros([3,5,8,9,9])) # Imprime la suma de lista de números ingresados.
print("----------------- FIN DEL EJERCICIO 4 -----------------")

# 5. Realizar un script que desordene al azar una lista.
import random  # Importa el módulo `random` y se utiliza la función `shuffle()` para desordenar la lista.
lista = [1, 2, 3, 4, 5] # Se define una lista de números.
print("La lista original es:", lista) # Imprime la lista original.
shuffle = random.shuffle(lista) # Desordena la lista utilizando la función `shuffle()`.
print("La lista desordenada es:", lista) # Imprime la lista desordenada.
print("----------------- FIN DEL EJERCICIO 5 -----------------")

# 6. Realizar un script que cuente todas las palabras mayusculas de un archivo de texto.
import re # Importa el módulo `re` para trabajar con expresiones regulares.
archivo = open("texto.txt", "r") # Abre el archivo de texto en modo lectura.
texto = archivo.read() # Lee el contenido del archivo.
archivo.close() # Cierra el archivo.
palabras = re.findall(r'\b[A-Z]+\b', texto) # Utiliza una expresión regular para encontrar todas las palabras en mayúsculas.    
print("Las palabras en mayúsculas:", palabras) # Imprime las palabras en mayúsculas.

with open("texto.txt") as fn: # Abre el archivo de texto en modo lectura, el metodo "with" permite lee y cerrar el archivo txt.
    count = 0 # Inicializa un contador en 0.
    text = fn.read() # Lee el contenido del archivo.
    for character in text: # Recorre cada carácter en el texto.
        if character.isupper(): # Verifica si el carácter es una letra mayúscula.
            count += 1 # Incrementa el contador en 1.
print("El número de palabras que empiezan en mayúsculas es:", count) # Imprime el número de palabras en mayúsculas.
print("----------------- FIN DEL EJERCICIO 6 -----------------")

# 7. ¿Si la lista 1 es [4, 6, 8, 1, 0, 3], que sería la lista 1 [-1]?
lista = [4,6,8,0,1,3] # Se define una lista de números.
print( lista[-1]) # Imprime el último elemento de la lista.
print("----------------- FIN DEL EJERCICIO 7 -----------------")

# 8. Escriba un programa para producir la serie Fibonacci en Python.
n = int(input("Ingrese un número: ")) # Solicita al usuario que ingrese un número.
first = 0 # Inicializa el primer número de la serie Fibonacci.
second = 1 # Inicializa el segundo número de la serie Fibonacci.
for i in range(n): # Se crea un bucle for que recorre el rango de números ingresados por el usuario.
    print("frecuencia de Fibonacci: " + str(first)) # Imprime el primer número de la serie Fibonacci.
    temp = first # Almacena el primer número en una variable temporal.
    first = second # Asigna el segundo número al primer número.
    second = temp + second # Asigna la suma de los dos números anteriores al segundo número.
print("----------------- FIN DEL EJERCICIO 8 -----------------")

# 9. programa en Python para comprobar si un número es primo.
def isPrimo(n): # Se define una función llamada `isPrimo` que toma un argumento `n`.
    if n <= 1: # Si el número es menor o igual a 1, no es primo.
        return False
    for i in range(2, n): # Se crea un bucle for que recorre el rango de números del 2 al número ingresado.
        if n % i == 0: # Si el número es divisible por otro número, no es primo.
            return False
    return True # Si el número no es divisible por ningún otro número, es primo.
if __name__ == "__main__": # se verifica si el archivo actual es el archivo principal que se está ejecutando.
    n = int(input("Ingrese un número: ")) # Solicita al usuario que ingrese un número.
    if isPrimo(n): # se llama a la función `isPrimo()` con el argumento `n`.
        print("El número es primo.") # si el número es primo, imprime un mensaje.
    else:
        print("El número no es primo.") # si el número no es primo, imprime un mensaje.
print("----------------- FIN DEL EJERCICIO 9 -----------------")

# 10. programa en Python para comprobar si un número es capicúa. Es decir, si se lee igual de derecha a izquierda que de izquierda a derecha.5
def is_capicua(n): # Se define una función llamada `is_capicua` que toma un argumento `a`.
    # Convierte el número en una cadena de texto y compara si es igual a su reverso.
    return str(n) == str(n)[::-1] # Devuelve verdadero si el número es capicúa.

if __name__ == "__main__": # se verifica si el archivo actual es el archivo principal que se está ejecutando.
    n = int(input("Ingrese un número: ")) # Solicita al usuario que ingrese un número.
    if is_capicua(n): # se llama a la función `is_capicua()` con el argumento `n`.
        print("El número es capicúa.")
    else:
        print("El número no es capicúa.")
print("----------------- FIN DEL EJERCICIO 10 -----------------")

# 11. Escribir un algoritmo de ordenación para un conjunto de datos numéricos en Python.
def bubble_sort(data): # Se define una función llamada `bubble_sort` que toma un argumento `data`.
    n = len(data) # Obtiene la longitud de los datos.
    for i in range(n-1): # Se crea un bucle for que recorre el rango de números de la longitud de los datos.
        for j in range(n-i-1): # Se crea un bucle for anidado que recorre el rango de números de la longitud de los datos menos el índice actual.
            if data[j] > data[j+1]: # Compara si el número actual es mayor que el siguiente número.
                data[j], data[j+1] = data[j+1], data[j] # Intercambia los números si el número actual es mayor que el siguiente número.
    return data

if __name__ == "__main__":
    data = [5, 2, 8, 1, 9, 3]
    sorted_data = bubble_sort(data) # se llama a la función `bubble_sort()` con el argumento `data`.
    print("Datos ordenados:", sorted_data)
print("----------------- FIN DEL EJERCICIO 11 -----------------")