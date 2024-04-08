import streamlit as st

# Título
st.markdown("""
<svg width="600" height="50">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:rgb(255,0,0);stop-opacity:1" />
      <stop offset="50%" style="stop-color:rgb(0,0,0);stop-opacity:1" />
    <stop offset="100%" style="stop-color:rgb(255,0,0);stop-opacity:1" />
    </linearGradient>
  </defs>
  <text x="55%" y="40" fill="url(#grad1)" font-size="40" text-anchor="middle" font-weight="bold">PRESENTACIÓN DEL EQUIPO</text>
</svg>
""", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# Crear una fila en la que la imagen estará a la izquierda y el texto a la derecha
col1, col2 = st.columns([1, 2])

# Mostrar la imagen en la columna 1
with col1:
    imagen_url = "images/Elisa.jpg"
    st.image(imagen_url, width=150)

# Descripción de Elisa
with col2:
    st.markdown("""
    <h2 style='font-size: 20px;'></h2>
    <ul>
        <li>Gaditana (El Puerto de Santa María)</li>
        <li>Estudios: Ciencias del Mar en Cádiz </li>
        <li>Última profesión: Agente de ventas </li>
        <li>Motivos para entrar en 4Geeks: Desarrollo profesional</li>
    </ul>
    """, unsafe_allow_html=True)
# Crear una fila en la que la imagen estará a la izquierda y el texto a la derecha
col1, col2 = st.columns([1, 2])

# Mostrar la imagen en la columna 1
with col1:
    imagen_url = "images/Isa.jpeg"
    st.image(imagen_url, width=150)

# Descripción de Isa
with col2:
    st.markdown("""
    <h2 style='font-size: 20px;'></h2>
    <ul>
        <li>Madrileña</li>
        <li>Estudios: Estadística en Valladolid</li>
        <li>Última profesión: Dueña de un centro de estética</li>
        <li>Motivos para entrar en 4Geeks: Ampliar y asentar conocimientos</li>
    </ul>
    """, unsafe_allow_html=True)


