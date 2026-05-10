import streamlit as st
from datetime import datetime

# 1. Configuración de la plataforma
st.set_page_config(page_title="El Templo de Anubis", layout="wide")

# Estilo CSS para fondo negro y letras doradas (Se mantiene para la mística del Templo)
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #d4af37; }
    h1, h2, h3, p, span, label { color: #d4af37 !important; font-family: 'Cinzel', serif; }
    [data-testid="stSidebar"] { background-color: #0a0a0a; border-right: 1px solid #d4af37; }
    .stTextInput>div>div>input, .stDateInput>div>div>input { 
        background-color: #1a1a1a; 
        color: #d4af37 !important; 
        border: 1px solid #d4af37; 
    }
    .stTabs [data-baseweb="tab-list"] { background-color: #050505; gap: 10px; }
    .stTabs [data-baseweb="tab"] { 
        background-color: #1a1a1a; 
        border: 1px solid #d4af37; 
        border-radius: 5px 5px 0 0; 
        color: #d4af37 !important; 
    }
    .stTabs [aria-selected="true"] { background-color: #d4af37 !important; color: #050505 !important; }
    .stButton>button { 
        background-color: #d4af37; 
        color: #050505; 
        border-radius: 5px; 
        font-weight: bold; 
        border: none; 
    }
    .stButton>button:hover { background-color: #f5f5dc; box-shadow: 0 0 15px #d4af37; }
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
    
    # Identidad del Maestro Vrolok
    es_instructor = (password == "anubis2026")
    
    if es_instructor:
        st.success("Acceso Maestro Activo")
        # El botón vuelve a estar aquí, en la izquierda, como lo prefieres
        st.link_button("📂 Abrir Presentación Maestra", "https://docs.google.com/presentation/d/1dO3YrrZYeU4uNyeJEsMKxhjCSlC_P0GDpVcJr9w5m2Q/edit")

# --- LÓGICA DE VISUALIZACIÓN ---
if nombre_user or es_instructor:
    
    if es_instructor:
        dias_pasados = 100 
        saludo = "Bienvenido Maestro Vrolok" if not nombre_user else f"Maestro Vrolok operando como: {nombre_user}"
        st.info(saludo)
    else:
        hoy = datetime.now().date()
        dias_pasados = (hoy - fecha_inscripcion).days
        st.success(f"Bienvenido/a a El Templo de Anubis, {nombre_user}")

    tab1, tab2, tab3 = st.tabs(["Tarot de Marsella", "Runas Vikingas", "Wicca & Magia"])

    with tab1:
        st.subheader("Módulo: Tarot de Marsella")
        
        # Orden solicitado: Clase 1 (Introducción), Clase 2 (Mazo)
        materiales = [
            {"titulo": "Clase 1", "url": "https://drive.google.com/file/d/159pd32ErBY5ivTRUhZoY-sHxstGc9puB/view", "dia": 0},
            {"titulo": "Clase 2", "url": "https://drive.google.com/file/d/1FOcbDLocK2i6xf_FH-APCF2GvM7iZwY5/view", "dia": 7},
            {"titulo": "Clase de tiradas", "url": "
