import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Academia Mística", layout="wide")

# Estilos visuales
st.markdown("""
    <style>
    .main { background-color: #1a1a1a; color: #d4af37; }
    .stButton>button { background-color: #4a148c; color: white; border-radius: 10px; width: 100%; }
    .clase-box { border: 1px solid #d4af37; padding: 15px; border-radius: 10px; margin-bottom: 10px; background-color: #262626; }
    </style>
    """, unsafe_allow_stdio=True)

st.title("🌙 Academia de Tarot, Runas y Wicca")

# Conexión con el enlace proporcionado
conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read()
df['Apellidos'] = df['Apellidos'].astype(str).str.strip().str.upper()

# Panel Administrativo
with st.expander("🔑 Acceso Administrativo"):
    st.link_button("📂 Abrir Presentación Maestra (Tarot)", "https://docs.google.com/presentation/d/1dO3YrrZYeU4uNyeJEsMKxhjCSlC_P0GDpVcJr9w5m2Q/edit")
    st.link_button("📊 Gestionar Alumnos (Sheets)", "https://docs.google.com/spreadsheets/d/1ii4x21yt0uqc3CQgwoiolxZLM5kzHJLzOSCCNtErzK8/edit")

# Acceso de Alumno
apellido_user = st.text_input("Ingresa tus Apellidos para entrar:").strip().upper()

if apellido_user:
    alumno = df[df['Apellidos'] == apellido_user]
    
    if not alumno.empty:
        nombre = alumno.iloc[0]['Nombre(s)']
        fecha_inicio = pd.to_datetime(alumno.iloc[0]['Fecha de Inicio'])
        dias_pasados = (datetime.now() - fecha_inicio).days
        
        st.success(f"Bienvenido/a, {nombre}")
        
        tab1, tab2, tab3 = st.tabs(["Tarot de Marsella", "Runas Vikingas", "Wicca & Magia"])

        with tab1:
            st.subheader("Módulo 1: Tarot (10 Clases)")
            materiales = [
                {"n": "Material para la clase 1", "u": "https://drive.google.com/file/d/159pd32ErBY5ivTRUhZoY-sHxstGc9puB/view", "d": 0},
                {"n": "Material para la clase 2", "u": "https://drive.google.com/file/d/1FOcbDLocK2i6xf_FH-APCF2GvM7iZwY5/view", "d": 7},
                {"n": "Material para la clase de tiradas", "u": "https://drive.google.com/file/d/19nYTrsNW76GI4pLvGddXZlZ4XfMdgFeW/view", "d": 14},
                {"n": "Material para la clase de arcanos menores", "u": "https://drive.google.com/file/d/1jYaMsGXcIbMYw18GNNqUTbOyidi5UjWa/view", "d": 21}
            ]

            for m in materiales:
                if dias_pasados >= m["d"]:
                    st.markdown(f'<div class="clase-box"><h4>{m["n"]}</h4></div>', unsafe_allow_stdio=True)
                    st.link_button(f"Descargar {m['n']}", m["u"])
                else:
                    st.info(f"🔒 {m['n']} (Disponible en {m['d'] - dias_pasados} días)")

    else:
        st.error("No se encontró el apellido en el registro.")