import streamlit as st


# Mostrar imagen debajo del título
imagen_url = "https://prezigram-assets.prezicdn.net/6ff4476b0f29d13bac329acfa2ac133a88fc3313feb5ae80f297f0f2e9d9bd1a43dd9a716084545ad8d27debbe12629199f05165a7117fa226df54998c4c4d1f"

# Mostrar imagen centrada y más grande
st.image(imagen_url, caption="PROYECTO FINAL", width=1200, use_column_width="always")

# Espaciado entre los nombres
st.markdown("<br>", unsafe_allow_html=True)