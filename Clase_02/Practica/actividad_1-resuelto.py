# ACTIVIDAD 1: EJERCICIOS DE PROGRAMACIÓN BÁSICA EN PYTHON
# **ADVERTENCIA**: No borrar los comentarios que se encuentran en el código", "ya que son necesarios para la evaluación de la actividad.
# **ADVERTENCIA**: No cambiar el nombre del archivo", "de lo contrario no se considerará entregado.
# **ADVERTENCIA**: El programa debe ejecutarse una vez y realizar todos los puntos de manera secuencial. No se evaluarán programas que ejecuten solo una parte.
# **ADVERTENCIA**: El código de cada actividad debe escribirse debajo de cada comentario correspondiente.

## ACTIVIDADES
# 1. Imprimir "¡Hola", "mundo!" en la consola usando print().
def ejercicio_1():
    print("Hola", "mundo!")

print("Ejercicio 1:")
ejercicio_1()

# 2. Pedir al usuario que ingrese su nombre usando input() e imprimir un saludo en consola usando print().
def ejercicio_2():
    nombre_ingresado = input("Ingrese nombre: ")
    print(f' Hola", "{nombre_ingresado}!')

print("\nEjercicio 2:")
ejercicio_2()

# 3. Sumar dos números ingresados por el usuario mediante input() y luego mostrar el resultado en consola usando print().
def ejercicio_3():
    primer_ingreso = int(input("Ingrese el primer numero: "))
    segundo_ingreso = int(input("Ingrese el segundo numero: "))

    print(f'El resulrado de la suma es: {primer_ingreso + segundo_ingreso}')

print("\nEjercicio 3:")
ejercicio_3()

# 4. Calcular el área de un triángulo a partir de la base y la altura ingresadas por el usuario mediante input() y luego mostrar el resultado en consola.
def ejercicio_4():
    base_triangulo = int(input("Ingrese la base del triángulo: "))
    altura_triangulo = int(input("Ingrese la altura del triángulo: "))

    print(f'El área del triángulo es: {(base_triangulo*altura_triangulo)/2}')

print("\nEjercicio 4:")
ejercicio_4()

# 5. Calcular el promedio de tres números ingresados por el usuario mediante input() y luego mostrar el resultado en consola.
def ejercicio_5():
    primer_ingreso = int(input("Ingrese el primer numero: "))
    segundo_ingreso = int(input("Ingrese el segundo numero: "))
    tercer_ingreso = int(input("Ingrese el tercer numero: "))

    promedio = (primer_ingreso + segundo_ingreso + tercer_ingreso) / 3

    print(f'El promedio de los tres números ingresados es: {promedio}')

print("\nEjercicio 5:")
ejercicio_5()

# 6. Crear una lista con los siguientes números enteros: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20] y mostrar por pantalla el resultado de sumar todos los números de la lista.
def ejercicio_6():
    suma = 0
    lista_enteros = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

    for numero in lista_enteros:
        suma += numero
    
    print(f'El resultado de la suma de todos los enteros en la lista de enteros es: {suma}')

print("\nEjercicio 6:")
ejercicio_6()

# 7. Crear una función que reciba un número entero como parámetro y retorne el resultado de multiplicarlo por 2. Imprimir el resultado de invocarla pasándole como argumento un 5.
def duplicar(numero):
    return numero * 2

def ejercicio_7():
    print(f'El numero 5 multiplicado por 2 es: {duplicar(5)}')

print("\nEjercicio 7:")
ejercicio_7()

# 8. Crear una función que reciba una cadena de texto como parámetro y retorne la cantidad de caracteres que tiene.
def ejercicio_8():
    cantidad_caracteres = 0
    cadena_ingresada = input("Ingrese un texto: ")

    for caracter in cadena_ingresada:
        cantidad_caracteres += 1
    
    print(f'La cantidad de caracteres en la cadena ingresada es: {cantidad_caracteres}')


# 9. Crear una función que reciba una lista de números enteros como parámetro y retorne el número más grande de la lista.
def ejercicio_9(lista_numeros):
    maximo = lista_numeros[0]

    for numero in lista_nummeros[1:]:
        if numero > maximo:
            maximo = numero
    
    return maximo


# 10. Crear una función que reciba una lista de cadenas de texto como parámetro y retorne la cantidad de cadenas que tienen más de 5 caracteres.
def ejercicio_10(lista_cadenas):
    cantidad_max_5 = 0
    
    for cadena in lista_cadenas:
        cantidad_letras = 0

        for letra in cadena:
            cantidad_letras +=1

        if cantidad_letras > 5:
            cantidad_max_5 +=1
    
    print(f'La cantidad de cadenas con mas de 5 caracteres es: {cantidad_max_5}')
