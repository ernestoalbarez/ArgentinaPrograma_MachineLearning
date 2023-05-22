# Clase 3
Trabajo con ambientes virtuales y librerías

## Configurar ambiente virtual
- Crear entorno virtual `python3 -m venv <mi_entorno_virtual>`
```
python3 -m venv env
```
> `env` es el nombre del entorno
- Activar entorno virtual `source mi_entorno_virtual/bin/activate`
```
source env/bin/activate
```
> Ahora el terminal comienza con `(mi_entorno_virtual)`, con el comando `deactivate` se desactiva el entorno virtual
## Instalar librerías: matplotlib
Se debe tener activado el ambiente virtual y estar en la ruta del proyecto, luego ejecutar el comando
```
pip install matplotlib
```
### Trabajar con la librería
Se pueden utilizar ejemplos de la [web oficial](https://matplotlib.org/stable/gallery/index.html), y pegarlos en un nuevo archivo `.py`. Luego ejecutar normalmente con `python3 ejemplo.py`

> matplotlib no muestra imagenes en Ubuntu, por lo tanto el comando `plt.show()` no tendrá resultados. Por este motivo, el comando `plt.savefig("img.png")` guardará una imagen en la carpeta del proyecto