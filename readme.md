# Sistema Integral Enfocado Principalmente en el Cuidado y Ahorro del Agua, Mitigación de la Degradación de Suelos y Optimización Agrícola mediante Biotecnología Simbiótica, Sensores IoT y Machine Learning

**Institución:** Universidad Autónoma de Querétaro

> El propósito fundamental y eje rector de este proyecto es el **cuidado, ahorro y conservación masiva del agua**. La agricultura actual enfrenta una crisis severa debido al desperdicio hídrico extremo y a la degradación de los suelos cultivables por el uso intensivo de agroquímicos. Para resolver esta problemática, el sistema integra tecnología y biología con la misión prioritaria de blindar y optimizar el recurso hídrico frente a la severa variabilidad climática, superando simultáneamente los altos costos de los fertilizantes de síntesis química y la falta de monitoreo en tiempo real.

---

## El Cuidado del Agua como Eje Central de la Problemática

El recurso hídrico es el elemento más vulnerable y desperdiciado en los sistemas agrícolas tradicionales, generando una crisis que este proyecto busca erradicar:
* La degradación masiva de los suelos agrícolas destruye su estructura y reduce drásticamente su capacidad natural de retención de humedad, obligando a realizar riegos constantes, empíricos y altamente ineficientes.
* El uso descontrolado de agua y fertilizantes sintéticos provoca una baja asimilación de nutrientes, altos costos de producción y la contaminación directa de los mantos acuíferos adyacentes por lixiviación.
* Los pequeños y medianos agricultores se enfrentan a una vulnerabilidad extrema ante las sequías y la escasez global de agua.

Para garantizar la máxima eficiencia y protección hídrica, implementamos una solución tecnológica cuyo fin primordial es lograr un alto porcentaje de ahorro en el consumo de agua.

---

## Arquitectura de la Solución para la Conservación del Agua

1. **Soporte Biológico Radicular para Retención Hídrica:** Introducción de consorcios microbianos (hongos micorrizógenos arbusculares y bacterias promotoras del crecimiento vegetal) que establecen una simbiosis con la raíz, formando una red subterránea que retiene de manera natural la humedad y mejora la estabilidad física del suelo.
2. **Monitoreo IoT en Tiempo Real:** Captura continua de variables críticas del suelo (humedad volumétrica, temperatura y conductividad eléctrica) mediante una red de sensores de bajo costo, eliminando el riego empírico y permitiendo suministrar agua únicamente cuando el cultivo lo requiere de forma exacta.
3. **Machine Learning Predictivo:** Algoritmos de aprendizaje automático que procesan de manera continua las variables ambientales del suelo para predecir las ventanas óptimas de absorción, anticipar el estrés hídrico antes de que dañe el sistema vegetal y maximizar la eficiencia en el uso del agua.

---

## Dataset y Pipeline de Análisis

El modelo analítico se desarrolló en un entorno de **Jupyter Notebook**, utilizando un dataset de clasificación de crecimiento de plantas obtenido de la plataforma **Kaggle** (`gorororororo23/plant-growth-data-classification`).

### Variables del Modelo
* **Variables de entrada (Features):** Tipo de suelo (`Soil_Type`), horas de sol (`Sunlight_Hours`), frecuencia de riego (`Water_Frequency`), tipo de insumo (`Fertilizer_Type`), temperatura (`Temperature`) y humedad relativa (`Humidity`).
* **Variable objetivo (Target):** Indicador de hito de crecimiento exitoso o estrés en el cultivo (`Growth_Milestone`).

### Algoritmo Implementado
Se implementó un modelo de **Random Forest Classifier** (`n_estimators=100`) para evaluar las condiciones ambientales inestables y establecer una línea base cuantitativa que demuestra la alta volatilidad de los suelos sin control inteligente, justificando la necesidad imperativa de incorporar la biotecnología y la automatización para salvaguardar el recurso hídrico.

---

## Librerías de Python Utilizadas

* `pandas`: Manipulación y estructuración de los datos tabulares.
* `numpy`: Procesamiento numérico y operaciones matriciales.
* `scikit-learn`: Preprocesamiento (`LabelEncoder`), partición de datos (`train_test_split`) y entrenamiento del modelo (`RandomForestClassifier`).
* `matplotlib` y `seaborn`: Generación de gráficos estadísticos y visualización analítica.

---

## Impacto Principal en el Recurso Hídrico y Ambiental

* **Conservación y Ahorro Hídrico (Prioridad Máxima):** Garantía de una eficiencia optimizada en el consumo de agua mediante la combinación sinérgica de retención biológica en la raíz y riego inteligente guiado por datos, protegiendo las reservas de agua locales y subterráneas.
* **Ecológico:** Regeneración de la salud del suelo, disminución de la huella de carbono y prevención absoluta de la lixiviación de nutrientes hacia los mantos acuíferos adyacentes.
* **Económico y Productivo:** Reducción drástica en los costos de producción por la sustitución parcial de fertilizantes sintéticos y optimización de los volúmenes de riego utilizados en el sistema agrícola.
