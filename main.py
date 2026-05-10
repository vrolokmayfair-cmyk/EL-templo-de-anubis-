import streamlit as st
from datetime import datetime

# 1. Configuración básica
st.set_page_config(page_title="Academia Mística - Anubis", layout="wide")

# 2. Título y Estilo Simple
st.title("🌙 Academia de Tarot, Runas y Wicca")
st.markdown("---")

# 3. Registro Manual en la barra lateral
with st.sidebar:
    st.header("📝 Registro de Alumno")
    nombre_alumno = st.text_input("Escribe tu nombre:")
    fecha_inscripcion = st.date_input("Fecha de inicio del curso:", datetime.now())
    st.info("Tus clases se liberan automáticamente cada 7 días desde esta fecha.")

# 4. Lógica de acceso
if nombre_alumno:
    # Cálculo de tiempo
    hoy = datetime.now().date()
    dias_pasados = (hoy - fecha_inscripcion).days

    st.success(f"Bienvenido/a al portal de alumnos, {nombre_alumno}")
    
    # Pestañas de cursos
    t1, t2, t3 = st.tabs(["Tarot de Marsella", "Runas Vikingas", "Wicca & Magia"])

    with t1:
        st.subheader("Módulo: Tarot de Marsella")
        
        clases = [
            {"titulo": "Clase 1: Introducción y Ética", "url": "https://drive.google.com/file/d/159pd32ErBY5ivTRUhZoY-sHxstGc9puB/view", "dia": 0},
            {"titulo": "Clase 2: Mazo para colorear", "url": "https://drive.google.com/file/d/1FOcbDLocK2i6xf_FH-APCF2GvM7iZwY5/view", "dia": 7},
            {"titulo": "Clase: Tiradas y Leyes Camoin", "url": "https://drive.google.com/file/d/19nYTrsNW76GI4pLvGddXZlZ4XfMdgFeW/view", "dia": 14},
            {"titulo": "Clase: Arcanos Menores", "url": "https://drive.google.com/file/d/1jYaMsGXcIbMYw18GNNqUTbOyidi5UjWa/view", "dia": 21}
        ]

        for c in clases:
            if dias_pasados >= c["dia"]:
                st.write(f"### ✅ {c['titulo']}")
                st.link_button(f"Descargar material", c["url"])
                st.write("---")
            else:
                st.warning(f"🔒 {c['titulo']} (Disponible en {c['dia'] - dias_pasados} días)")

    with t2:
        st.info("Próximamente: Materiales de Runas Vikingas.")

    with t3:
        st.info("Próximamente: Materiales de Wicca y Magia.")

else:
    st.info("👈 Ingresa tu nombre en el panel lateral para ver tus materiales.")

# 5. Panel Administrativo
with st.sidebar:
    st.write("---")
    with st.expander("🔑 Acceso Instructor"):
        st.link_button("📂 Presentación Maestra", "https://docs.google.com/presentation/d/1dO3YrrZYeU4uNyeJEsMKxhjCSlC_P0GDpVcJr9w5m2Q/edit")
