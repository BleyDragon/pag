import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score, confusion_matrix, ConfusionMatrixDisplay
import utilidades as util
from pickle import dump, load
import numpy as np
import plotly.express as px

# Configurar la página principal
st.set_page_config(
    page_title=" Análisis de Siniestros",
    page_icon=":racing_motorcycle:",
    layout="wide",  # Layout amplio para aprovechar toda la pantalla
    initial_sidebar_state="expanded"
)

# Llamar el menú
util.generarMenu()

# Título principal
st.title("Análisis de Siniestros de Motociclistas")

# Espaciado entre secciones
st.markdown("---")

# Mostrar el reporte de Power BI con un iframe responsivo
st.header("Visualización de Reporte en Power BI")

st.markdown(
    """
    <style>
    /* CSS para hacer el iframe responsivo */
    .responsive-iframe-container {
        position: relative;
        width: 100%;
        padding-top: 56.25%; /* Relación de aspecto 16:9 */
    }
    .responsive-iframe-container iframe {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        border: none;
    }
    </style>
    <div class="responsive-iframe-container">
        <iframe src="https://app.powerbi.com/view?r=eyJrIjoiZmI3NWM5ZTgtM2Y2Zi00OGYzLTkwZWUtYTk2ZTNlZmMxZjkzIiwidCI6ImU0NzQ5NGEwLTQ5MDMtNGQ2YS05NDk5LWY1YWEyZmM0NTliNiJ9" 
                allowfullscreen>
        </iframe>
    </div>
    """,
    unsafe_allow_html=True
)








