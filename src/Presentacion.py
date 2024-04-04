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
      <stop offset="0%" style="stop-color:rgb(255,0,0);stop-opacity:1" />
      <stop offset="50%" style="stop-color:rgb(0,0,0);stop-opacity:1" />
    <stop offset="100%" style="stop-color:rgb(255,0,0);stop-opacity:1" />
    </linearGradient>
  </defs>
  <text x="55%" y="40" fill="url(#grad1)" font-size="40" text-anchor="middle" font-weight="bold">BANK CHURN PREDICTION</text>
</svg>
""", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# Tamaño de texto y alineación centrada
st.markdown("<h3 style='text-align: center;'>Elisa Castro</h3>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Isabel Estévez</h3>", unsafe_allow_html=True)

# Mostrar imagen debajo del título
imagen_url = "https://img.freepik.com/premium-vector/bank-facade-with-tiny-people-flat-vector-illustration-office-workers-economists-making-deals-clients-exchanging-money-taking-credit-buying-house-government-finance-system-business-concept_74855-23956.jpg?w=996"

st.markdown(f"""
    <div style="display: flex; justify-content: center;">
        <img src="{imagen_url}" style="max-width: 60%;" alt="PROYECTO FINAL">
    </div>
""", unsafe_allow_html=True)

