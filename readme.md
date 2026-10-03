# 🌱 AtlaIA: Optimización de Cultivos de Sorgo mediante IoT y Machine Learning

[![Python](https://img.shields.io/badge/Python-3.14%2B-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Machine%20Learning-Random%20Forest-orange.svg)](https://scikit-learn.org/)
[![Status](https://img.shields.io/badge/Status-En%20Desarrollo-success.svg)]()

> **AtlaIA** es una solución tecnológica e innovadora diseñada para el sector agrícola, enfocada específicamente en la optimización del cultivo de **sorgo forrajero**. Combina el monitoreo ambiental en tiempo real (IoT) con un modelo predictivo de Machine Learning y un soporte biológico radicular (micorrizas y PGPB) para garantizar un **35% de ahorro hídrico** y maximizar el rendimiento del suelo.

---

## 🚀 Descripción del Proyecto

En las regiones áridas y semiáridas (como Querétaro), la agricultura enfrenta una enorme volatilidad climática y un desperdicio crítico de recursos hídricos debido al riego tradicional basado en estimaciones empíricas. 

AtlaIA resuelve este problema mediante un enfoque de tres capas:
1. **Hardware / IoT (Los Ojos):** Nodos sensores basados en microcontroladores (ESP32) que miden temperatura, humedad relativa y condiciones del suelo en tiempo real.
2. **Biología (El Soporte Físico):** Inoculación de micorrizas y bacterias promotoras del crecimiento vegetal (PGPB) para crear una red simbiótica subterránea que retiene la humedad de manera natural en la raíz.
3. **Machine Learning (El Cerebro):** Un modelo predictivo que analiza el comportamiento ambiental y la viabilidad del cultivo para anticipar riesgos de estrés hídrico y optimizar la toma de decisiones.

---

## 📊 Dataset y Workflow de Machine Learning

El proyecto utiliza un pipeline analítico desarrollado en **Jupyter Notebook**, empleando un dataset de clasificación de crecimiento de plantas obtenido directamente de **Kaggle** (`gorororororo23/plant-growth-data-classification`).

### Variables Analizadas
* **Variables de Entrada (Features):** 
  * `Soil_Type` (Tipo de suelo: arcilloso, arenoso, franco, etc.)
  * `Sunlight_Hours` (Horas de exposición solar)
  * `Water_Frequency` (Frecuencia de riego)
  * `Fertilizer_Type` (Insumos: químico, orgánico/biológico, o ninguno)
  * `Temperature` (°C)
  * `Humidity` (%)
* **Variable Objetivo (Target):**
  * `Growth_Milestone` (Binario: `0` = Fracaso / Estrés severo, `1` = Éxito / Hito de crecimiento óptimo).

### Algoritmo Implementado
Se implementó un modelo de **Random Forest Classifier** (`n_estimators=100`) para evaluar la correlación entre las condiciones ambientales inestables y el éxito del cultivo. La línea base actual demuestra la alta volatilidad de los suelos sin control tecnológico, justificando la intervención directa de la biotecnología y el monitoreo automatizado de AtlaIA.

---

## 🛠️ Librerías de Python Utilizadas

El desarrollo del modelo, preprocesamiento de datos y visualización analítica se apoya en las siguientes librerías del ecosistema de Python:

* `pandas`: Manipulación, limpieza y estructuración de los datos tabulares.
* `numpy`: Operaciones matemáticas y numéricas eficientes.
* `scikit-learn`: Implementación del preprocesamiento (`LabelEncoder`), división de datos (`train_test_split`) y entrenamiento del modelo (`RandomForestClassifier`).
* `matplotlib` & `seaborn`: Generación de diagramas de dispersión y gráficos estadísticos para la validación agronómica.

---

## 📈 Visualizaciones Clave

El sistema genera análisis gráficos automatizados para validar el impacto agronómico:
* **Temperatura vs. Humedad:** Visualiza la dispersión de puntos críticos donde la planta entra en estrés hídrico frente a los rangos óptimos de supervivencia.
* **Impacto por Tipo de Insumo:** Compara estadísticamente el rendimiento entre fertilizantes químicos, ausencia de insumos y alternativas orgánicas/biológicas, demostrando la superioridad del consorcio microbiano.

---

## 👥 Autores y Competencia

* **Proyecto:** Participante en el concurso de innovación agrícola **Innodrop 2026**.
* **Desarrollo Técnico y Ciencia de Datos:** Equipo **AtlaIA**.