import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

st.header('Vehicles')  # crear un encabezado
# crear una casilla de verificacion
hist_build = st.checkbox('Construir histograma')

if hist_build:  # si la casilla de verificación está seleccionada
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# crear una casilla de verificacion
disp_build = st.checkbox('Construir grafico de dispersion')

if disp_build:  # si la casilla de verificación está seleccionada
    # escribir un mensaje
    st.write(
        'Creación de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')

    # crear un grafico de dispersion
    fig = px.scatter(car_data, x="odometer", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
