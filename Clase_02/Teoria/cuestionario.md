# Cuestionario guia de lectura del material

- [Conceptos básicos](Clase_02/Teoria/Machine Learning I Semana 02 - Conceptos básicos de Python.pdf)
- [Modulo](Clase_02/Teoria/Machine Learning I Semana 02 - Modulo 1.pdf)
- [Clase 2 - Youtube](https://youtu.be/sFMemySEMlg)

## 1. ¿Qué es python y qué ventajas tiene como lenguaje de programación?
Python es un lenguaje de programación interpretado y de alto nivel. Se caracteriza por su simplicidad, legibilidad y facilidad de uso. Algunas de las ventajas de Python como lenguaje de programación son:

- **Sintaxis clara y legible:** Python utiliza una sintaxis concisa y legible, lo que facilita la comprensión y el mantenimiento del código. Su estilo de escritura en bloques mediante indentación en lugar de llaves o palabras clave mejora la legibilidad del código.

- **Amplia biblioteca estándar:** Python cuenta con una amplia biblioteca estándar que proporciona una amplia gama de funcionalidades y herramientas para diferentes tareas, lo que facilita el desarrollo de aplicaciones sin necesidad de buscar bibliotecas externas.

- **Gran cantidad de bibliotecas y frameworks:** Python tiene una comunidad activa que ha desarrollado una gran cantidad de bibliotecas y frameworks que cubren diversos dominios, como ciencia de datos, aprendizaje automático, desarrollo web, automatización de tareas, entre otros. Esto permite a los programadores aprovechar estas herramientas y acelerar el desarrollo de aplicaciones.

- **Portabilidad:** Python es un lenguaje multiplataforma, lo que significa que el mismo código se puede ejecutar en diferentes sistemas operativos sin necesidad de cambios significativos. Esto brinda flexibilidad al desarrollar aplicaciones para diferentes entornos.

- **Aprendizaje y productividad:** Python es considerado uno de los lenguajes más fáciles de aprender debido a su sintaxis sencilla y clara. Además, su enfoque en la legibilidad del código y su amplia disponibilidad de herramientas y bibliotecas contribuyen a una mayor productividad en el desarrollo de aplicaciones.

- **Integración:** Python se puede integrar fácilmente con otros lenguajes como C, C++, Java y .NET, lo que permite utilizar bibliotecas existentes escritas en otros lenguajes y aprovechar las fortalezas de cada uno.

- **Comunidad activa:** Python cuenta con una comunidad de desarrolladores muy activa y colaborativa. Esto significa que hay una abundancia de recursos, documentación, tutoriales y foros de discusión que pueden ayudar a resolver problemas y facilitar el aprendizaje.

En resumen, Python es un lenguaje de programación versátil y poderoso que ofrece una amplia gama de ventajas, desde su legibilidad y facilidad de uso hasta su ecosistema rico en bibliotecas y frameworks. Estas características hacen de Python una elección popular para el desarrollo de una variedad de aplicaciones, desde scripts simples hasta proyectos de mayor envergadura.

## 2. ¿Cómo se define una función en python y cómo se le pasan argumentos?
En Python, se define una función utilizando la palabra clave `def` seguida del nombre de la función y paréntesis que pueden contener los argumentos de la función. La sintaxis general para definir una función es la siguiente:

```
def nombre_de_funcion(argumento1, argumento2, ...):
    # Cuerpo de la función
    # Código que se ejecuta cuando la función es llamada
    # Puede incluir declaraciones, operaciones, llamadas a otras funciones, etc.
    return resultado  # Opcionalmente, se puede devolver un valor

```

Aquí hay un ejemplo simple de cómo definir una función que suma dos números:
```
def sumar(a, b):
    resultado = a + b
    return resultado

```

Para llamar a una función y pasarle argumentos, simplemente utilizamos el nombre de la función seguido de paréntesis que contienen los valores que deseamos pasar. Por ejemplo, para llamar a la función `sumar()` y pasarle los argumentos 3 y 4, haríamos lo siguiente:
```
resultado_suma = sumar(3, 4)
print(resultado_suma)  # Imprimirá 7

```

En este ejemplo, la función `sumar()` recibe dos argumentos, `a` y `b`, realiza la operación de suma y devuelve el resultado. Al llamar a la función `sumar(3, 4)`, los valores 3 y 4 se asignan a los parámetros `a` y `b` dentro de la función, y se devuelve el resultado de la suma, que es 7. Finalmente, el resultado se almacena en la variable `resultado_suma` y se imprime en la consola.

## 3. ¿Qué son las listas y los diccionarios en python y cómo se acceden a sus elementos?
En Python, las listas y los diccionarios son estructuras de datos muy utilizadas para almacenar y organizar colecciones de elementos. Aquí tienes una explicación de cada uno y cómo se acceden a sus elementos:

**Listas:**
- Definición: Una lista es una secuencia ordenada y mutable de elementos separados por comas y encerrados entre corchetes ([ ]).
- Ejemplo de creación:
    ```
    mi_lista = [1, 2, 3, 4, 5]
    ```
- Acceso a elementos: Los elementos de una lista se acceden mediante su índice, que comienza en 0. Puedes acceder a un elemento específico utilizando el índice entre corchetes.
    ```
    primer_elemento = mi_lista[0]  # Acceder al primer elemento (índice 0)
    tercer_elemento = mi_lista[2]  # Acceder al tercer elemento (índice 2)
    ```
- Modificación de elementos: Las listas son estructuras mutables, lo que significa que puedes modificar sus elementos asignándoles nuevos valores.
    ```
    mi_lista[3] = 10  # Modificar el cuarto elemento de la lista
    ```
- Operaciones comunes: Las listas tienen métodos incorporados que permiten realizar diversas operaciones, como agregar elementos, eliminar elementos, ordenar la lista, obtener su longitud, entre otros.

**Diccionarios:**
- Definición: Un diccionario es una estructura de datos mutable que almacena pares de clave-valor, donde cada clave está asociada a un valor y se encierran entre llaves ({ }).
- Ejemplo de creación:
    ```
    mi_diccionario = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}
    ```
- Acceso a elementos: Los elementos de un diccionario se acceden mediante sus claves en lugar de utilizar índices. Puedes acceder a un valor específico utilizando la clave entre corchetes.
    ```
    nombre = mi_diccionario["nombre"]  # Acceder al valor asociado a la clave "nombre"
    edad = mi_diccionario["edad"]  # Acceder al valor asociado a la clave "edad"
    ```
- Modificación de elementos: Los valores de un diccionario pueden modificarse asignando un nuevo valor a una clave existente o añadiendo una nueva clave-valor.
    ```
    mi_diccionario["edad"] = 26  # Modificar el valor asociado a la clave "edad"
    mi_diccionario["profesion"] = "Ingeniero"  # Agregar una nueva clave-valor
    ```
- Operaciones comunes: Los diccionarios tienen métodos incorporados que permiten realizar operaciones como obtener todas las claves, obtener todos los valores, verificar si una clave existe, entre otros.

En resumen, las listas se utilizan para almacenar una secuencia ordenada de elementos, y los elementos se acceden por su índice. Los diccionarios se utilizan para almacenar pares de clave-valor, y los elementos se acceden por sus claves. Ambas estructuras de datos son muy versátiles y útiles en diferentes escenarios de programación.


## 4. ¿Cómo se usa la sentencia if para controlar el flujo de ejecución en python?
En Python, el enunciado "if" se utiliza para controlar el flujo de ejecución condicionalmente. Permite ejecutar un bloque de código si se cumple una condición especificada. Aquí tienes la estructura básica de un enunciado "if" en Python:
```
if condicion:
    # Bloque de código que se ejecuta si la condición es verdadera
    # Puede contener una o varias instrucciones
else:
    # Bloque de código que se ejecuta si la condición es falsa
    # Opcional y se ejecuta cuando la condición del "if" es falsa
    # También puede contener una o varias instrucciones

```

La condición en el enunciado "if" es una expresión que se evalúa como verdadera o falsa. Si la condición es verdadera, se ejecuta el bloque de código indentado bajo el enunciado "if". Si la condición es falsa, se omite ese bloque y se ejecuta el bloque indentado bajo el enunciado "else" (si está presente).

Aquí tienes un ejemplo simple que muestra cómo utilizar el enunciado "if" para controlar el flujo de ejecución:
```
edad = 18

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

```

En este ejemplo, la variable `edad` se compara con el valor 18. Si la condición `edad >= 18` es verdadera, se imprimirá "Eres mayor de edad". De lo contrario, se imprimirá "Eres menor de edad".

Es importante tener en cuenta que la parte del "else" es opcional. Puedes tener solo el enunciado "if" sin la parte del "else" si no deseas ejecutar un bloque de código específico cuando la condición sea falsa.

Además, se pueden utilizar construcciones adicionales, como el enunciado "elif" (abreviatura de "else if"), para evaluar múltiples condiciones en secuencia. Esto permite realizar pruebas condicionales más complejas y tener diferentes bloques de código para diferentes situaciones.

## 5. ¿Qué es el bucle for y cómo se usa junto con la función range?
El bucle "for" en Python se utiliza para iterar sobre una secuencia de elementos o realizar un conjunto de instrucciones un número determinado de veces. Se combina comúnmente con la función "range()" para generar una secuencia de números que se utilizan en la iteración. Aquí tienes una explicación de cómo funciona:

La estructura básica de un bucle "for" en Python es la siguiente:
```
for elemento in secuencia:
    # Bloque de código que se repite para cada elemento de la secuencia
    # Puede contener una o varias instrucciones

```

- `elemento` es una variable que se utiliza para almacenar el valor actual de la secuencia en cada iteración. Puedes elegir cualquier nombre válido para esta variable.
- `secuencia` puede ser una lista, una tupla, una cadena de texto u otra estructura iterable en Python.

Cuando se utiliza en conjunto con la función "range()", el bucle "for" itera sobre una secuencia de números generados por "range()". La función "range()" devuelve una secuencia de números que se pueden utilizar en la iteración del bucle "for". Aquí tienes una forma básica de utilizar el bucle "for" con la función "range()":
```
for i in range(inicio, fin, paso):
    # Bloque de código que se repite para cada valor de 'i' en el rango
    # Puede contener una o varias instrucciones

```

- `inicio` es el valor inicial del rango (inclusive). Si no se especifica, se asume que es 0.
- `fin` es el valor final del rango (exclusivo). El rango generado por "range()" no incluirá este valor.
- `paso  es el incremento entre los valores sucesivos del rango. Si no se especifica, se asume que es 1.

Aquí tienes un ejemplo que muestra cómo utilizar el bucle "for" con la función "range()" para imprimir los números del 1 al 5:
```
for i in range(1, 6):
    print(i)

```

En este ejemplo, el bucle "for" se repetirá cinco veces, y en cada iteración, la variable `i` tomará los valores 1, 2, 3, 4 y 5. En cada iteración, se imprime el valor de `i`.

El bucle "for" con la función "range()" es una herramienta poderosa para iterar sobre secuencias de números o realizar una tarea repetitiva un número determinado de veces. Puedes ajustar el rango y la lógica dentro del bloque de código para adaptarse a tus necesidades específicas.