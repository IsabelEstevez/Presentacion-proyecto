import streamlit as st

# Configurar página
st.set_page_config(
    page_title="Bienvenidos",
    page_icon="👋",
)

# Título principal centrado
st.markdown("""
<svg width="600" height="50">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:rgb(0,0,0);stop-opacity:1" />
      <stop offset="50%" style="stop-color:rgb(255,0,0);stop-opacity:1" />
    <stop offset="100%" style="stop-color:rgb(0,0,0);stop-opacity:1" />
    </linearGradient>
  </defs>
  <text x="55%" y="40" fill="url(#grad1)" font-size="40" text-anchor="middle" font-weight="bold">CONTEXTO DEL PROYECTO</text>
</svg>
""", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# Tamaño de texto y alineación centrada
st.markdown("""Nuestro proyecto de fin del bootcamp Data Science y Machine Learning de 4Geeks está basado en la **base de datos de un banco**, y pretende **predecir** la **probabilidad** de que un cliente se dé de **baja** o no, de cara a realizar **acciones preventivas de retención** al cliente en caso de probabilidad alta de baja.""", unsafe_allow_html=True)
st.markdown("""Para este modelo se han recopilado una serie de variables demográficas del cliente, así como otras relacionadas con la salud financiera del mismo.""", unsafe_allow_html=True)



