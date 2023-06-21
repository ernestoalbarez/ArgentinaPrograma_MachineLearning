# Cuestionario guia de lectura del material

- [Guia de Estudio](Machine Learning I Semana 03 - Guia de Estudio.pdf)
- [Clase 3 - YouTube](https://youtu.be/ucz4qhYV76s)

## 1. ¿Qué es matplotlib y para qué sirve?
Matplotlib es una biblioteca de visualización de datos muy popular en Python. Proporciona una amplia gama de funciones y herramientas para crear gráficos estáticos, gráficos interactivos, diagramas, histogramas, diagramas de dispersión y muchas otras visualizaciones.

Las principales características y usos de Matplotlib son:

**Creación de gráficos:** Matplotlib permite crear gráficos de alta calidad con una variedad de estilos y formatos. Puedes crear gráficos de líneas, gráficos de barras, gráficos de dispersión, gráficos de áreas, gráficos de torta, entre otros.

**Personalización y control:** Matplotlib ofrece un alto grado de personalización, lo que te permite ajustar y controlar todos los aspectos de tus gráficos, como colores, estilos de línea, etiquetas, leyendas, títulos, ejes, entre otros. Puedes crear visualizaciones a medida para adaptarse a tus necesidades específicas.

**Interactividad:** Matplotlib también proporciona funciones para crear gráficos interactivos. Puedes agregar funcionalidades como zoom, selección de puntos, ventanas emergentes de información, desplazamiento, etc., para permitir una exploración interactiva de tus datos.

**Compatibilidad con diversos formatos y plataformas:** Matplotlib puede generar gráficos en una amplia gama de formatos de salida, incluyendo PNG, JPG, PDF, SVG, entre otros. Además, es compatible con varias interfaces de usuario y entornos de desarrollo, como Jupyter Notebook, entornos de escritorio y aplicaciones web.

**Integración con otras bibliotecas:** Matplotlib se integra bien con otras bibliotecas de análisis de datos y aprendizaje automático en Python, como NumPy, Pandas y SciPy. Esto permite combinar las capacidades de visualización de Matplotlib con el análisis y procesamiento de datos de estas bibliotecas.

En resumen, Matplotlib es una biblioteca poderosa y flexible para visualización de datos en Python. Se utiliza ampliamente en el ámbito científico, de análisis de datos y aprendizaje automático para crear gráficos informativos y atractivos que ayudan a comprender y comunicar los datos de manera efectiva.

## 2. ¿Qué función se usa para crear un diagrama de dispersión con matplotlib?
Para crear un gráfico de dispersión (scatter plot) con Matplotlib, se utiliza la función `scatter()`. Esta función permite representar puntos individuales en un sistema de coordenadas cartesianas, donde cada punto se define por sus coordenadas x e y.

Aquí tienes la sintaxis básica de la función `scatter()`:
```
import matplotlib.pyplot as plt

plt.scatter(x, y, s=None, c=None, marker=None, cmap=None)
plt.xlabel('Etiqueta del eje x')
plt.ylabel('Etiqueta del eje y')
plt.title('Título del gráfico')
plt.show()
```

- `x`: Una secuencia de valores numéricos que representa las coordenadas x de los puntos del gráfico de dispersión.
- `y`: Una secuencia de valores numéricos que representa las coordenadas y de los puntos del gráfico de dispersión.
- `s` (opcional): Tamaño de los puntos en el gráfico. Puede ser un solo número o una secuencia que especifique el tamaño para cada punto.
- `c` (opcional): Color de los puntos en el gráfico. Puede ser un solo color o una secuencia que especifique el color para cada punto.
- `marker` (opcional): Tipo de marcador utilizado para representar los puntos en el gráfico. Por defecto, se utiliza el marcador 'o', que representa círculos.
- `cmap` (opcional): Colormap utilizado para asignar colores a los puntos en función de un valor numérico. Se utiliza cuando se especifica un valor para el parámetro c.

Además de estos parámetros, puedes personalizar el gráfico agregando etiquetas a los ejes x e y, un título al gráfico y ajustar otros aspectos visuales según tus necesidades.

Aquí tienes un ejemplo básico de cómo utilizar la función `scatter()` para crear un gráfico de dispersión:
```
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.scatter(x, y)
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.title('Gráfico de dispersión')
plt.show()
```

En este ejemplo, se proporcionan dos listas `x` e `y` que representan las coordenadas de los puntos en el gráfico de dispersión. Luego, se utiliza `plt.scatter(x, y)` para crear el gráfico de dispersión. Finalmente, se agregan etiquetas a los ejes y un título al gráfico antes de mostrarlo con `plt.show()`.

## 3. ¿Qué módulo de matplotlib ofrece una interfaz cómoda y sencilla para añadir elementos a los gráficos?
El módulo en Matplotlib que ofrece una interfaz conveniente y sencilla para agregar elementos a los gráficos se llama `pyplot`. Por lo general, se importa como `plt`.

El módulo `pyplot` de Matplotlib proporciona una interfaz de alto nivel para crear y modificar gráficos. Simplifica el proceso de creación de gráficos al ofrecer funciones para agregar elementos como líneas, marcadores, etiquetas, títulos, leyendas y más. Abstrae muchos de los detalles de bajo nivel, lo que te permite generar visualizaciones rápidamente con un código mínimo.

Aquí tienes un ejemplo que muestra el uso de `pyplot` para crear un gráfico sencillo:
```
import matplotlib.pyplot as plt

# Datos
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Crear el gráfico
plt.plot(x, y, marker='o')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Gráfico Simple')
plt.grid(True)

# Mostrar el gráfico
plt.show()
```

En este ejemplo, se utiliza el módulo `pyplot` para crear un gráfico. La función `plt.plot(x, y, marker='o')` se utiliza para trazar los puntos de datos con marcadores. Las funciones `plt.xlabel()`, `plt.ylabel()` y `plt.title()` se utilizan para agregar etiquetas a los ejes y un título al gráfico. La función `plt.grid(True)` agrega una cuadrícula al gráfico. Finalmente, se llama a `plt.show()` para mostrar el gráfico.

Al utilizar el módulo `pyplot`, puedes agregar y personalizar fácilmente varios elementos de tus gráficos, lo que lo convierte en una interfaz conveniente y sencilla para crear visualizaciones en Matplotlib.

## 4. ¿Cómo importar una librería al código Python?
Para importar una biblioteca en código Python, puedes utilizar la declaración `import` seguida del nombre de la biblioteca. Aquí tienes algunas formas comunes de importar bibliotecas:

- Importar toda la biblioteca:
    ```
    import nombre_de_la_biblioteca
    ```
    Con esta forma de importación, debes utilizar el nombre de la biblioteca seguido de un punto para acceder a sus funciones y clases. Por ejemplo: `nombre_de_la_biblioteca.funcion()`, `nombre_de_la_biblioteca.Clase()`.

- Importar la biblioteca con un alias:
    ```
    import nombre_de_la_biblioteca as alias
    ```
    Con esta forma de importación, puedes proporcionar un alias (nombre corto) para la biblioteca. Esto facilita el uso de sus funciones y clases. Por ejemplo: `alias.funcion()`, `alias.Clase()`.

- Importar una función o clase específica de la biblioteca:
    ```
    from nombre_de_la_biblioteca import funcion, Clase
    ```
    Con esta forma de importación, puedes importar una función o clase específica directamente. No es necesario utilizar el nombre de la biblioteca para acceder a ellas. Por ejemplo: `funcion()`, `Clase()`.

- Importar todas las funciones y clases de la biblioteca:
    ```
    from nombre_de_la_biblioteca import *
    ```

    Esta forma de importación importa todas las funciones y clases de la biblioteca directamente. Puedes acceder a ellas sin utilizar el nombre de la biblioteca. Sin embargo, ten en cuenta que esta forma puede ocasionar conflictos de nombres si hay funciones o clases con el mismo nombre en diferentes bibliotecas.

    Es importante tener en cuenta que, en general, es recomendable importar solo las funciones y clases necesarias en lugar de importar toda la biblioteca. Esto evita posibles conflictos de nombres y ayuda a mantener el código más legible y eficiente.

    Aquí tienes un ejemplo de cómo importar la biblioteca `math` y utilizar una de sus funciones:
    ```
    import math

    resultado = math.sqrt(25)
    print(resultado)
    ```

    En este ejemplo, se importa la biblioteca `math` utilizando la forma 1. Luego, se utiliza la función `sqrt()` de `math` para calcular la raíz cuadrada de 25 y se almacena en la variable `resultado`. Finalmente, se imprime el resultado en la consola.

## 5. ¿Cómo se puede guardar un gráfico creado con matplotlib en un archivo de imagen?
Para guardar un gráfico creado con Matplotlib en un archivo de imagen, puedes utilizar la función `savefig()` del módulo `pyplot`. Esta función te permite guardar el gráfico en varios formatos de archivo, como PNG, JPG, PDF, SVG, entre otros.

Aquí tienes la sintaxis básica de la función `savefig()`:

```
import matplotlib.pyplot as plt

# Código para crear y personalizar el gráfico

plt.savefig('ruta_del_archivo')
```

En el código anterior, después de crear y personalizar tu gráfico utilizando las funciones de `pyplot`, utilizas `plt.savefig('ruta_del_archivo')` para guardar el gráfico en un archivo de imagen. Debes proporcionar la ruta y el nombre del archivo que deseas guardar. Matplotlib reconocerá automáticamente la extensión del archivo y lo guardará en el formato correspondiente.

A continuación, se muestra un ejemplo de cómo guardar un gráfico como archivo PNG:
```
import matplotlib.pyplot as plt

# Datos
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Crear el gráfico
plt.plot(x, y)
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Gráfico Guardado')

# Guardar el gráfico como archivo PNG
plt.savefig('grafico.png')
```

En este ejemplo, se utiliza `plt.savefig('grafico.png')` para guardar el gráfico en un archivo llamado "grafico.png". Puedes especificar la ruta completa del archivo si deseas guardarlo en un directorio específico.

Recuerda que debes llamar a `savefig()` después de haber personalizado tu gráfico y antes de llamar a `plt.show()` o cerrar la figura. De lo contrario, el gráfico no se guardará correctamente.

Al guardar el gráfico como un archivo de imagen, podrás utilizarlo posteriormente en informes, presentaciones o cualquier otro contexto donde necesites compartir o utilizar la visualización generada por Matplotlib.