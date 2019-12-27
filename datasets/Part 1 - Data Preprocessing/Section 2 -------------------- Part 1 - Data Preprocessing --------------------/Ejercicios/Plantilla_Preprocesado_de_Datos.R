# Plantilla para el pre Procesado de Datos
# Importar el dataset
dataset = read.csv('Data.csv')

#Tratamiento de los valores NA
dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age, FUN = function(x) mean(x,na.rm = TRUE)), 
                     dataset$Age)

dataset$Salary = ifelse(is.na(dataset$Salary),
                     ave(dataset$Salary, FUN = function(x) mean(x,na.rm = TRUE)), 
                     dataset$Salary)

#Codificar variables categóricas
dataset$Country = factor(dataset$Country,
                         levels = c("France", "Spain", "Germany"),
                         labels = c(1, 2, 3))

dataset$Purchased = factor(dataset$Purchased,
                           levels = c("No", "Yes"),
                           labels = c(0, 1))

#Dividir los datos en conjunto de entrenamiento y evaluación
#Importamos la libreria para separar los conjuntos
library(caTools)

#Especificamos el numero de repeticiones del algoritmo (Puede ser cualquiera)
set.seed(123)

#Devuelve un vector del mismo tamaño que la variable o vector que se le da
#indicando si debe formar parte del conjunto de entrenamiento
split = sample.split(dataset$Purchased, SplitRatio = 0.8)

#Separa y almacena en dos diferentes variables los conjuntos de 
#entrenamiento y evaluación
training_set = subset(dataset, split==TRUE)
testing_set = subset(dataset, split==FALSE)

#Escalado de variables
training_set[,2:3] = scale(training_set[,2:3])
testing_set[,2:3] = scale(testing_set[,2:3])