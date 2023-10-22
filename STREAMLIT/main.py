import streamlit as st
import pandas as pd

st.title('Calculadora de Estadísticas con Streamlit')

# Campo de carga de archivos
archivo = st.file_uploader('Cargue un archivo Excel', type=['xls', 'xlsx'])

if archivo is not None:
    # Leer el archivo Excel y cargar los datos en un DataFrame de pandas
    df = pd.read_excel(archivo, sheet_name='Datos')

    st.subheader('Datos del archivo:')
    st.write(df)

    # Seleccionar la columna para calcular estadísticas
    columna = st.selectbox('Seleccione una columna:', df.columns)

    st.subheader('Resultados de estadísticas:')
    st.write(f'Media: {df[columna].mean()}')
    st.write(f'Mediana: {df[columna].median()}')
    st.write(f'Desviación Estándar: {df[columna].std()}')
