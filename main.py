import streamlit as st
from datetime import datetime

# Configuración estética
st.set_page_config(page_title="Academia Mística - Anubis", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #1a1a1a; color: #d4af37; }
    .stButton>button { background-color: #4a148c; color: white; border-radius: 10px; width: 100%; }
    .clase-box { border: 1px solid #d4af37; padding: 15px; border-radius: 10px; margin-bottom: 10px; background-color: #262626; }
    </style>
    """, unsafe_allow_stdio=True)

st.title("🌙 Academia de Tarot, Runas y Wicca")
st.write("---")

# --- REGISTRO DE ALUMNO ---
with st.sidebar:
    st.header("📝 Registro de Alumno")
    nombre = st.text_input("Nombre Completo:")
    fecha_inscripcion = st.date_input("¿Qué día te inscribiste?", datetime.now())
    st.info("Nota: Los materiales se liberarán automáticamente cada 7 días a partir de esta fecha.")

if nombre:
    # Cálculo de días transcurridos
    hoy = datetime.now().date()
    dias_pasados = (hoy - fecha_inscripcion).days

    st.success(f"Bienvenido/a a tu portal, {nombre}")
    
    tab1, tab2, tab3 = st.tabs(["Tarot de Marsella", "Runas Vikingas", "Wicca & Magia"])

    with tab1:
        st.subheader("Módulo 1: Tarot (Liberación Progresiva)")
        
        # Lista de materiales
        materiales = [
            {"n": "Material para la clase 1", "u": "https://drive.google.com/file/d/159pd32ErBY5ivTRUhZoY-sHxstGc9puB/view", "d": 0},
            {"n": "Material para la clase 2", "u": "https://drive.google.com/file/d/1FOcbDLocK2i6xf_FH-APCF2GvM7iZwY5/view", "d": 7},
            {"n": "Material para la clase de tiradas", "u": "https://drive.google.com/file/d/19nYTrsNW76GI4pLvGddXZlZ4XfMdgFeW/view", "d": 14},
            {"n": "Material para la clase de arcanos menores", "u": "https://drive.google.com/file/d/1jYaMsGXcIbMYw18GNNqUTbOyidi5UjWa/view", "d": 21}
        ]

        for m in materiales:
            if dias_pasados >= m["d"]:
                with st.container():
                    st.markdown(f'<div class="clase-box"><h4>✅ {m["n"]}</h4></div>', unsafe_allow_stdio=True)
                    st.link_button(f"Descargar {m['n']}", m["u"])
            else:
                st.info(f"🔒 {m['n']} (Disponible en {m['d'] - dias_pasados} días)")

    with tab2:
        st.info("Próximamente materiales de Runas Vikingas.")

    with tab3:
        st.info("Próximamente materiales de Wicca y Magia Draconiana.")
else:
    st.warning("👈 Por favor, regístrate en el panel de la izquierda para ver tus materiales.")

# --- PANEL ADMIN (PARA TI) ---
with st.expander("🔑 Acceso Administrador"):
    st.link_button("📂 Presentación Maestra", "https://docs.google.com/presentation/d/1dO3YrrZYeU4uNyeJEsMKxhjCSlC_P0GDpVcJr9w5m2Q/edit")
