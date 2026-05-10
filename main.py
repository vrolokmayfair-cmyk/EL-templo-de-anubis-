import streamlit as st
from datetime import datetime

# 1. Configuración de la página
st.set_page_config(page_title="Academia Mística - Anubis", layout="wide")

# Estilo personalizado para que se vea profesional
st.markdown("""
    <style>
    .main { background-color: #1a1a1a; color: #d4af37; }
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] { height: 50px; white-space: pre-wrap; background-color: #262626; border-radius: 5px; color: #d4af37; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌙 Academia de Tarot, Runas y Wicca")
st.markdown("---")

# --- BARRA LATERAL ---
with st.sidebar:
    st.header("📝 Registro de Alumno")
    nombre_user = st.text_input("Nombre Completo:")
    fecha_inscripcion = st.date_input("Fecha de inicio:", datetime.now())
    
    st.write("---")
    
    # --- APARTADO PROTEGIDO PARA INSTRUCTOR ---
    st.header("🔐 Área del Instructor")
    password = st.text_input("Introduce la clave maestra:", type="password")
    
    # Definimos tu clave aquí (puedes cambiar 'anubis2026' por la que quieras)
    es_instructor = (password == "anubis2026")
    
    if es_instructor:
        st.success("Acceso de Instructor Activo")
        st.link_button("📂 Presentación Maestra (Tarot)", "https://docs.google.com/presentation/d/1dO3YrrZYeU4uNyeJEsMKxhjCSlC_P0GDpVcJr9w5m2Q/edit")

# --- LÓGICA DE VISUALIZACIÓN ---
if nombre_user or es_instructor:
    
    # Si eres instructor, el sistema te da "poder total" (días infinitos)
    if es_instructor:
        dias_pasados = 100 
        st.info(f"Modo Instructor: Viendo plataforma como el alumno '{nombre_user if nombre_user else 'Admin'}'")
    else:
        hoy = datetime.now().date()
        dias_pasados = (hoy - fecha_inscripcion).days
        st.success(f"Bienvenido/a, {nombre_user}")

    # Pestañas de cursos
    tab1, tab2, tab3 = st.tabs(["Tarot de Marsella", "Runas Vikingas", "Wicca & Magia"])

    with tab1:
        st.subheader("Módulo: Tarot de Marsella")
        
        materiales = [
            {"titulo": "Clase 1: Introducción y Ética", "url": "https://drive.google.com/file/d/159pd32ErBY5ivTRUhZoY-sHxstGc9puB/view", "dia": 0},
            {"titulo": "Clase 2: Mazo para colorear", "url": "https://drive.google.com/file/d/1FOcbDLocK2i6xf_FH-APCF2GvM7iZwY5/view", "dia": 7},
            {"titulo": "Clase: Tiradas y Leyes Camoin", "url": "https://drive.google.com/file/d/19nYTrsNW76GI4pLvGddXZlZ4XfMdgFeW/view", "dia": 14},
            {"titulo": "Clase: Arcanos Menores", "url": "https://drive.google.com/file/d/1jYaMsGXcIbMYw18GNNqUTbOyidi5UjWa/view", "dia": 21}
        ]

        for c in materiales:
            # Si eres instructor o ya pasaron los días, se abre
            if es_instructor or dias_pasados >= c["dia"]:
                st.write(f"### ✅ {c['titulo']}")
                st.link_button(f"Descargar {c['titulo']}", c["url"])
                st.write("---")
            else:
                st.warning(f"🔒 {c['titulo']} (Disponible en {c['dia'] - dias_pasados} días)")

    with tab2:
        st.info("Próximamente: Materiales de Runas Vikingas.")

    with tab3:
        st.info("Próximamente: Materiales de Wicca y Magia.")

else:
    st.info("👈 Ingresa tu nombre o la clave de instructor para acceder.")
