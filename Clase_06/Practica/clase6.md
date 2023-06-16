# Resolución de ejericcios de la clase 6

- [Consignas](actividad_2.py)

## 1. Configurar el entorno virtual
- Se debe crear un ambiente virtual
```
python -m venv env
```

- Activar entorno virtual
```
source env/bin/activate
```

## 2. Instalar [Pandas](https://pandas.pydata.org/pandas-docs/stable/reference/index.html)
Se debe tener activado el ambiente virtual y estar en la ruta del proyecto, luego ejecutar el comando
```
pip install matplotlib
```

## 3. Importar librerías
Al principio del archivo, agregar el import
```
import pandas as pd
```
> Ahora se puede trabajar con las consignas y para ejecutar el archivo, ejecutar `python actividad_3.py`

## 4. Resolución de los ejercicios
1. Antes de comenzar, se deben importar los datos de una fuente, en este caso se importan los datos desde un archivo csv
    ```
    df = pd.read_csv("datos.csv")
    ```
    El método `read_csv()` recibe como parámetro la ubicación del arvhivo a leer y devuelve como resultado el esquema mapeado, que se puede guardar en una variable

2. Para obtener los primeros 5 registros, se utiliza el método `head()` y se puede motrar por consola con `print()`

3. Para obtener los últimos 5 registros, se utiliza el método `tail()` y también se puede motrar por consola con `print()`

4. El atributo `shape` es para obener la cantidad de filas y columnas

5. El método `describe()` obtiene la información estadística

6. Con el método `loc()` se pueden filtrar registos que cumplan cieta condición y se obtiene como resultado un nuevo set de datos que puede. En el punto 6 del ejercicio se obtienen todas las filas que coninciden en su nombre

7. Se utiliza el método `loc()` nuevamente para filtrar datos, esta vez comparando números

8. En esta oportunidad se combinan las comparaciones con el médotdo `loc()`, que deben estar separadas por paréntesis

9. Para eliminar, se utiliza el método `drop()` que requiere de dos argumentos: aquello que se desea eliminar y el **axis**, o bien el *eje* (1:para columna; 0: para fila)

10. Si se busca eliminar campos duplicados, se utiliza el método `drop_duplicates()` y se debe especificar en el parámetros en que columna buscar los duplicados