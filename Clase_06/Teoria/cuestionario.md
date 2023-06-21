
# Cuestionario guia de lectura del material
Este es un cuestionario guía de cinco preguntas sobre algoritmos de Machine Learning. El
objetivo es evaluar su nivel de conocimiento y comprensión de los conceptos básicos de esta
disciplina.

Las preguntas son las siguientes:

## 1. ¿Qué es un algoritmo de Machine Learning y para qué sirve?
Un algoritmo de aprendizaje automático (Machine Learning) es una serie de pasos y reglas que se utilizan para enseñar a una computadora a realizar una tarea específica basada en datos y experiencias pasadas. Estos algoritmos permiten a las máquinas aprender patrones y tomar decisiones o hacer predicciones sin ser programadas explícitamente para cada escenario.

El objetivo principal de los algoritmos de aprendizaje automático es aprender a partir de los datos y generar modelos o funciones matemáticas que puedan generalizar y realizar predicciones o tomar decisiones en nuevos datos no vistos previamente. Estos algoritmos buscan identificar patrones y relaciones en los datos de entrenamiento para poder hacer inferencias o tomar acciones en datos nuevos o futuros.

Los algoritmos de aprendizaje automático se utilizan en una amplia variedad de aplicaciones, incluyendo:

- **Clasificación:** Los algoritmos de clasificación se utilizan para asignar una categoría o etiqueta a un conjunto de datos basándose en patrones identificados en los datos de entrenamiento. Por ejemplo, clasificar correos electrónicos como spam o no spam, clasificar imágenes como gato o perro, o clasificar transacciones bancarias como fraudulentas o legítimas.

- **Regresión:** Los algoritmos de regresión se utilizan para predecir valores numéricos continuos basados en datos históricos. Por ejemplo, predecir el precio de una casa en función de características como el tamaño, el número de habitaciones y la ubicación, o predecir la demanda de productos en función de variables como el precio y la publicidad.

- **Agrupamiento:** Los algoritmos de agrupamiento se utilizan para identificar grupos o segmentos en un conjunto de datos sin etiquetas previas. Estos algoritmos buscan agrupar elementos similares y separar elementos diferentes basándose en similitudes o patrones identificados en los datos. Por ejemplo, agrupar clientes según su comportamiento de compra o agrupar documentos según su contenido.

- **Anomalía o detección de anomalías:** Los algoritmos de detección de anomalías se utilizan para identificar patrones o instancias inusuales o anormales en un conjunto de datos. Estos algoritmos son útiles para detectar fraudes, anomalías médicas o cualquier otro comportamiento atípico que pueda ser relevante en un contexto específico.

- **Recomendación:** Los algoritmos de recomendación se utilizan para proporcionar recomendaciones personalizadas a los usuarios basadas en sus preferencias o comportamiento pasado. Estos algoritmos se utilizan comúnmente en sistemas de recomendación de películas, música, productos de compras en línea, entre otros.

Estos son solo algunos ejemplos de las aplicaciones de los algoritmos de aprendizaje automático. En resumen, los algoritmos de aprendizaje automático son herramientas poderosas que permiten a las máquinas aprender de los datos y realizar tareas como clasificación, regresión, agrupamiento y detección de anomalías sin requerir una programación explícita para cada caso individual.

## 2. ¿Qué diferencia hay entre aprendizaje supervisado y no supervisado?
La diferencia principal entre el aprendizaje supervisado y el aprendizaje no supervisado radica en la presencia o ausencia de datos etiquetados durante el proceso de aprendizaje:

- **Aprendizaje supervisado:** En el aprendizaje supervisado, el conjunto de datos utilizado para el entrenamiento incluye tanto las características de entrada como sus correspondientes etiquetas de salida.
El objetivo es aprender una relación o mapeo entre las características de entrada y las etiquetas de salida, basándose en los ejemplos etiquetados proporcionados.
El modelo entrenado puede luego hacer predicciones o clasificar nuevos datos de entrada no vistos, mapeándolos a los patrones aprendidos a partir de los datos etiquetados.
Ejemplos de algoritmos de aprendizaje supervisado incluyen regresión lineal, regresión logística, árboles de decisión, bosques aleatorios, máquinas de vectores de soporte (SVM) y redes neuronales.

- **Aprendizaje no supervisado:** En el aprendizaje no supervisado, el conjunto de datos utilizado para el entrenamiento consiste únicamente en características de entrada sin etiquetas de salida correspondientes.
El objetivo es encontrar patrones, estructuras o relaciones dentro de los datos sin la guía de etiquetas de salida conocidas.
Los algoritmos de aprendizaje no supervisado buscan descubrir patrones ocultos, agrupar instancias similares o reducir la dimensionalidad de los datos.
La agrupación y la reducción de dimensionalidad son tareas comunes en el aprendizaje no supervisado.
Ejemplos de algoritmos de aprendizaje no supervisado incluyen el agrupamiento k-means, el agrupamiento jerárquico, el análisis de componentes principales (PCA) y modelos generativos como los modelos de mezcla gaussiana (GMM) y los autoencoders.

En resumen, el aprendizaje supervisado se basa en datos etiquetados para aprender la relación entre las características de entrada y las etiquetas de salida, mientras que el aprendizaje no supervisado explora la estructura y los patrones inherentes en datos no etiquetados sin utilizar etiquetas de salida conocidas.

## 3. ¿Qué son las características y las etiquetas en un conjunto de datos?
- **Características (Features):** Las características, también conocidas como variables de entrada o variables independientes, son las características medibles o atributos de los datos que se utilizan como entrada para un modelo de aprendizaje automático.
Las características representan los datos de entrada sobre los cuales el modelo hará predicciones o aprenderá patrones.
Ejemplos de características pueden ser valores numéricos (por ejemplo, edad, temperatura), valores categóricos (por ejemplo, color, categoría de producto), datos textuales (por ejemplo, descripción de texto) o cualquier otro dato relevante que describa la entrada.

- **Etiquetas (Labels):** Las etiquetas, también conocidas como variables de salida o variables dependientes, son los valores objetivo o los resultados esperados que el modelo de aprendizaje automático va a predecir o clasificar.
Las etiquetas representan la salida deseada o la verdad fundamental asociada a los datos de entrada.
En el aprendizaje supervisado, el conjunto de datos incluye tanto las características como sus etiquetas correspondientes.
Ejemplos de etiquetas pueden ser etiquetas de clase (por ejemplo, spam/no spam, positivo/negativo), valores numéricos (por ejemplo, precios de casas, precios de acciones) o cualquier otro dato relevante que represente la predicción o clasificación deseada.

La relación entre las características y las etiquetas es la base del aprendizaje supervisado. El modelo de aprendizaje automático aprende patrones y relaciones a partir de los ejemplos proporcionados (características y etiquetas correspondientes) durante la fase de entrenamiento. Una vez entrenado, el modelo puede generalizar y hacer predicciones o clasificaciones sobre nuevos datos no vistos, basándose en los patrones aprendidos a partir de los datos etiquetados.

Es importante tener en cuenta que en el aprendizaje no supervisado, donde no se proporcionan etiquetas, el conjunto de datos consiste únicamente en características sin etiquetas correspondientes. En este caso, el objetivo es descubrir patrones, estructuras o relaciones dentro de los datos sin la guía de etiquetas de salida conocidas.

## 4. ¿Qué es el sobreajuste y cómo se puede evitar?
El sobreajuste (overfitting en inglés) ocurre cuando un modelo de aprendizaje automático se ajusta demasiado a los datos de entrenamiento, de manera que pierde su capacidad de generalizar correctamente en datos nuevos o no vistos. Sucede cuando el modelo captura ruido o patrones irrelevantes en los datos de entrenamiento que no se generalizan bien.

Para evitar el sobreajuste, se pueden seguir las siguientes estrategias:

- **Aumentar los datos de entrenamiento:** Proporcionar más datos de entrenamiento diversos y representativos puede ayudar al modelo a aprender patrones generales en lugar de memorizar ejemplos específicos. Más datos reducen las posibilidades de sobreajuste.

- **Selección de características:** Seleccionar características relevantes e informativas puede evitar que el modelo se enfoque en datos irrelevantes o ruidosos. Ayuda a eliminar la complejidad innecesaria y mejorar la generalización.

- **Regularización:** Las técnicas de regularización añaden un término de penalización a la función objetivo del modelo para desalentar valores de parámetros excesivamente complejos o grandes. Esto ayuda a prevenir el sobreajuste al fomentar que el modelo generalice correctamente.

- **Validación cruzada:** Utilizar técnicas como la validación cruzada ayuda a evaluar el rendimiento del modelo en datos no vistos. Implica dividir los datos en múltiples pliegues, entrenar en un subconjunto y validar en los pliegues restantes. Proporciona una mejor estimación del rendimiento del modelo y ayuda a detectar el sobreajuste.

- **Detención temprana:** Durante el entrenamiento, se puede monitorear el rendimiento del modelo en un conjunto de validación. Si el rendimiento comienza a empeorar después de una mejora inicial, se puede detener el entrenamiento tempranamente para evitar el sobreajuste. Esta técnica evita que el modelo se ajuste demasiado a los datos de entrenamiento.

- **Métodos de conjunto:** Los métodos de conjunto combinan múltiples modelos para realizar predicciones, reduciendo el riesgo de sobreajuste. Técnicas como el bagging y el boosting pueden mejorar la generalización al combinar las predicciones de varios modelos.

- **Control de la complejidad del modelo:** Controlar la complejidad del modelo, como reducir el número de capas en una red neuronal o limitar la profundidad de un árbol de decisión, puede prevenir el sobreajuste. Los modelos más simples a menudo generalizan mejor.

Aplicando estas estrategias, se puede mitigar el sobreajuste y desarrollar modelos que tengan un buen rendimiento en datos no vistos, lo que conduce a una mejor generalización y mejores resultados de aprendizaje automático.

## 5. ¿Qué es la validación cruzada y cuál es su utilidad?
La validación cruzada (cross-validation en inglés) es una técnica utilizada en el aprendizaje automático para evaluar y validar el rendimiento de un modelo utilizando los datos disponibles. Su utilidad radica en proporcionar una estimación más confiable y realista del rendimiento del modelo en datos no vistos, en comparación con una simple división de los datos en conjuntos de entrenamiento y prueba.

El proceso de validación cruzada implica dividir el conjunto de datos en múltiples partes llamadas "folds" (pliegues). Luego, se realizan iteraciones en las que cada uno de los pliegues se utiliza como conjunto de prueba, mientras que los pliegues restantes se utilizan como conjunto de entrenamiento. Esto significa que el modelo se entrena y evalúa varias veces, cada vez utilizando diferentes combinaciones de pliegues como datos de entrenamiento y prueba.

La validación cruzada tiene varias ventajas:

- **Estimación más precisa:** Al evaluar el modelo en múltiples conjuntos de prueba diferentes, la validación cruzada proporciona una estimación más precisa del rendimiento del modelo en datos no vistos. Esto reduce la dependencia de una única partición de los datos y proporciona una medida más robusta de la capacidad del modelo para generalizar.

- **Utilización eficiente de los datos:** Al utilizar todos los datos disponibles tanto para entrenamiento como para evaluación, la validación cruzada aprovecha al máximo el conjunto de datos, especialmente cuando este es limitado. Esto evita desperdiciar datos valiosos que podrían haber quedado excluidos en una simple división en conjuntos de entrenamiento y prueba.

- **Detección de overfitting:** La validación cruzada ayuda a detectar el sobreajuste (overfitting) al evaluar el rendimiento del modelo en diferentes conjuntos de prueba. Si el modelo tiene un rendimiento excelente en el conjunto de entrenamiento pero un rendimiento inferior en los conjuntos de prueba, esto podría indicar que se ha producido un sobreajuste.

- **Selección de hiperparámetros:** La validación cruzada también es útil para la selección de hiperparámetros. Al probar diferentes combinaciones de valores de hiperparámetros en cada iteración de validación cruzada, se puede determinar la configuración óptima que maximice el rendimiento del modelo.

En resumen, la validación cruzada proporciona una evaluación más precisa y confiable del rendimiento del modelo en datos no vistos, utilizando eficientemente todos los datos disponibles. Es una técnica fundamental en el desarrollo de modelos de aprendizaje automático y ayuda a tomar decisiones informadas sobre la elección del modelo y la configuración de los hiperparámetros.