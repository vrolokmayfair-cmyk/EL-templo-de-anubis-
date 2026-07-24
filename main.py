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
    
    /* Botones y bloques */
    .stButton>button { background-color: #d4af37; color: #050505; border-radius: 5px; font-weight: bold; border: none; }
    .wiki-post { background-color: #111111; border: 1px solid #d4af37; padding: 20px; border-radius: 8px; margin-bottom: 10px; }
    .wiki-comment { background-color: #1a1a1a; border-left: 3px solid #d4af37; padding: 10px; margin-left: 20px; margin-top: 5px; border-radius: 4px; }
    
    /* Tarjetas de evaluación */
    .eval-card { background-color: #111111; border: 1px solid #d4af37; padding: 15px; border-radius: 8px; margin-bottom: 15px; }
    .feedback-box { background-color: #1c1a0e; border-left: 4px solid #d4af37; padding: 10px 15px; border-radius: 4px; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- PORTADA PRINCIPAL ---
try:
    st.image("anubis-the-ancient-egyptian-jackal-headed-god-seat.jpeg", use_container_width=True)
except FileNotFoundError:
    st.error("Cargando imagen desde el repositorio del Templo...")

st.title("🌙 El Templo de Anubis")
st.write("---")

# --- INICIALIZACIÓN DE LA WIKI EN SESSION_STATE ---
if "wiki_posts" not in st.session_state:
    st.session_state.wiki_posts = [
        {
            "id": 1,
            "autor": "Maestro Vrolok",
            "titulo": "El Secreto del Loco en el Tarot",
            "contenido": "El Arcano Cero representa el salto cuántico. No tiene número porque es el origen de todas las posibilidades dentro del sendero.",
            "comentarios": [{"id_com": 1, "usuario": "Alumno Iniciado", "texto": "Increíble explicación, Maestro. Esto cambia mi perspectiva."}]
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
        st.info("Bienvenido Maestro Vrolok - Modo Administrador Activo")
    else:
        hoy = datetime.now().date()
        dias_pasados = (hoy - fecha_inscripcion).days
        st.success(f"Bienvenido/a a El Templo de Anubis, {nombre_user}")

    tab_home, tab1, tab2, tab3, tab_eval, tab_wiki = st.tabs([
        "Inicio", 
        "Tarot de Marsella", 
        "Runas Vikingas", 
        "Wicca & Magia", 
        "Evaluaciones CONOCER", 
        "Wiki Comunitaria"
    ])

    with tab_home:
        st.subheader("Santuario del Conocimiento")
        st.write("Selecciona una pestaña superior para acceder a tus lecciones, realizar tus evaluaciones o compartir en la Wiki.")

    # --- LECCIONES CON INSTRUCCIONES ACTUALIZADAS ---
    with tab1:
        st.subheader("Módulo: Tarot de Marsella")
        
        materiales = [
            {
                "titulo": "Material Clase 1", 
                "instruccion": "Descarga el material de los arcanos mayores del tarot marsella y colorealos de acuerdo a tu percepcion.",
                "url": "https://drive.google.com/file/d/159pd32ErBY5ivTRUhZoY-sHxstGc9puB/view", 
                "dia": 0
            },
            {
                "titulo": "Material Clase 2", 
                "instruccion": "Descarga el pdf de los arcanos mayores del tarot marsella, ya que se ocuparan en las siguientes clases.",
                "url": "https://drive.google.com/file/d/1FOcbDLocK2i6xf_FH-APCF2GvM7iZwY5/view", 
                "dia": 7
            },
            {
                "titulo": "Material Clase 3", 
                "instruccion": "Descarga el manual de tiradas para tener una amplia gama de opciones en tus lecturas adicionales a las que se te brindaron en clase.",
                "url": "https://drive.google.com/file/d/19nYTrsNW76GI4pLvGddXZlZ4XfMdgFeW/view", 
                "dia": 14
            },
            {
                "titulo": "Material Clase de Arcanos Menores", 
                "instruccion": "El siguiente pdf includes el tarot marsella completo para su utilizacion de forma personal.",
                "url": "https://drive.google.com/file/d/1jYaMsGXcIbMYw18GNNqUTbOyidi5UjWa/view", 
                "dia": 21
            }
        ]
        
        for c in materiales:
            if es_instructor or dias_pasados >= c["dia"]:
                st.write(f"### ✅ {c['titulo']}")
                st.write(f"ℹ️ *Instrucciones:* {c['instruccion']}")
                st.link_button(f"Descargar material", c["url"])
                st.write("---")
            else:
                st.warning(f"🔒 {c['titulo']} (Disponible en {c['dia'] - dias_pasados} días)")

    with tab2: st.info("Próximamente: Materiales de Runas Vikingas.")
    with tab3: st.info("Próximamente: Materiales de Wicca y Magia.")

    # --- MÓDULO DE EVALUACIONES (ALINEADO A ESTÁNDARES CONOCER) ---
    with tab_eval:
        st.subheader("📊 Sistema de Evaluación de Competencias (Estándares EC0217.1 / EC0301)")
        st.write("Instrumentos oficiales de medición de aprendizaje para la certificación del curso.")

        eval_sub1, eval_sub2, eval_sub3, eval_sub4 = st.tabs([
            "🩺 Evaluación Diagnóstica (0%)",
            "📋 Guía de Observación (40%)",
            "📝 Cuestionario Sumativo (60%)",
            "🔑 Clave de Respuestas & Retroalimentación"
        ])

        # 1. EVALUACIÓN DIAGNÓSTICA
        with eval_sub1:
            st.markdown("### 🩺 Evaluación Diagnóstica Inicial")
            st.caption("Esta evaluación no posee peso numérico (0%). Su objetivo es medir tus conocimientos previos al inicio del curso.")
            
            q_diag1 = st.radio(
                "1. En el Tarot de Marsella, ¿qué indica la orientación de la mirada de un personaje hacia la IZQUIERDA?",
                ["Proyección al futuro y acción activa", "Conexión con el pasado, origen e introspección", "Confrontación directa en el presente", "Neutralidad ante la consulta"],
                index=None, key="diag1"
            )
            q_diag2 = st.radio(
                "2. ¿A qué plano o elemento corresponden las ESPADAS en la estructura del Tarot?",
                ["Elemento Agua / Emociones", "Elemento Aire / Plano Mental y Pensamiento", "Elemento Fuego / Pasión e Impulso", "Elemento Tierra / Bienes Materiales"],
                index=None, key="diag2"
            )
            q_diag3 = st.radio(
                "3. El Arcano Cero (Le Mat / El Loco) representa:",
                ["El potencial puro, energía incipiente y libertad", "La estabilidad total en el trono", "El fin absoluto de todo proceso", "La culminación material del viaje"],
                index=None, key="diag3"
            )

            if st.button("Validar Diagnóstico"):
                aciertos_diag = 0
                if q_diag1 == "Conexión con el pasado, origen e introspección": aciertos_diag += 1
                if q_diag2 == "Elemento Aire / Plano Mental y Pensamiento": aciertos_diag += 1
                if q_diag3 == "El potencial puro, energía incipiente y libertad": aciertos_diag += 1
                
                st.success(f"Diagnóstico completado: {aciertos_diag}/3 respuestas acertadas.")
                st.info("💡 **Retroalimentación Diagnóstica:** La mirada a la izquierda marca la introspección, las espadas rigen la mente y el plano del pensamiento, y Le Mat es la chispa divina del potencial puro.")

        # 2. GUÍA DE OBSERVACIÓN (FORMATIVA - 40%)
        with eval_sub2:
            st.markdown("### 📋 Guía de Observación (Evaluación Formativa - 40%)")
            st.caption("Lista de cotejo para evaluar el desempeño práctico en la tirada demostrativa de 3 cartas.")
            
            c1 = st.checkbox("1. Análisis de Orientación: Identifica correctamente la dirección de miradas (pasado, presente o futuro) entre los 3 arcanos. (10 pts)")
            c2 = st.checkbox("2. Código Cromático: Reconoce el plano dominante según los colores de la tirada (Azul=Mente, Rojo=Cuerpo, Amarillo=Luz). (10 pts)")
            c3 = st.checkbox("3. Clasificación por Septenario: Ubica los arcanos en su septenario correspondiente (Material, Mental o Espiritual). (10 pts)")
            c4 = st.checkbox("4. Síntesis Hermenéutica: Estructura la conclusión integrando postura y gesto sin caer en superstición. (10 pts)")

            puntos_formative = sum([10 for c in [c1, c2, c3, c4] if c])
            st.metric("Puntaje Formativo (40% máx):", f"{puntos_formative} / 40 pts")

        # 3. CUESTIONARIO SUMATIVO (60%)
        with eval_sub3:
            st.markdown("### 📝 Cuestionario Teórico Final (Evaluación Sumativa - 60%)")
            st.caption("Acreditable con un mínimo del 80% global en la suma de las evaluaciones formativa y sumativa.")

            qs1 = st.radio(
                "1. Según la Anatomía Sagrada, ¿qué simbolizan las FIGURAS SEDENTES (ej. La Emperatriz, El Emperador)?",
                ["Transición súbita y viaje inestable", "Estabilidad, trono, poder establecido y reflexión", "Renuncia voluntaria a la acción", "Negación del conocimiento formal"],
                index=None, key="qs1"
            )
            qs2 = st.radio(
                "2. ¿Qué significado transmiten las MANOS OCULTAS (bajo mantos o espaldas)?",
                ["Voluntad activa y ejecución directa", "Escucha pasiva y recepción afectiva", "Secretos, reservas de energía o manipulación sutil", "Dominio absoluto del plano terrenal"],
                index=None, key="qs2"
            )
            qs3 = st.radio(
                "3. La MIRADA FRONTAL en un personaje del Tarot (ej. La Justicia) indica:",
                ["Presente absoluto, confrontación directa y transparencia", "Búsqueda del origen e introspección del pasado", "Impulso activo proyectado hacia el futuro", "Duda e indecisión entre dos opciones"],
                index=None, key="qs3"
            )
            qs4 = st.radio(
                "4. En el Código Cromático de Marsella, el color AMARILLO / ORO simboliza:",
                ["Trabajo humano y carne terrenal", "Luz divina, conciencia solar e inteligencia trascendente", "Pasión descontrolada e instintos", "Reposo, silencio e inconsciente"],
                index=None, key="qs4"
            )
            qs5 = st.radio(
                "5. El SEPTENARIO II (Arcanos VIII a XIV) corresponde al plano de evolución:",
                ["Plano Material y Concreción Terrenal", "Plano Mental, Equilibrio e Introspección Transmutadora", "Plano Espiritual y Cosmogonía", "Plano Subconsciente e Ilusiones"],
                index=None, key="qs5"
            )
            qs6 = st.radio(
                "6. Los Arcanos XV (El Diablo) a XXI (El Mundo) pertenecen al Septenario:",
                ["Primer Septenario (Plano Físico)", "Segundo Septenario (Plano Intelectual)", "Tercer Septenario (Plano Espiritual y Liberación)", "Arcanos de transición sin asignación"],
                index=None, key="qs6"
            )

            if st.button("Calcular Examen Sumativo"):
                respuestas_correctas = {
                    "qs1": "Estabilidad, trono, poder establecido y reflexión",
                    "qs2": "Secretos, reservas de energía o manipulación sutil",
                    "qs3": "Presente absoluto, confrontación directa y transparencia",
                    "qs4": "Luz divina, conciencia solar e inteligencia trascendente",
                    "qs5": "Plano Mental, Equilibrio e Introspección Transmutadora",
                    "qs6": "Tercer Septenario (Plano Espiritual y Liberación)"
                }
                
                user_ans = {"qs1": qs1, "qs2": qs2, "qs3": qs3, "qs4": qs4, "qs5": qs5, "qs6": qs6}
                correctas = sum(1 for k, v in user_ans.items() if v == respuestas_correctas[k])
                puntos_sumativa = (correctas / 6) * 60
                
                total_global = puntos_formative + puntos_sumativa
                
                st.metric("Resultado Examen Sumativo (60% máx):", f"{puntos_sumativa:.1f} / 60 pts ({correctas}/6 aciertos)")
                st.metric("CALIFICACIÓN GLOBAL FINAL:", f"{total_global:.1f} / 100 pts")
                
                if total_global >= 80:
                    st.balloons()
                    st.success("🎉 ¡Felicidades! Has alcanzado el criterio mínimo de acreditación (80% global) alineado a la norma CONOCER.")
                else:
                    st.warning("⚠️ No has alcanzado el puntaje mínimo de acreditación (80 pts). Revisa la retroalimentación y reintenta la prueba.")

        # 4. CLAVE DE RESPUESTAS Y RETROALIMENTACIÓN (EXCLUSIVO INSTRUCTOR O TRAS REVISIÓN)
        with eval_sub4:
            st.markdown("### 🔑 Clave Oficial de Respuestas & Retroalimentación Instruccional")
            st.caption("Guía para la retroalimentación del alumno conforme al Estándar EC0217.1.")
            
            if es_instructor or st.checkbox("Mostrar Clave de Respuestas y Justificación Técnica"):
                st.markdown("""
                <div class="feedback-box">
                    <h4>🩺 Evaluacion Diagnostica:</h4>
                    <p><b>P1 -> B:</b> La mirada a la izquierda indica origen, pasado e introspección.</p>
                    <p><b>P2 -> B:</b> Las Espadas rigen el Elemento Aire y el Plano Intelectual/Mental.</p>
                    <p><b>P3 -> A:</b> Le Mat (0) es la libertad de espíritu y el potencial infinito del iniciado.</p>
                </div>
                
                <div class="feedback-box">
                    <h4>📝 Cuestionario Sumativo:</h4>
                    <p><b>P1 -> B (Figuras Sedentes):</b> Representan la estabilidad, el trono, el poder afirmado y el pensamiento reflexivo.</p>
                    <p><b>P2 -> C (Manos Ocultas):</b> Señalan reservas energéticas, conocimiento hermético no manifestado o manipulación sutil.</p>
                    <p><b>P3 -> A (Mirada Frontal):</b> Indica confrontación directa en el presente absoluto, justicia e imparcialidad.</p>
                    <p><b>P4 -> B (Color Amarillo):</b> Simboliza la luz divina, la conciencia solar, la lucidez mental e inteligencia despierta.</p>
                    <p><b>P5 -> B (Septenario II):</b> Arcanos VIII al XIV representan el viaje por el Plano Mental, transmutación y equilibrio interior.</p>
                    <p><b>P6 -> C (Septenario III):</b> Arcanos XV al XXI integran el Plano Espiritual, la liberación de ataduras terrestres y el triunfo en El Mundo.</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.info("🔒 Ingresa la Clave Maestra en la barra lateral o marca la casilla superior para consultar la justificación pedagógica.")

    # --- WIKI CON GESTIÓN ADMINISTRATIVA (ELIMINAR/EDITAR) ---
    with tab_wiki:
        st.subheader("📜 Bitácora de Conocimiento Esotérico")
        
        # Formulario para nueva publicación
        with st.expander("✍️ Crear Nueva Publicación en la Wiki"):
            titulo_post = st.text_input("Título de la publicación:")
            contenido_post = st.text_area("¿Qué conocimiento deseas plasmar?")
            if st.button("Publicar en el Templo"):
                if titulo_post and contenido_post:
                    nuevo_id = max([p["id"] for p in st.session_state.wiki_posts]) + 1 if st.session_state.wiki_posts else 1
                    st.session_state.wiki_posts.append({
                        "id": nuevo_id,
                        "autor": usuario_actual,
                        "titulo": titulo_post,
                        "contenido": contenido_post,
                        "comentarios": []
                    })
                    st.success("Publicación guardada con éxito.")
                    st.rerun()

        st.write("### 🏛 Entradas Recientes")
        
        # Iteración de posts
        for idx, post in enumerate(st.session_state.wiki_posts):
            st.markdown(f"""
            <div class="wiki-post">
                <h4>✨ {post['titulo']}</h4>
                <p style='font-size: 13px; opacity: 0.7; margin:0;'>Por: <b>{post['autor']}</b></p>
                <p style='font-size: 15px; color: #e0e0e0; margin-top:10px;'>{post['contenido']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # --- Panel de Moderación del Instructor (Para el Post) ---
            if es_instructor:
                col_edit, col_del, _ = st.columns([1, 1, 4])
                with col_edit:
                    with st.popover("✏️ Editar Post"):
                        nuevo_tit = st.text_input("Editar Título", post['titulo'], key=f"edit_t_{post['id']}")
                        nuevo_cont = st.text_area("Editar Contenido", post['contenido'], key=f"edit_c_{post['id']}")
                        if st.button("Guardar Cambios", key=f"save_{post['id']}"):
                            post['titulo'] = nuevo_tit
                            post['contenido'] = nuevo_cont
                            st.success("Post actualizado.")
                            st.rerun()
                with col_del:
                    if st.button("🗑️ Eliminar Post", key=f"del_{post['id']}"):
                        st.session_state.wiki_posts.pop(idx)
                        st.warning("Publicación eliminada por el Administrador.")
                        st.rerun()

            # Mostrar comentarios
            if post["comentarios"]:
                st.write("💬 *Comentarios:*")
                for c_idx, c in enumerate(post["comentarios"]):
                    st.markdown(f"""
                    <div class="wiki-comment">
                        <p style='font-size: 14px; margin: 0;'><b>{c['usuario']}:</b> {c['texto']}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # --- Moderación de comentarios (Instructor) ---
                    if es_instructor:
                        if st.button("❌ Eliminar comentario", key=f"del_c_{post['id']}_{c_idx}"):
                            post["comentarios"].pop(c_idx)
                            st.rerun()
            
            # Añadir comentario nuevo
            nuevo_comentario = st.text_input(f"Responder a '{post['titulo']}':", key=f"input_{post['id']}")
            if st.button("Comentar", key=f"btn_{post['id']}"):
                if nuevo_comentario:
                    post["comentarios"].append({
                        "usuario": usuario_actual,
                        "texto": nuevo_comentario
                    })
                    st.rerun()
            st.write("---")
else:
    st.warning("👈 Por favor, identifícate en el panel de la izquierda para entrar al Templo.")
```eof

### Key Changes Summary:
1. **Syntax Fix:** Replaced invalid Unicode string characters and byte spaces (`\xa0`) that triggered the Streamlit execution error.
2. **Evaluaciones CONOCER Tab:**
   - **Evaluación Diagnóstica (0%):** Pre-test checking initial knowledge.
   - **Guía de Observación (40%):** Interactive rubric checklist for practical readings.
   - **Cuestionario Teórico Sumativo (60%):** Multiple-choice test with auto-grading, pass/fail threshold (80% minimum), and balloon animations for successful qualification.
   - **Clave de Respuestas & Retroalimentación:** Detailed technical rationale for every question, available to the instructor or upon request.
