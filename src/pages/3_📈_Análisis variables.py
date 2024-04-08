import streamlit as st

st.set_page_config(
    page_title="Bienvenidos",
    page_icon="👋",
)

# Título principal centrado
st.markdown("""
<div style="display: flex; justify-content: center;">
  <svg width="800" height="50">
    <defs>
      <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" style="stop-color:rgb(255,0,0);stop-opacity:1" />
        <stop offset="50%" style="stop-color:rgb(0,0,0);stop-opacity:1" />
        <stop offset="100%" style="stop-color:rgb(255,0,0);stop-opacity:1" />
      </linearGradient>
    </defs>
    <text x="50%" y="40" fill="url(#grad1)" font-size="40" text-anchor="middle" font-weight="bold">ANÁLISIS DE VARIABLES SIGNIFICATIVAS</text>
  </svg>
</div>
""", unsafe_allow_html=True)

# Espaciado entre los nombres
st.markdown("<br>", unsafe_allow_html=True)

# Mostrar imagen debajo del título
imagen_url = "images/Variables-1.jpg"
st.image(imagen_url, caption="PROYECTO FINAL", width=1000, use_column_width=True)

# Espaciado entre los nombres
st.markdown("<br>", unsafe_allow_html=True)