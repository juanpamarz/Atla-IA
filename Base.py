import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
df = pd.read_csv ("C:\\Users\\jpma2\\Documents\\INNODROP\\DATASET_MUESTRA.csv")
#Muestra de solo las primeras 5 filas de los datos 
print (df.head())
print (df.describe)

