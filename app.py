import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') #lendo os dados
hist_button = st.button('Criar histograma') #criar um botão

if hist_button: #se o botão for clicado
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)


car_data = pd.read_csv('vehicles_us.csv') # lendo os dados

# Criar botão para o gráfico de dispersão
scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button: # Se o botão for clicado
    st.write('Criando um gráfico de dispersão para odometer vs price') # Escrever uma mensagem
    
    # Criar o gráfico de dispersão
    fig = px.scatter(car_data, x="odometer", y="price")
    
    # Exibir o gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)