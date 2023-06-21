# Cuestionario guia de lectura del material
- [Clase 5 - YouTube](https://youtu.be/4sAeT16H62M)

## 1. ¿Qué es numpy y para qué se utiliza?
NumPy (Numerical Python) es una biblioteca esencial para el cálculo numérico en Python. Se utiliza ampliamente en campos como ciencia de datos, aprendizaje automático, simulaciones científicas y más. Proporciona una base sólida para el manejo de datos numéricos eficiente y la realización de operaciones matemáticas complejas en arreglos multidimensionales.

>Algunas características clave de NumPy y cómo se utiliza:

**Arreglos multidimensionales:** NumPy introduce el objeto ndarray, que es un arreglo n-dimensional eficiente en memoria. Los arreglos de NumPy son más rápidos y consumen menos memoria que las listas de Python estándar, lo que los hace ideales para trabajar con grandes cantidades de datos numéricos.

**Funciones matemáticas:** NumPy ofrece una amplia gama de funciones matemáticas para realizar operaciones en los arreglos. Estas funciones están optimizadas para un rendimiento eficiente y pueden operar en todo el arreglo o a lo largo de un eje específico.

**Operaciones de álgebra lineal:** NumPy proporciona un conjunto completo de funciones y herramientas para realizar cálculos de álgebra lineal, como multiplicación de matrices, descomposición de valores singulares, resolución de sistemas de ecuaciones lineales, entre otros.

**Integración con otras bibliotecas:** NumPy es una base fundamental para muchas otras bibliotecas científicas en Python, como pandas, SciPy y scikit-learn. Estas bibliotecas se construyen sobre NumPy y aprovechan su capacidad para manejar eficientemente grandes conjuntos de datos y realizar operaciones numéricas complejas.

**Indexación y slicing avanzado:** NumPy permite realizar operaciones de indexación y slicing en los arreglos, lo que facilita la extracción y manipulación de subconjuntos de datos.

## 2. ¿Qué ventajas tiene usar numpy sobre las listas de Python para el cálculo científico?
Numpy provides several advantages over Python lists for scientific computation:

**Efficient storage and manipulation of arrays:** Numpy uses a contiguous block of memory to store arrays, which allows for efficient access and manipulation of elements. In contrast, Python lists are implemented as dynamic arrays, leading to less efficient memory management and slower computations.

**Vectorized operations:** Numpy supports vectorized operations, which allow you to perform element-wise operations on entire arrays without the need for explicit loops. This leads to more concise and efficient code compared to manually iterating over Python lists.

**Optimized mathematical functions:** Numpy provides a wide range of optimized mathematical functions that operate on arrays, such as trigonometric functions, exponential functions, linear algebra operations, and more. These functions are implemented in C or Fortran and are therefore faster than their Python counterparts.

**Broad range of numerical data types:** Numpy offers a variety of numerical data types with different precision levels, including integers, floating-point numbers, and complex numbers. This flexibility allows you to choose the appropriate data type for your specific scientific computations, optimizing both memory usage and computational efficiency.

**Broadcasting:** Numpy's broadcasting feature allows arrays of different shapes to be automatically resized and matched during arithmetic operations. This simplifies the handling of arrays with different dimensions, eliminating the need for explicit loop structures and enabling efficient computations on multi-dimensional data.

**Integration with other scientific libraries:** Numpy is a fundamental building block for many other scientific libraries in Python, such as Pandas, Scikit-learn, and SciPy. It provides a common data structure that seamlessly integrates with these libraries, enabling efficient data manipulation, analysis, and modeling.

Overall, Numpy's advantages make it a powerful tool for scientific computation. Its efficient storage, vectorized operations, optimized functions, data types, broadcasting capabilities, and integration with other libraries make it a preferred choice for handling and processing numerical data in scientific computing tasks.

## 3. ¿Qué es un array de numpy y cómo se crea?
Un arreglo de NumPy (NumPy array) es una estructura de datos multidimensional que contiene elementos del mismo tipo. Es una de las principales características de NumPy y se utiliza ampliamente en la computación científica y el análisis numérico.

Un arreglo de NumPy se puede crear de diferentes formas:

- **Desde una lista o tupla:** Puedes crear un arreglo de NumPy a partir de una lista o tupla existente utilizando la función numpy.array(). Por ejemplo:
    ```
    import numpy as np

    lista = [1, 2, 3, 4, 5]
    arreglo = np.array(lista)
    ```

- **Utilizando funciones específicas de NumPy:** NumPy proporciona varias funciones específicas para crear arreglos con valores predefinidos. Algunas de estas funciones incluyen `numpy.zeros()`, `numpy.ones()`, `numpy.arange()`, `numpy.linspace()`, entre otras. Por ejemplo:
    ```
    import numpy as np

    arreglo_zeros = np.zeros((3, 4))  # Crea un arreglo de ceros de tamaño 3x4
    arreglo_ones = np.ones((2, 3))    # Crea un arreglo de unos de tamaño 2x3
    arreglo_range = np.arange(0, 10, 2)  # Crea un arreglo con valores del 0 al 8 (con incremento de 2)
    arreglo_linspace = np.linspace(0, 1, 5)  # Crea un arreglo de 5 valores equidistantes entre 0 y 1
    ```

- **Desde un archivo de datos:** NumPy permite cargar datos desde archivos existentes en formatos como CSV o texto delimitado. Puedes utilizar funciones como `numpy.loadtxt()` o `numpy.genfromtxt()` para cargar datos en un arreglo de NumPy.

Una vez que se ha creado un arreglo de NumPy, puedes acceder a sus elementos utilizando índices y realizar operaciones matemáticas y manipulaciones de datos eficientes en ellos debido a la naturaleza vectorizada de las operaciones de NumPy.

Por ejemplo, aquí tienes un código que muestra cómo crear un arreglo de NumPy y realizar algunas operaciones básicas:
```
import numpy as np

# Crear un arreglo de NumPy desde una lista
lista = [1, 2, 3, 4, 5]
arreglo = np.array(lista)

# Acceder a los elementos del arreglo
print(arreglo[0])   # Acceder al primer elemento: 1
print(arreglo[2])   # Acceder al tercer elemento: 3

# Realizar operaciones matemáticas en el arreglo
arreglo_cuadrado = arreglo ** 2
suma_total = np.sum(arreglo)

print(arreglo_cuadrado)  # [ 1  4  9 16 25]
print(suma_total)        # 15
```

En este ejemplo, se crea un arreglo de NumPy a partir de una lista. Luego, se accede a los elementos del arreglo utilizando índices. También se realizan operaciones matemáticas en el arreglo, como elevar al cuadrado cada elemento y calcular la suma total de los elementos utilizando las funciones de NumPy.

## 4. ¿Qué operaciones se pueden realizar con los arrays de numpy?
Los arrays de Numpy admiten una amplia gama de operaciones que se pueden realizar para cálculos matemáticos y lógicos eficientes. Aquí hay algunas operaciones comunes que se pueden realizar con arrays de numpy:

- **Operaciones aritméticas:** Los arreglos de NumPy admiten operaciones aritméticas elemento a elemento, como suma, resta, multiplicación y división. Estas operaciones se pueden realizar entre dos arreglos del mismo tamaño o entre un arreglo y un valor escalar.

- **Funciones matemáticas:** NumPy proporciona una amplia colección de funciones matemáticas que operan elemento a elemento en los arreglos. Estas funciones incluyen funciones trigonométricas (`np.sin()`, `np.cos()`, etc.), funciones exponenciales y logarítmicas (`np.exp()`, `np.log()`, etc.), raíz cuadrada (`np.sqrt()`), funciones de redondeo (`np.round()`, `np.floor()`, `np.ceil()`), entre otras.

- **Manipulación de arreglos:** Los arreglos de NumPy ofrecen diversas funciones para manipular su forma y dimensiones. Puedes cambiar la forma de un arreglo utilizando `np.reshape()`, transponer un arreglo utilizando `np.transpose()`, concatenar arreglos utilizando `np.concatenate()`, dividir un arreglo utilizando `np.split()`, y apilar arreglos utilizando `np.stack()`, entre otras.

- **Operaciones de reducción:** Los arreglos de NumPy te permiten realizar operaciones de reducción a lo largo de un eje específico. Estas operaciones incluyen sumar elementos (`np.sum()`), calcular la media (`np.mean()`), encontrar los valores mínimo y máximo (`np.min()`, `np.max()`), calcular la desviación estándar (`np.std()`), y realizar otros cálculos estadísticos.

- **Operaciones lógicas:** Los arreglos de NumPy admiten operaciones lógicas, como comparaciones elemento a elemento (`<`, `>`, `==`, etc.) y operaciones lógicas como `np.logical_and()`, `np.logical_or()`, y `np.logical_not()` para realizar operaciones lógicas elemento a elemento en arreglos.

- **Operaciones de álgebra lineal:** NumPy brinda un soporte completo para operaciones de álgebra lineal. Puedes realizar multiplicación de matrices (`np.dot()`), calcular el determinante (`np.linalg.det()`), calcular los valores propios y vectores propios (`np.linalg.eig()`), resolver sistemas lineales (`np.linalg.solve()`), y más.

- **Indexación y segmentación:** Los arreglos de NumPy permiten la indexación y segmentación para acceder a elementos específicos o subarreglos. Puedes utilizar indexación entera, indexación booleana y la notación de segmentación (`:`) para seleccionar elementos específicos o rangos de elementos de un arreglo.

Estos son solo algunos ejemplos de las operaciones que se pueden realizar con arreglos de NumPy. La funcionalidad extensa de NumPy lo convierte en una herramienta poderosa para realizar cálculos numéricos eficientes en diversas aplicaciones científicas y matemáticas.

## 5. ¿Cuáles son las funciones universales de numpy y cómo se aplican a los arrays?
Las funciones universales (universal functions o ufuncs) de NumPy son funciones que operan elemento a elemento en arreglos, lo que las hace muy eficientes para realizar cálculos rápidos y vectorizados en grandes conjuntos de datos. Estas funciones aprovechan la capacidad de NumPy de realizar operaciones de manera eficiente en arreglos multidimensionales.

Las ufuncs de NumPy ofrecen varias ventajas:

- **Vectorización:** Las ufuncs aplican automáticamente una operación a cada elemento de un arreglo, eliminando la necesidad de iterar manualmente sobre los elementos. Esto permite un código más conciso y legible.

- **Eficiencia:** Las ufuncs están implementadas en C, lo que les permite aprovechar la eficiencia y rapidez de ejecución de este lenguaje. Esto significa que las operaciones se ejecutan de manera más rápida en comparación con el uso de bucles en Python puro.

- **Broadcasting:** Las ufuncs también aprovechan el mecanismo de broadcasting de NumPy, que permite realizar operaciones entre arreglos de diferentes tamaños y formas. Esto simplifica las operaciones entre arreglos y evita la necesidad de expandir manualmente las dimensiones.

Las ufuncs de NumPy cubren una amplia gama de operaciones matemáticas y funciones especiales, incluyendo:

- **Funciones matemáticas básicas:** suma (`np.add()`), resta (`np.subtract()`), multiplicación (`np.multiply()`), división (`np.divide()`), exponenciación (`np.power()`), logaritmos (`np.log()`, `np.log10()`, etc.), trigonometría (`np.sin()`, `np.cos()`, `np.tan()`), entre otras.

- **Funciones estadísticas:** suma acumulada (`np.cumsum()`), producto acumulado (`np.cumprod()`), promedio (`np.mean()`), mediana (`np.median()`), desviación estándar (`np.std()`), varianza (`np.var()`), entre otras.

- **Funciones de comparación y lógicas:** igualdad (`np.equal()`), desigualdad (`np.not_equal()`), mayor que (`np.greater()`), menor que (`np.less()`), operaciones lógicas (`np.logical_and()`, `np.logical_or()`, `np.logical_not()`), entre otras.

- **Funciones trigonométricas y hiperbólicas:** seno (`np.sin()`), coseno (`np.cos()`), tangente (`np.tan()`), arcseno (`np.arcsin()`), arcocoseno (`np.arccos()`), arcotangente (`np.arctan()`), sinh (`np.sinh()`), cosh (`np.cosh()`), tanh (`np.tanh()`), entre otras.

Estos son solo algunos ejemplos de las ufuncs disponibles en NumPy. Las ufuncs son una parte fundamental de NumPy y su uso es esencial para realizar operaciones eficientes y vectorizadas en arreglos de NumPy.