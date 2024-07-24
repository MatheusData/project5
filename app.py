import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp
import streamlit as st 
import plotly.express as px

from pathlib import Path

car_data = pd.read_csv(Path("../Data/vehicles.csv"))


fig= px.histogram(car_data, x= "odometer",title= 'Count x Odometer')
st.title('Histograma com relação entre quantidade de veículos e suas quilometragens')
st.plotly_chart(fig)



fig = px.scatter(car_data, x="odometer", y="price", title= 'Odometer x Price')
st.title('Grafico de dispersão com relação entre preço dos veiculos e suas quilometragens')
st.plotly_chart(fig)



hist_button = st.button('Criar histograma')
     
if hist_button: 
         
         st.write('Criando um histograma com relação entre quantidade de veículos e suas quilometragens')
         
         fig = px.histogram(car_data, x="odometer")
     
         st.plotly_chart(fig, use_container_width=True)