import streamlit as st
from datetime import datetime

# 1. Configuración de la plataforma
st.set_page_config(page_title="El Templo de Anubis", layout="wide")

# Estilo CSS para fondo negro y letras doradas
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
    /* Estilo para la pestaña seleccionada: Texto negro sobre amarillo */
    .stTabs [aria-selected="true"] { 
        background-color: #d4af37 !important; 
        color: #050505 !important; 
    }
    .stButton>button { 
        background-color: #d4af37; 
        color: #050505; 
        border-radius: 5px; 
        font-weight: bold; 
        border: none; 
    }
    .stButton>button:hover { background-color: #f5f5dc; box-shadow: 0 0 15px #d4af37; }
    
    /* Estilo para la imagen de portada */
    .cover-img {
        border: 2px solid #d4af37;
        border-radius: 15px;
        margin-bottom: 20px;
    }
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

    # Pestañas con "Inicio" como la primera opción
    tab_home, tab1, tab2, tab3 = st.tabs(["🏛 Inicio", "Tarot de Marsella", "Runas Vikingas", "Wicca & Magia"])

    with tab_home:
        # --- IMAGEN DE PORTADA ---
        # Convertimos el enlace de Drive a un enlace directo para Streamlit
        img_url = "https://drive.google.com/uc?id=1w5HrhaJ2zTry18aSflGsDxTv-ianMTEC"
        st.image(img_url, use_container_width=True, caption="El Templo de Anubis - Sabiduría Ancestral")
        
        st.subheader("Bienvenido al Santuario del Conocimiento")
        st.write("Selecciona uno de los módulos superiores para comenzar tu formación.")
        st.write("Cada paso que des en este templo te acercará más a la maestría de las artes sagradas.")

    with tab1:
        st.subheader("Módulo: Tarot de Marsella")
        
        # Orden: Clase 1 (Introducción), Clase 2 (Mazo)
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

    with tab2:
        st.info("Próximamente: Materiales de Runas Vikingas.")

    with tab3:
        st.info("Próximamente: Materiales de Wicca y Magia.")

else:
    st.info("👈 Por favor, ingresa tu nombre en el registro lateral para acceder.")
