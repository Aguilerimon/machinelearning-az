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