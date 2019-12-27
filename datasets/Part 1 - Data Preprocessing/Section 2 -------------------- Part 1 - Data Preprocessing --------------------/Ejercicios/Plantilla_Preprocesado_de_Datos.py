# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 15:21:50 2019

@author: Aguilerimon
"""

import numpy as np
import matplotlib.pyplot as ptl
import pandas as pd

#Importar el data set
dataset = pd.read_csv('Data.csv')

#Separamos las variables del data set

#Localizacion de los elementos por localizacion (index)

#Asignamos a la variable x todas las filas de las tres primeras columnas como 
#variables independientes del data set
x = dataset.iloc[:,:-1].values

#Asignamos a la variable y todas las filas de la ultima columna como variable dependiente
y = dataset.iloc[:, 3].values

#Tratamiento de los NAs o valores faltantes
from sklearn.preprocessing import Imputer

#Especificamos todos los terminos necesarios para el tratamiento de los NAs
imputer = Imputer(missing_values = "NaN", strategy = "mean", axis = 0)

imputer = imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])

#Codificar los datos categóricos
#Import de las librerias LabelEncoder(Le da igual si los datos son catogórico u ordinales)
#Y la libreria OneHotEncoder(Implementación de las variable dummy categóricas)
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

#Constructor del método labelencoder
labelencoder_x = LabelEncoder()
labelencoder_y = LabelEncoder()

#Aplicamos la transformación numérica a la primer columna y la sobreescribimos al objeto x
x[:,0] = labelencoder_x.fit_transform(x[:,0])

#Para los valores boolean no nos interesa utilizar el método OneHotEncoder 
y = labelencoder_y.fit_transform(y)

#Es necesario haber tratado anteriormente el vector con LabelEncoder
#debido a que OneHotEncoder no podrá convertir el string original a float
onehotencoder = OneHotEncoder(categorical_features=[0])
x = onehotencoder.fit_transform(x).toarray()

#Dividir el dataset en un conjunto de entrenamiento y de evaluación
#Importamos la sublibreria train_test_split
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size= 0.2, random_state=0)

#Escalado de variables
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)