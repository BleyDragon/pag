import pandas as pd
import streamlit as st
import utilidades as util
#Configurar la pagina principal
st.set_page_config(
    page_title="Análisis de Siniestros de Motociclistas",
    page_icon=":racing_motorcycle:",
    initial_sidebar_state="auto",
    layout="centered"
)

#llamamos el menú
util.generarMenu()

st.title("Análisis de Siniestros de Motociclistas: Un Enfoque Data-Driven")

st.write("""Este proyecto aborda el problema de la siniestralidad de motociclistas en Colombia utilizando técnicas avanzadas de análisis de datos, modelos predictivos y prescriptivos. Se busca desarrollar una solución innovadora para reducir los riesgos y mejorar la seguridad.
""")


#Ponemos una imagen a nuestra pagina
from PIL import Image
#habrimos la imagen
imagen = Image.open("media/imagen.jpg")
#incrustamos la imagen
st.image(imagen, caption="",
         use_container_width=True,width=700)

hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style> 
        """
st.markdown(hide_streamlit_style,unsafe_allow_html=True)
st.header("Problema a resolver")
st.write("""El aumento de la siniestralidad de motociclistas y la necesidad urgente de políticas públicas para reducirla.

Las motocicletas en Colombia son esenciales para el transporte, pero la accidentalidad es alarmante.

Se estima que seis de cada diez muertes en accidentes de tránsito son de motociclistas (Agencia Nacional de Seguridad Vial).

""")
