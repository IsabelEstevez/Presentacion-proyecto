import streamlit as st

# Establecer el estilo CSS para la imagen difuminada con texto superpuesto
estilo_css = """
<style>
.container {
    position: relative;
    width: 100%;
    height: 600px; /* Altura deseada para la imagen */
    overflow: hidden;
    border-radius: 20px; /* Borde redondeado */
    border: 10px solid transparent; /* Borde transparente */
    background: linear-gradient(to bottom right, #D32F2F, #212121
    
    ); /* Degradado de fondo */

}

.blur-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
    filter: blur(6px); /* Ajustar el valor de desenfoque según sea necesario */
    
}

.texto-superpuesto {
    position: absolute;
    top: 10%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
    color: white; /* Color del texto */
    font-size: 40px;
    font-weight: bold;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); /* Sombra suave para mejorar visibilidad */
}

.lista-mejoras {
    position: absolute;
    top: 60%;
    left: 50%;
    right: -30%;
    transform: translate(-50%, -40%);
    text-align: left; /* Alineación del texto de la lista a la izquierda */
    color: black; /* Color de la lista */
    font-size: 30px; /* Tamaño de fuente más grande para la lista */
    font-weight: bold; /* Texto en negrita */
    line-height: 1.5; /* Espaciado entre líneas de la lista */
}

.lista-mejoras li {
    margin-bottom: 10px; /* Espacio entre elementos de la lista */
}
</style>
"""

# Mostrar el estilo CSS en el encabezado de la página
st.markdown(estilo_css, unsafe_allow_html=True)

# Mostrar la imagen difuminada con texto superpuesto y lista de mejoras
imagen_url = "https://img.freepik.com/foto-gratis/vista-superior-conjunto-flechas-apuntando-arriba_23-2148490613.jpg?w=900"  # URL de ejemplo, reemplazar con tu URL de imagen
texto_superpuesto = """
<div class="container">
    <img class="blur-image" src="{}">
    <div class="texto-superpuesto">
        <svg width="600" height="300">
            <defs>
                <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
                    <stop offset="0%" style="stop-color:rgb(255,0,0);stop-opacity:1" />
                    <stop offset="50%" style="stop-color:rgb(0,0,0);stop-opacity:1" />
                    <stop offset="100%" style="stop-color:rgb(255,0,0);stop-opacity:1" />
                </linearGradient>
            </defs>
            <text x="50%" y="160" fill="url(#grad1)" font-size="40" text-anchor="middle" font-weight="bold">POSIBLES MEJORAS</text>
            <text x="50%" y="210" fill="url(#grad1)" font-size="40" text-anchor="middle" font-weight="bold">Y</text>
            <text x="50%" y="260" fill="url(#grad1)" font-size="40" text-anchor="middle" font-weight="bold">APLICACIONES A FUTURO</text>
        </svg>
    </div>
    <div class="lista-mejoras">
        <ul>
            <li style="font-size: 24px;"><strong>Incremento del volumen de datos para la variable objetivo</strong></li>
            <li style="font-size: 24px;"><strong>Aplicación de recomendación de acciones de retención por cliente</strong></li>
            <li style="font-size: 24px;"><strong>Sistema de alertas por cliente previa a la baja</strong></li>
        </ul>
    </div>
</div>
""".format(imagen_url)

# Mostrar el texto superpuesto con formato HTML
st.markdown(texto_superpuesto, unsafe_allow_html=True)

