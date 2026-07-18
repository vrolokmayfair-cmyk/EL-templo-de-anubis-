import streamlit as st
from datetime import datetime

# 1. Configuración de la plataforma
st.set_page_config(page_title="El Templo de Anubis", page_icon="🌙", layout="wide")

# Estilo CSS Avanzado (Fondo negro, letras doradas, texto negro en pestañas activas)
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #d4af37; }
    h1, h2, h3, h4, p, span, label { color: #d4af37 !important; font-family: 'Cinzel', serif; }
    [data-testid="stSidebar"] { background-color: #0a0a0a; border-right: 1px solid #d4af37; }
    
    .stTextInput>div>div>input, .stDateInput>div>div>input, .stTextArea>div>div>textarea { 
        background-color: #1a1a1a; 
        color: #d4af37 !important; 
        border: 1px solid #d4af37; 
    }

    /* Pestañas */
    .stTabs [data-baseweb="tab-list"] { background-color: #050505; gap: 10px; }
    .stTabs [data-baseweb="tab"] { 
        background-color: #1a1a1a; 
        border: 1px solid #d4af37; 
        border-radius: 5px 5px 0 0; 
        color: #d4af37 !important; 
    }
    .stTabs [aria-selected="true"] p { color: #000000 !important; }
    .stTabs [aria-selected="true"] { background-color: #d4af37 !important; }
    
    /* Botones y bloques de comentarios */
    .stButton>button { background-color: #d4af37; color: #050505; border-radius: 5px; font-weight: bold; border: none; }
    .wiki-post { background-color: #111111; border: 1px solid #d4af37; padding: 20px; border-radius: 8px; margin-bottom: 20px; }
    .wiki-comment { background-color: #1a1a1a; border-left: 3px solid #d4af37; padding: 10px; margin-left: 20px; margin-top: 5px; border-radius: 4px; }
    </style>
    """, unsafe_allow_html=True)

# --- PORTADA PRINCIPAL ---
try:
    st.image("anubis-the-ancient-egyptian-jackal-headed-god-seat.jpeg", use_container_width=True)
except FileNotFoundError:
    st.error("Cargando imagen desde el repositorio del Templo...")

st.title("🌙 El Templo de Anubis")
st.write("---")

# --- INICIALIZACIÓN DE LA WIKI (Memoria de la App) ---
if "wiki_posts" not in st.session_state:
    st.session_state.wiki_posts = [
        {
            "id": 1,
            "autor": "Maestro Vrolok",
            "titulo": "El Secreto del Loco en el Tarot",
            "contenido": "El Arcano Cero representa el salto cuántico. No tiene número porque es el origen de todas las posibilidades dentro del sendero.",
            "comentarios": [{"usuario": "Alumno Iniciado", "texto": "Increíble explicación, Maestro. Esto cambia mi perspectiva de la tirada."}]
        }
    ]

# --- BARRA LATERAL ---
with st.sidebar:
    st.header("📝 Registro de Alumno")
    nombre_user = st.text_input("Nombre Completo:")
    fecha_inscripcion = st.date_input("Fecha de inicio:", datetime.now())
    st.write("---")
    st.header("🔐 Área del Instructor")
    password = st.text_input("Clave Maestra:", type="password")
    
    es_instructor = (password == "anubis2026")
    
    if es_instructor:
        st.success("Acceso Maestro Activo")
        st.link_button("📂 Abrir Presentación Maestra", "https://docs.google.com/presentation/d/1dO3YrrZYeU4uNyeJEsMKxhjCSlC_P0GDpVcJr9w5m2Q/edit")

# --- LÓGICA DE CONTENIDO ---
if nombre_user or es_instructor:
    
    usuario_actual = "Maestro Vrolok" if es_instructor else (nombre_user if nombre_user else "Buscador Anónimo")
    
    if es_instructor:
        dias_pasados = 100 
        st.info("Bienvenido Maestro Vrolok")
    else:
        hoy = datetime.now().date()
        dias_pasados = (hoy - fecha_inscripcion).days
        st.success(f"Bienvenido/a a El Templo de Anubis, {nombre_user}")

    # Nueva pestaña añadida: "Wiki Comunitaria"
    tab_home, tab1, tab2, tab3, tab_wiki = st.tabs(["🏛 Inicio", "Tarot de Marsella", "Runas Vikingas", "Wicca & Magia", "📜 Wiki Comunitaria"])

    with tab_home:
        st.subheader("Santuario del Conocimiento")
        st.write("Selecciona una pestaña superior para acceder a tus lecciones o compartir en la Wiki.")

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

    # --- DESARROLLO DEL MÓDULO WIKI ---
    with tab_wiki:
        st.subheader("📜 Bitácora de Conocimiento Esotérico")
        st.write("Un espacio compartido para que los iniciados de El Templo de Anubis publiquen sus reflexiones, dudas y hallazgos.")
        
        # Formulario para nueva publicación
        with st.expander("✍️ Crear Nueva Publicación en la Wiki"):
            titulo_post = st.text_input("Título de la publicación:")
            contenido_post = st.text_area("¿Qué conocimiento deseas plasmar?")
            if st.button("Publicar en el Templo"):
                if titulo_post and contenido_post:
                    nuevo_id = len(st.session_state.wiki_posts) + 1
                    st.session_state.wiki_posts.append({
                        "id": nuevo_id,
                        "autor": usuario_actual,
                        "titulo": titulo_post,
                        "contenido": contenido_post,
                        "comentarios": []
                    })
                    st.success("El conocimiento ha sido grabado en los muros del templo.")
                    st.rerun()
                else:
                    st.error("Por favor completa el título y el contenido.")

        st.write("### 🏛 Entradas Recientes")
        
        # Despliegue de publicaciones (desde la más nueva)
        for post in reversed(st.session_state.wiki_posts):
            st.markdown(f"""
            <div class="wiki-post">
                <h4>✨ {post['titulo']}</h4>
                <p style='font-size: 14px; opacity: 0.7;'>Por: <b>{post['autor']}</b></p>
                <p style='font-size: 16px; color: #e0e0e0;'>{post['contenido']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Mostrar comentarios existentes
            if post["comentarios"]:
                st.write("💬 *Comentarios de los iniciados:*")
                for c in post["comentarios"]:
                    st.markdown(f"""
                    <div class="wiki-comment">
                        <p style='font-size: 14px; margin-bottom: 2px;'><b>{c['usuario']}:</b> {c['texto']}</p>
                    </div>
                    """, unsafe_allow_html=True)
            
            # Formulario para añadir comentario (con llave única basada en ID)
            nuevo_comentario = st.text_input(f"Añadir comentario a '{post['titulo']}':", key=f"input_{post['id']}")
            if st.button("Comentar", key=f"btn_{post['id']}"):
                if nuevo_comentario:
                    post["comentarios"].append({
                        "usuario": usuario_actual,
                        "texto": nuevo_comentario
                    })
                    st.success("Comentario añadido.")
                    st.rerun()
            st.write("---")

else:
    st.warning("👈 Por favor, identifícate en el panel de la izquierda para entrar al Templo.")
