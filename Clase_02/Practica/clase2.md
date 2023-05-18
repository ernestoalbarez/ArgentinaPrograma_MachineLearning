# Resolución de ejericcios de la clase 2

- [Consignas de ejercicios](actividad_1.py)
- [Archivo con ejercios resueltos](actividad_1-resuelto.py)

## 1. Imprimir **"¡Hola", "mundo!"** en la consola usando `print()`.
```
print("Hola, mundo!")
```
La función `print()` muestra en la consola, lo que reciba dentro de los paréntesis
> En este caso hay que enviar un texto *"Hola, mundo!"* y eso se muestra en la consola

## 2. Pedir al usuario que ingrese su nombre usando `input()` e imprimir un saludo en consola usando `print()`.
```
nombre_ingresado = input("Ingrese nombre: ")
print(f' Hola, {nombre_ingresado}!')
```
La función `input()` recibe datos de la consola, en los paréntesis se escribe un texto informativo a ser mostrado para el usuario
- La información recibida por el `input()` es del tipo *texto*
- En la función `print()` se pueden combiar textos con información contenida en variables, gracias a la *f* al principio, utilizando comillas simples y ecribiendo las variables entre corchetes
> `f'Esto es texto {esto_es_una_variable}'`

## 3. Sumar dos números ingresados por el usuario mediante `input()` y luego mostrar el resultado en consola usando `print()`.
```
primer_ingreso_tipo_texto = input("Ingrese el primer numero: ")
segundo_ingreso_tipo_texto = input("Ingrese el segundo numero: ")

primer_ingreso_tipo_numerico = int(primer_ingreso_tipo_texto)
segundo_ingreso_tipo_numerico = int(segundo_ingreso_tipo_texto)

resultado_de_suma = primer_ingreso_tipo_numerico + segundo_ingreso_tipo_numerico

print(f'El resulrado de la suma es: {resultado_de_suma}')
```
- Ambas variables que terminan en *_tipo_texto* reciben el numero desde la consola, la que ingresa el usuario. Pero este dato es del tipo texto, y Python no puede realizar calculos matemáticos con textos
- Las dos variables que terminan en *_tipo_numerico* son la conversión de esos datos ingresados por el usuario de texto a número, mas específicamente a número entero, ya que se está utilizando la función `int()`
- La variable `resultado_de_suma` almacena el resultado de la operacón matemática, que es posibe gracias a que ambas variables a sumar son del tipo númerico

## 4. Calcular el área de un triángulo a partir de la base y la altura ingresadas por el usuario mediante `input()` y luego mostrar el resultado en consola.
> El calculo para el área de un triángulo es: **(base*altura)/2**

```
base_triangulo = int(input("Ingrese la base del triángulo: "))
altura_triangulo = int(input("Ingrese la altura del triángulo: "))

print(f'El área del triángulo es: {(base_triangulo*altura_triangulo)/2}')
```
Acá observamos que:
- la función `input()` recibe desde la consola el dato ingresado por el usuario
- la función `int()` recibe como argumento a la función `input()`, eso transforma el dato del tipo texto al tipo numécico en una sola línea de código
- se realiza un cálculo matemático dentro de los corchetes en la función `print()`, esto es totalmente válido 

## 5. Calcular el promedio de tres números ingresados por el usuario mediante `input()` y luego mostrar el resultado en consola.
```
primer_ingreso = int(input("Ingrese el primer numero: "))
segundo_ingreso = int(input("Ingrese el segundo numero: "))
tercer_ingreso = int(input("Ingrese el tercer numero: "))

promedio = (primer_ingreso + segundo_ingreso + tercer_ingreso) / 3

print(f'El promedio de los tres números ingresados es: {promedio}')
```
Se podría realizar el calculo del promedio dentro de la función `print()` pero quedaría demasiado largo para leer

## 6. Crear una lista con los siguientes números enteros: `[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]` y mostrar por pantalla el resultado de sumar todos los números de la lista.
```
suma = 0
lista_enteros = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

for numero in lista_enteros:
    suma += numero

print(f'El resultado de la suma de todos los enteros en la lista de enteros es: {suma}')
```
- La variable `suma` está *inicializada* en cero, que es el neutro de la suma. Esto se hace para "limpiar" la variable y cuando le sumemos datos, nos aseguramos que la sumatoria dará un resultado esperado
- El loop `for` sirve para realizar tareas repetitivas, en este caso vamos a realizar sumas repetidas cuyos resultados se almacenan en la variable `suma`
- La expresión `suma += numero` es lo mismo que `suma = suma + numero`, en otras palabras "realizar la operación *suma + numero* y el resultado guardarlo en la variable *suma*"
## 7. Crear una función que reciba un número entero como parámetro y retorne el resultado de multiplicarlo por 2. Imprimir el resultado de invocarla pasándole como argumento un 5.
```
def duplicar(numero):
    return numero * 2

print(f'El numero 5 multiplicado por 2 es: {duplicar(5)}')
```
- Para crear una función se utiliza la palabra reservada `def`, seguido por el nombre de la función y finalmente los paréntesis
- Los paréntesis pueden estar vaciós para indicar que la función no recibirá argumentos
- Los paréntesis pueden estar con argumentos para indiar cuales son los datos que necesita la función
- La palabra reservada `return` indica que la función devuelve un resultado luego cumplir con su trabajo
- Es posible invocar a la función dentro de otra, en este caso dentro del `print()`
> Ya habíamos visto un ejemplo con `int(input("mensaje"))`
## 8. Crear una función que reciba una cadena de texto como parámetro y retorne la cantidad de caracteres que tiene.
```
def contar_cantidad_de_caracteres_en_cadena_de_texto(cadena_ingresada):
    cantidad_caracteres = 0

    for caracter in cadena_ingresada:
        cantidad_caracteres += 1
    
    return cantidad_caracteres
```
- La variable `cantidad_caracteres` comienza en cero para luego ir contanto de uno en uno la cantidad de caracteres del texto ingresado por agumento
- La expresión `for caracter in cadena_ingresada:` va reemplazando el valor de la variable `caracter` en cada iteración, la primera vez se le asigna el valor del primer caracter; la segunda vez el valor del segundo caracter; y así hasta que llege al final de la cadena de texto

## 9. Crear una función que reciba una lista de números enteros como parámetro y retorne el número más grande de la lista.
```
def encontrar_valor_maximo_en_lista(lista_numeros):
    maximo = lista_numeros[0]

for numero in lista_nummeros[1:]:
    if numero > maximo:
        maximo = numero

return maximo
```
- Lo primero que se hace es asumir que el primer valor de la lista es el máimo valor
- Luego se va comparando el valor de la variable `maximo` con cada uno de los valores de la lista; si el valor que está en la lista es mayor, entonces este pasa  ser el nuevo máximo
- La expresión `lista_nummeros[1:]` omite el primer valor de la lista, ya que este se encuentra previamente almacenado en la variable `maximo`
## 10. Crear una función que reciba una lista de cadenas de texto como parámetro y retorne la cantidad de cadenas que tienen más de 5 caracteres.
```
def contar_cadenas_mas_de_cinco_caracteres(lista_cadenas):
    cantidad_max_5 = 0

    for cadena in lista_cadenas:
        cantidad_letras = 0

        for letra in cadena:
            cantidad_letras +=1

        if cantidad_letras > 5:
            cantidad_max_5 +=1
    
    return cantidad_max_5
```
- La variable `cantidad_max_5` está inicializada en cero para ir sumando de a uno la cantidad de palabras que tienen mas de 5 caracteres
- El primer for `for cadena in lista_cadenas:` es para recorrer la lista que contiene a todas las cadenas
- Cada vez que se tiene una cadena lista para recorrer, la variable `cantidad_letras` se inicializa en cero para contar adecuadamente la cantidad de letras
- El segundo for `for letra in cadena:` es para recorrer letra por letra toda la cadena e ir contándolas
- Para cualquier valor mayor a cinco en la variable `cantidad_letras`, se contará a esta cadena como una cadena con mas de cinco letras
- Al finalizar todo el proceso se devuelve la variable `cantidad_max_5` que tendrá contabilizadas las cadenas que llegaron a contar mas de cinco letras