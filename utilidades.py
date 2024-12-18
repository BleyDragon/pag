import streamlit as st
import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score, confusion_matrix, ConfusionMatrixDisplay
import utilidades as util
from pickle import dump
from pickle import load
import numpy as np


def generarMenu():
    with st.sidebar:
        st.header('Análisis de Siniestros de Motociclistas')
        st.page_link('Home.py', label='Inicio', icon='🏠')
      #  st.page_link('pages/Pronostico.py', label='Pronóstico SMEC', icon='💚')
        st.page_link('pages/graficos.py', label='Gráficas', icon='📊')


#Función del modelo predictivo
def modelo_rf(df_pacientes_rf):
    #Variable a predeci
    Y = df_pacientes_rf.iloc[:,0]
    #Variables predictoras
    X = df_pacientes_rf.iloc[:,1:11] 
    #Variables de prueba  ->  prueba
    #Variables de entrenamiento -> entrenar
    X_entrenar, X_prueba, Y_entrenar, Y_prueba = train_test_split(X, Y, train_size=0.8, random_state=0)
    
    st.markdown('-Separamos los datos')
    st.write('Set de entrenamiento')
    st.info(X_entrenar.shape)
    st.write('Set de eprueba')
    st.info(X_prueba.shape)
    st.markdown('-Detalles de las variables')
    st.write('Variables Predictoras')
    st.info(list(X.columns))
    st.write('Variable a Predecir')
    st.info(Y.name)
       
    #Creamos el bosque
    bosque = RandomForestClassifier()
    #entrenamos el bosque
    bosque.fit(X_entrenar,Y_entrenar)
   
    st.subheader('**Características del modelo')
    st.markdown('-Set de Prueba')
    #Hacemos la predicción
    Y_prediccion = bosque.predict(X_prueba)
    accuracy = accuracy_score(Y_prueba,Y_prediccion)
    st.write('Accuracy:')
    st.info(accuracy)
    #Parámetros
    st.subheader('**Parámetros del modelo')
    st.write(bosque.get_params())
    #Guardamos el modelo
    archivo_modelo = open('data\modelo_rf.sav', 'wb')
    dump(bosque, archivo_modelo)
    archivo_modelo.close()

