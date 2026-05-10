import streamlit as st
from datetime import datetime

# 1. Configuración de la plataforma
st.set_page_config(page_title="El Templo de Anubis", layout="wide")

# Estilo CSS Avanzado para fondo negro y letras doradas
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #d4af37; }
    h1, h2, h3, p, span, label { color: #d4af37 !important; font-family: 'Cinzel', serif; }
    [data-testid="stSidebar"] { background-color: #0a0a0a; border-right: 1px solid #d4af37; }
    .stTextInput>div>div>input, .stDateInput>div>div>input { background-color: #1a1a1a; color: #d4af37 !important; border: 1px solid #d4af37; }
    .stTabs [data-baseweb="tab-list"] { background-color: #050505; gap: 10px; }
    .stTabs [data-baseweb="tab"] { background-color: #1a1a1a; border: 1px solid #d4af37; border-radius: 5px 5px 0 0; color: #d4af37 !important; }
    .stTabs [aria-selected="true"] { background-color: #d4af37 !important; color: #050505 !important; }
    .stButton>button { background-color: #d4af37; color: #050505; border-radius: 5px; font-weight: bold; border: none; }
    .stButton>button:hover { background-color: #f5f5dc; box-shadow: 0 0 15px #d4af37; }
    iframe { border: 2px solid #d4af37; border-radius: 10px; }
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
    st.header("🔐 Área del Instructor")
    password = st.text_input("Clave Maestra:", type="password")
    
    es_instructor = (password == "anubis2026")

# --- LÓGICA DE VISUALIZACIÓN ---
if nombre_user or es_instructor:
    
    if es_instructor:
        dias_pasados = 100 
        st.info(f"Maestro Vrolok operando como: {nombre_user if nombre_user else 'Administrador'}")
        
        # --- PRESENTACIÓN AUTOMÁTICA (EMBED) ---
        st.subheader("📺 Pantalla de Presentación Maestra")
        # El ID de tu presentación de Google Slides
        slide_id = "1dO3YrrZYeU4uNyeJEsMKxhjCSlC_P0GDpVcJr9w5m2Q"
        embed_url = f"https://docs.google.com/presentation/d/{slide_id}/embed?start=false&loop=false&delayms=3000"
        
        # Ajustamos el ancho al 100% para que ocupe toda la pantalla disponible
        st.components.v1.iframe(embed_url, height=600, scrolling=True)
        st.write("---")
    else:
        hoy = datetime.now().date()
        dias_pasados = (hoy - fecha_inscripcion).days
        st.success(f"Bienvenido/a a El Templo de Anubis, {nombre_user}")

    tab1, tab2, tab3 = st.tabs(["Tarot de Marsella", "Runas Vikingas", "Wicca & Magia"])

    with tab1:
        st.subheader("Módulo: Tarot de Marsella")
        materiales = [
            {"titulo": "Clase 1", "url": "https://drive.google.com/file/d/159pd32ErBY5ivTRUhZoY-sHxstGc9puB/view", "dia": 0},
            {"titulo": "Clase 2", "url": "https://drive.google.com/file/d/1FOcbDLocK2i6xf_FH-APCF2GvM7iZwY5/view", "dia": 7},
            {"titulo": "Clase de tiradas", "url": "https://drive.google.com/file/d/19nYTrsNW76GI4pLvGddXZlZ4XfMdgFeW/view", "dia": 14},
            {"titulo": "Clase de arcanos menores", "url": "https://drive.google.com/file/d/1jYaMsGXcIbMYw18GNNqUTbOyidi5UjWa/view", "dia": 21}
        ]

        for c in materiales:
            if es_instructor or dias_pasados >= c["dia"]:
                st.write(f"### ✅ {c['titulo']}")
                st.link_button(f"Descargar material", c["url"])
                st.write("---")
            else:
                st.warning(f"🔒 {c['titulo']} (Disponible en {c['dia'] - dias_pasados} días)")

    with tab2: st.info("Próximamente: Materiales de Runas Vikingas.")
    with tab3: st.info("Próximamente: Materiales de Wicca y Magia.")

else:
    st.info("👈 Por favor, ingresa tu nombre en el registro lateral para acceder.")
