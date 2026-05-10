import streamlit as st
from datetime import datetime

# 1. Configuración de la plataforma
st.set_page_config(page_title="El Templo de Anubis", layout="wide")

# Estilo personalizado para una atmósfera mística
st.markdown("""
    <style>
    .main { background-color: #1a1a1a; color: #d4af37; }
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] { height: 50px; background-color: #262626; border-radius: 5px; color: #d4af37; }
    .stButton>button { background-color: #4a148c; color: white; border-radius: 10px; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌙 El Templo de Anubis")
st.write("---")

# --- BARRA LATERAL ---
with st.sidebar:
    st.header("📝 Registro de Alumno")
    nombre_user = st.text_input("Nombre Completo:")
    fecha_inscripcion = st.date_input("Fecha de inicio:", datetime.now())
    
    st.write("---")
    
    # --- APARTADO PROTEGIDO PARA INSTRUCTOR ---
    st.header("🔐 Área del Instructor")
    password = st.text_input("Clave Maestra:", type="password")
    
    # Verificación de identidad
    es_instructor = (password == "anubis2026")
    
    if es_instructor:
        st.success("Acceso Maestro Activo")
        st.link_button("📂 Presentación Maestra (Tarot)", "https://docs.google.com/presentation/d/1dO3YrrZYeU4uNyeJEsMKxhjCSlC_P0GDpVcJr9w5m2Q/edit")

# --- LÓGICA DE VISUALIZACIÓN ---
if nombre_user or es_instructor:
    
    # Acceso total si es instructor
    if es_instructor:
        dias_pasados = 100 
        saludo = f"Bienvenido Maestro Juan Carlos Sumano" if not nombre_user else f"Operando como: {nombre_user}"
        st.info(saludo)
    else:
        hoy = datetime.now().date()
        dias_pasados = (hoy - fecha_inscripcion).days
        st.success(f"Bienvenido/a a El Templo de Anubis, {nombre_user}")

    # Pestañas de Cursos
    tab1, tab2, tab3 = st.tabs(["Tarot de Marsella", "Runas Vikingas", "Wicca & Magia"])

    with tab1:
        st.subheader("Módulo: Tarot de Marsella")
        
        # Lista de materiales con el orden corregido
        materiales = [
            {"titulo": "Clase 1: Mazo para imprimir y colorear", "url": "https://drive.google.com/file/d/1FOcbDLocK2i6xf_FH-APCF2GvM7iZwY5/view", "dia": 0},
            {"titulo": "Clase 2: Introducción, Ética y Anatomía Sagrada", "url": "https://drive.google.com/file/d/159pd32ErBY5ivTRUhZoY-sHxstGc9puB/view", "dia": 7},
            {"titulo": "Clase de Tiradas: Leyes Camoin", "url": "https://drive.google.com/file/d/19nYTrsNW76GI4pLvGddXZlZ4XfMdgFeW/view", "dia": 14},
            {"titulo": "Clase de Arcanos Menores: Figuras de la Corte", "url": "https://drive.google.com/file/d/1jYaMsGXcIbMYw18GNNqUTbOyidi5UjWa/view", "dia": 21}
        ]

        for c in materiales:
            if es_instructor or dias_pasados >= c["dia"]:
                st.write(f"### ✅ {c['titulo']}")
                st.link_button(f"Descargar material", c["url"])
                st.write("---")
            else:
                st.warning(f"🔒 {c['titulo']} (Disponible en {c['dia'] - dias_pasados} días)")

    with tab2:
        st.info("Próximamente: Materiales de Runas Vikingas.")

    with tab3:
        st.info("Próximamente: Materiales de Wicca y Magia.")

else:
    st.info("👈 Por favor, ingresa tu nombre en el registro lateral para acceder.")
