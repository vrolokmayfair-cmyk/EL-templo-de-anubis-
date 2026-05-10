import streamlit as st
from datetime import datetime

# 1. Configuración de la plataforma (Título e Icono en la pestaña del navegador)
st.set_page_config(page_title="El Templo de Anubis", page_icon="🌙", layout="wide")

# Estilo CSS Avanzado para atmósfera mística (Fondo negro, letras doradas)
st.markdown("""
    <style>
    /* Fondo principal y textos generales */
    .stApp {
        background-color: #050505;
        color: #d4af37;
    }
    
    /* Títulos y tipografía mística */
    h1, h2, h3, p, span, label {
        color: #d4af37 !important;
        font-family: 'Cinzel', serif;
    }

    /* Barra lateral (Sidebar) */
    [data-testid="stSidebar"] {
        background-color: #0a0a0a;
        border-right: 1px solid #d4af37;
    }
    
    /* Inputs y campos de texto */
    .stTextInput>div>div>input, .stDateInput>div>div>input {
        background-color: #1a1a1a;
        color: #d4af37 !important;
        border: 1px solid #d4af37;
    }

    /* Pestañas (Tabs) */
    .stTabs [data-baseweb="tab-list"] {
        background-color: #050505;
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #1a1a1a;
        border: 1px solid #d4af37;
        border-radius: 5px 5px 0 0;
        color: #d4af37 !important;
        padding: 10px 20px;
    }
    
    /* CORRECCIÓN DE LEGIBILIDAD: Texto negro sobre fondo dorado al seleccionar */
    .stTabs [aria-selected="true"] p {
        color: #000000 !important;
    }
    .stTabs [aria-selected="true"] {
        background-color: #d4af37 !important;
    }

    /* Botones dorados */
    .stButton>button {
        background-color: #d4af37;
        color: #050505;
        border-radius: 5px;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #f5f5dc;
        box-shadow: 0 0 15px #d4af37;
    }
    
    /* Mensajes de alerta */
    .stAlert {
        background-color: #1a1a1a;
        border: 1px solid #d4af37;
        color: #d4af37;
    }
    </style>
    """, unsafe_allow_html=True)

# --- PORTADA PRINCIPAL (Siempre visible, incluso antes de loguearse) ---
# Intentamos cargar la imagen desde el repositorio de GitHub
try:
    st.image("anubis-the-ancient-egyptian-jackal-headed-god-seat.jpeg", use_container_width=True)
except FileNotFoundError:
    # Mensaje de respaldo si la imagen no se encuentra en GitHub
    st.error("La imagen de portada está siendo invocada desde el repositrio. Por favor, asegúrate de subir el archivo JPEG con el nombre exacto.")

st.title("🌙 El Templo de Anubis")
st.write("---")

# --- BARRA LATERAL (Registro y Acceso Instructor) ---
with st.sidebar:
    st.header("📝 Registro de Alumno")
    nombre_user = st.text_input("Nombre Completo:")
    fecha_inscripcion = st.date_input("Fecha de inicio del curso:", datetime.now())
    
    st.write("---")
    
    st.header("🔐 Área del Instructor")
    password = st.text_input("Clave Maestra:", type="password")
    
    # Verificación de identidad para el acceso de Maestro Vrolok
    es_instructor = (password == "anubis2026")
    
    if es_instructor:
        st.success("Acceso Maestro Activo")
        st.link_button("📂 Abrir Presentación Maestra (Tarot)", "https://docs.google.com/presentation/d/1dO3YrrZYeU4uNyeJEsMKxhjCSlC_P0GDpVcJr9w5m2Q/edit")

# --- LÓGICA DE VISUALIZACIÓN DE CONTENIDO ---
# Solo se muestra el contenido si hay un alumno registrado o si es el instructor
if nombre_user or es_instructor:
    
    # Saludo personalizado
    if es_instructor:
        dias_pasados = 100 # Desbloqueo total para el instructor
        st.info(f"Bienvenido Maestro Vrolok")
    else:
        # Cálculo de días desde la inscripción
        hoy = datetime.now().date()
        dias_pasados = (hoy - fecha_inscripcion).days
        st.success(f"Bienvenido/a a El Templo de Anubis, {nombre_user}")

    # Pestañas de Cursos (Mantenemos Inicio como pestaña por defecto)
    tab_home, tab1, tab2, tab3 = st.tabs(["🏛 Inicio", "Tarot de Marsella", "Runas Vikingas", "Wicca & Magia"])

    with tab_home:
        st.subheader("Bienvenido al Santuario del Conocimiento")
        st.write("Selecciona uno de los módulos superiores para comenzar tu formación.")
        st.write("Los misterios antiguos se revelarán ante ti a su debido tiempo.")

    with tab1:
        st.subheader("Módulo: Tarot de Marsella")
        
        # Lista de materiales y días de liberación
        materiales = [
            {"titulo": "Clase 1: Introducción, Ética y Anatomía Sagrada", "url": "https://drive.google.com/file/d/159pd32ErBY5ivTRUhZoY-sHxstGc9puB/view", "dia": 0},
            {"titulo": "Clase 2: Mazo para imprimir y colorear", "url": "https://drive.google.com/file/d/1FOcbDLocK2i6xf_FH-APCF2GvM7iZwY5/view", "dia": 7},
            {"titulo": "Clase de tiradas: Leyes Camoin", "url": "https://drive.google.com/file/d/19nYTrsNW76GI4pLvGddXZlZ4XfMdgFeW/view", "dia": 14},
            {"titulo": "Clase de arcanos menores: Figuras de la Corte", "url": "https://drive.google.com/file/d/1jYaMsGXcIbMYw18GNNqUTbOyidi5UjWa/view", "dia": 21}
        ]

        # Despliegue de materiales con lógica de tiempo
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
    # Mensaje cuando NO han iniciado sesión
    st.info("👈 Por favor, regístrate en la barra lateral para acceder a tus materiales de estudio.")
