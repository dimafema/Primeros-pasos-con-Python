"""
Este código muestra ejemplos de declaración de variables en Python.
"""

# declaracion de variables
# variables tipo entero
numero_entero_int= 10
# variables tipo flotante
numero_flotante_float= 10.5    # Siempre el punto, es el separador de decimales
# variables tipo string
texto__str = "hola"            # Siempre entre comillas dobles o simples
texto__str2 = 'esto es "un texto" dentro de otro texto'    
texto__str3 = """-------
esto es un texto 
con diferentes lineas 
con el caracter de escape comillas
-----------------------------------"""   # Siempre entre comillas triples
texto__str4 = """------- \n
esto es un texto \n
con diferentes lineas de otro texto \n
con el caracter de escape \n
-----------------------------------"""   # también se puede usar el caracter de escape \n para continuar en la siguiente linea
# variables tipo boleano
boleano_bool = True  # True es igual a 1 y False es igual a 0
bool2 = False
# variables tipo lista
lista_list = [1,2,3,4,5]
# variables tipo tupla
tupla_tuple = (1,2,3,4,5)
# variables tipo diccionario
diccionario_dict = {"nombre":"juan","apellido":"perez"}
# variables tipo conjunto
conjunto_set = {1,2,3,4,5}

"""  Las restricciones al declarar variables en Python son las siguientes:

1. Los nombres de las variables deben comenzar con una letra o un guión bajo (_).
2. Los nombres de las variables solo pueden contener letras, números y guiones bajos.
3. Los nombres de las variables distinguen entre mayúsculas y minúsculas, por lo que "nombre" y "Nombre" son variables diferentes.
4. No se pueden utilizar palabras reservadas de Python como nombres de variables. Algunas palabras reservadas comunes son: ```and```, ```or```, ```if```, ```else```, ```for```, ```while```, ```def```, ```class```, etc.
5. Es una buena práctica utilizar nombres descriptivos para las variables, que reflejen su propósito o contenido.
6. No se pueden utilizar caracteres especiales, como espacios, en los nombres de las variables.

Recuerda que estas son solo algunas de las restricciones al declarar variables en Python. Es importante seguir estas reglas para evitar errores y confusiones en tu código.  """

# imprimir variables
print(lista_list)
print(tupla_tuple)
print(diccionario_dict)
print(conjunto_set)
print(numero_entero_int)
print(numero_flotante_float)
print(texto__str)
print(texto__str2)
print(texto__str3)
print(texto__str4)
print(boleano_bool)
print(bool2 + 1)  # el valor de False es 0 como hemos sumado 1 el resultado es 1
print("--------------------------------------------------------------------------------")

"""las constantes son variables cuyo valor no cambia durante la ejecución de un programa. En Python, no hay una forma directa de declarar constantes, 
    ya que las variables pueden cambiar de valor en cualquier momento. Sin embargo, se puede seguir una convención de nomenclatura para indicar que una 
    variable se considera constante y no debe modificarse. Por ejemplo, se puede utilizar un nombre en mayúsculas para indicar que una variable es una constante, como en el siguiente ejemplo:
    """
CONSTANTE_TITULO = "CONSTANTES EN PYTHON"
CONSTANTE_PI = 3.14159
CONSTANTE_GRAVEDAD = 9.8
CONSTANTE_VELOCIDAD_LUZ = 299792458
CONSTANTE_NOMBRE_EMPRESA = "Acme Corp"
CONSTANTE_NUMERO_MAGICO = 42

print(CONSTANTE_TITULO)
print(CONSTANTE_PI)
print(CONSTANTE_GRAVEDAD)
print(CONSTANTE_VELOCIDAD_LUZ)
print(CONSTANTE_NOMBRE_EMPRESA)
print(CONSTANTE_NUMERO_MAGICO)
