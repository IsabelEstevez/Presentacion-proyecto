import streamlit as st

# Configurar página
st.set_page_config(
    page_title="Bienvenidos",
    page_icon="👋",
)

# Título principal centrado
# st.markdown("<h3 style='text-align: center;'>MODELO SELECIONADO: </h3>", unsafe_allow_html=True)
# st.markdown("<h1 style='text-align: center; color:#6fa8dc;'>Boosting Algorithms </h1>", unsafe_allow_html=True)
# st.markdown("<h2 style='text-align: center;'>(XGBOOST) </h2>", unsafe_allow_html=True)
st.markdown("""
<svg width="600" height="50">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:rgb(255,0,0);stop-opacity:1" />
      <stop offset="50%" style="stop-color:rgb(0,0,0);stop-opacity:1" />
    <stop offset="100%" style="stop-color:rgb(255,0,0);stop-opacity:1" />
    </linearGradient>
  </defs>
  <text x="55%" y="40" fill="url(#grad1)" font-size="40" text-anchor="middle" font-weight="bold">MODELO SELECCIONADO</text>
</svg>
""", unsafe_allow_html=True)

st.markdown("""
<div style="display: flex; justify-content: center;">
  <svg width="600" height="50">
    <defs>
      <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" style="stop-color:rgb(0,0,0);stop-opacity:1" />
        <stop offset="50%" style="stop-color:rgb(255,0,0);stop-opacity:1" />
        <stop offset="100%" style="stop-color:rgb(0,0,0);stop-opacity:1" />
      </linearGradient>
    </defs>
    <text x="50%" y="40" fill="url(#grad1)" font-size="30" text-anchor="middle" font-weight="bold">Boosting Algorithms (XGBOOST)</text>
  </svg>
</div>
""", unsafe_allow_html=True)


st.markdown("<br>", unsafe_allow_html=True)


# Mostrar imagen debajo del título
imagen_url = "images/explicacion modelo.jpg"
st.image(imagen_url, caption="PROYECTO FINAL", width=1000, use_column_width=True)

