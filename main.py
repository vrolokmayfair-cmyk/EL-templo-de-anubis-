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
    .eval-card { background-color: #111111; border: 1px solid #d4af37; padding: 18px; border-radius: 8px; margin-bottom: 15px; }
    .feedback-box { background-color: #1c1a0e; border-left: 4px solid #d4af37; padding: 12px 18px; border-radius: 4px; margin-top: 10px; margin-bottom: 10px; }
    .teacher-badge { background-color: #d4af37; color: #000; padding: 3px 8px; border-radius: 4px; font-weight: bold; font-size: 12px; }
    </style>
    """, unsafe_allow_html=True)

# --- PORTADA PRINCIPAL ---
try:
    st.image("anubis-the-ancient-egyptian-jackal-headed-god-seat.jpeg", use_container_width=True)
except Exception:
    st.info("🌙 El Templo de Anubis — Cuestionario y Plataforma de Estudio")

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
        st.link_button("📂 Abrir Presentación Maestra", "[https://docs.google.com/presentation/d/1dO3YrrZYeU4uNyeJEsMKxhjCSlC_P0GDpVcJr9w5m2Q/edit](https://docs.google.com/presentation/d/1dO3YrrZYeU4uNyeJEsMKxhjCSlC_P0GDpVcJr9w5m2Q/edit)")

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
        "🏛 Inicio", 
        "Tarot de Marsella", 
        "Runas Vikingas", 
        "Wicca & Magia", 
        "📊 Evaluaciones", 
        "📜 Wiki Comunitaria"
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
                "url": "[https://drive.google.com/file/d/159pd32ErBY5ivTRUhZoY-sHxstGc9puB/view](https://drive.google.com/file/d/159pd32ErBY5ivTRUhZoY-sHxstGc9puB/view)", 
                "dia": 0
            },
            {
                "titulo": "Material Clase 2", 
                "instruccion": "Descarga el pdf de los arcanos mayores del tarot marsella, ya que se ocuparan en las siguientes clases.",
                "url": "[https://drive.google.com/file/d/1FOcbDLocK2i6xf_FH-APCF2GvM7iZwY5/view](https://drive.google.com/file/d/1FOcbDLocK2i6xf_FH-APCF2GvM7iZwY5/view)", 
                "dia": 7
            },
            {
                "titulo": "Material Clase 3", 
                "instruccion": "Descarga el manual de tiradas para tener una amplia gama de opciones en tus lecturas adicionales a las que se te brindaron en clase.",
                "url": "[https://drive.google.com/file/d/19nYTrsNW76GI4pLvGddXZlZ4XfMdgFeW/view](https://drive.google.com/file/d/19nYTrsNW76GI4pLvGddXZlZ4XfMdgFeW/view)", 
                "dia": 14
            },
            {
                "titulo": "Material Clase de Arcanos Menores", 
                "instruccion": "El siguiente pdf incluye el tarot marsella completo para su utilizacion de forma personal.",
                "url": "[https://drive.google.com/file/d/1jYaMsGXcIbMYw18GNNqUTbOyidi5UjWa/view](https://drive.google.com/file/d/1jYaMsGXcIbMYw18GNNqUTbOyidi5UjWa/view)", 
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

    # --- MÓDULO DE EVALUACIONES COMPLETO ---
    with tab_eval:
        st.subheader("📊 Sistema Oficial de Evaluaciones de Competencias")
        st.write("Instrumentos pedagógicos para medir el aprendizaje teórico y práctico en el Templo de Anubis.")

        eval_sub1, eval_sub2, eval_sub3, eval_sub4 = st.tabs([
            "🩺 1. Evaluación Diagnóstica",
            "📋 2. Guía de Observación (40%)",
            "📝 3. Evaluación Final (60%)",
            "🔑 4. Clave del Facilitador"
        ])

        # 1. EVALUACIÓN DIAGNÓSTICA (10 Preguntas)
        with eval_sub1:
            st.markdown("### 🩺 Evaluación Diagnóstica Inicial (Sin peso numérico - 15 min)")
            st.caption("Objetivo: Conocer el nivel previo de los participantes sobre Tarot y simbolismo.")
            
            with st.form("form_diag"):
                qd1 = st.text_area("1. ¿Qué entiendes por 'Arcanos Mayores'?")
                qd2 = st.text_area("2. Menciona los cuatro elementos asociados a los palos del Tarot y su correspondencia (Fuego, Agua, Aire, Tierra):")
                qd3 = st.radio("3. ¿Qué significa cuando un personaje del Tarot mira hacia la izquierda?", 
                               ["Hacia el futuro y la acción activa", "Hacia el pasado, el origen, lo femenino o la introspección", "Hacia la confrontación directa en el presente", "Neutralidad absoluta"], index=None)
                qd4 = st.text_area("4. Nombra tres colores principales del Tarot de Marsella y un significado simbólico para cada uno:")
                qd5 = st.text_area("5. ¿Qué representa 'El Loco' (Le Mat) en el viaje del Tarot?")
                qd6 = st.radio("6. Diferencia entre figuras sedentes y figuras de pie en la iconografía marsellesa:", 
                               ["Sedentes = Acción y dinamismo / De pie = Estabilidad", "Sedentes = Estabilidad, poder establecido y reflexión / De pie = Acción, dinamismo y transición", "Ambas significan lo mismo"], index=None)
                qd7 = st.text_area("7. ¿Qué simboliza la mano derecha en la mayoría de los arcanos?")
                qd8 = st.radio("8. ¿En qué septenario se ubica 'La Justicia' y qué plano representa?", 
                               ["Septenario I - Plano Material", "Septenario II - Plano Mental y Transmutación", "Septenario III - Plano Espiritual"], index=None)
                qd9 = st.text_area("9. ¿Qué es el 'código cromático' según la tradición marsellesa?")
                qd10 = st.text_area("10. ¿Cuál es el objetivo general de este curso?")
                
                sub_diag = st.form_submit_button("Enviar Evaluación Diagnóstica")
                if sub_diag:
                    st.success("✅ Evaluación Diagnóstica enviada correctamente. Consulta la retroalimentación en la pestaña 'Clave del Facilitador'.")

        # 2. GUÍA DE OBSERVACIÓN (FORMATIVA - 40%) - MÓDULO DEL MAESTRO
        with eval_sub2:
            st.markdown("### 📋 Evaluación Formativa – Guía de Observación (40% - Práctica Demostrativa)")
            st.caption("Instrucciones: El participante realizará una lectura de 3 cartas (tirada libre o pasado-presente-futuro) aplicando los criterios vistos en clase.")
            
            if es_instructor:
                st.markdown("<span class='teacher-badge'>MODO EVALUADOR ACTIVO</span>", unsafe_allow_html=True)
                nombre_evaluado = st.text_input("Nombre del Participante Evaluado:", placeholder="Ej. Juan Pérez")
                fecha_eval = st.date_input("Fecha de Evaluación:", datetime.now(), key="fech_eval_m")
                
                col_obs1, col_obs2 = st.columns(2)
                with col_obs1:
                    i1 = st.slider("1. Identifica correctamente la dirección de la mirada y su significado temporal", 0, 10, 8, key="sl_1")
                    i2 = st.slider("2. Analiza el color dominante y su relación con el plano de la consulta", 0, 10, 8, key="sl_2")
                    i3 = st.slider("3. Reconoce el septenario al que pertenecen las cartas y su plano (Material/Mental/Espiritual)", 0, 10, 8, key="sl_3")
                with col_obs2:
                    i4 = st.slider("4. Describe correctamente postura, manos y elementos clave de cada arcano", 0, 10, 8, key="sl_4")
                    i5 = st.slider("5. Integra los arquetipos en una narrativa coherente y hermenéutica", 0, 10, 8, key="sl_5")
                
                total_obs_pts = i1 + i2 + i3 + i4 + i5
                porcentaje_obs = total_obs_pts * 2
                peso_final_obs = (porcentaje_obs / 100) * 40
                
                st.markdown(f"**Puntos Totales Obtenidos:** `{total_obs_pts} / 50 pts`")
                st.markdown(f"**Porcentaje de Desempeño Práctico:** `{porcentaje_obs}%`")
                st.metric("Ponderación Formativa Final (40% máx):", f"{peso_final_obs:.1f}% / 40%")
                
                obs_comments = st.text_area("Comentarios del Facilitador:", placeholder="Anota aquí las fortalezas y áreas de mejora del participante...")
                if st.button("Guardar Evaluación Práctica", key="btn_save_prac"):
                    st.success(f"Evaluación de {nombre_evaluado} guardada exitosamente con {peso_final_obs:.1f}% / 40%.")
            else:
                st.info("ℹ️ Esta sección es utilizada por el **Maestro Vrolok** durante tu práctica en vivo de 3 cartas.")
                st.markdown("""
                | Ítem | Criterio de Evaluación | Puntos Máximos |
                |---|---|---|
                | **1** | Identifica correctamente la dirección de la mirada y su significado temporal | 10 pts |
                | **2** | Analiza el color dominante y su relación con el plano de la consulta | 10 pts |
                | **3** | Reconoce el septenario al que pertenecen las cartas y su plano (Material/Mental/Espiritual) | 10 pts |
                | **4** | Describe correctamente postura, manos y elementos clave de cada arcano | 10 pts |
                | **5** | Integra los arquetipos en una narrativa coherente y hermenéutica | 10 pts |
                | **Total** | **Suma total de desempeño (Escala × 2 = % Final)** | **50 pts (100%)** |
                """)

        # 3. EVALUACIÓN FINAL SUMATIVA (60%)
        with eval_sub3:
            st.markdown("### 📝 Evaluación Final – Cuestionario Teórico (60%)")
            st.caption("Evaluación sumativa dividida en Opción Múltiple (40 pts) y Preguntas Abiertas (60 pts).")

            st.markdown("#### **Parte I – Opción Múltiple (40 puntos)**")
            q_f1 = st.radio("1. ¿Qué representa principalmente el color Azul en el Tarot de Marsella?",
                            ["a) Acción y voluntad", "b) Recepción, espiritualidad e introspección", "c) Inteligencia y claridad mental", "d) Transformación radical"], index=None, key="qf1")
            
            q_f2 = st.radio("2. La mirada hacia la derecha indica:",
                            ["a) Pasado", "b) Futuro y acción", "c) Presente absoluto", "d) Introspección"], index=None, key="qf2")
            
            q_f3 = st.radio("3. ¿En qué septenario se encuentra 'El Diablo'?",
                            ["a) Septenario I", "b) Septenario II", "c) Septenario III"], index=None, key="qf3")
            
            q_f4 = st.radio("4. La postura sedente simboliza principalmente:",
                            ["a) Acción y movimiento", "b) Estabilidad y poder establecido", "c) Transición"], index=None, key="qf4")
            
            q_f5 = st.radio("5. ¿Qué arcano representa la 'transmutación y limpieza'?",
                            ["a) La Templanza", "b) La Muerte (Arcano XIII)", "c) La Estrella"], index=None, key="qf5")

            st.markdown("#### **Parte II – Preguntas Abiertas Cortas (60 puntos)**")
            qa1 = st.text_area("1. Explica el significado de las manos ocultas en la iconografía marsellesa:", key="qa1_k")
            qa2 = st.text_area("2. Describe el significado de El Carro (VII) y su relación con el dominio de opuestos:", key="qa2_k")
            qa3 = st.text_area("3. ¿Cómo se interpreta la dominancia de color rojo en una tirada?", key="qa3_k")
            qa4 = st.text_area("4. Explica la estructura de los tres septenarios y qué plano de conciencia representa cada uno:", key="qa4_k")
            qa5 = st.text_area("5. Analiza el arcano 'La Estrella' (XVII) según simbolismo, color y arquetipo:", key="qa5_k")

            if st.button("Enviar Examen Sumativo Final", key="btn_sub_final"):
                pts_op = 0
                if q_f1 == "b) Recepción, espiritualidad e introspección": pts_op += 8
                if q_f2 == "b) Futuro y acción": pts_op += 8
                if q_f3 == "c) Septenario III": pts_op += 8
                if q_f4 == "b) Estabilidad y poder establecido": pts_op += 8
                if q_f5 == "b) La Muerte (Arcano XIII)": pts_op += 8
                
                st.success(f"Examen entregado. Calificación automática Parte I (Opción múltiple): {pts_op} / 40 pts.")
                st.info("La Parte II (Preguntas abiertas - 60 pts) será revisada por el Maestro Vrolok.")

        # 4. CLAVE DE RESPUESTAS DEL FACILITADOR
        with eval_sub4:
            st.markdown("### 🔑 Clave Completa de Respuestas (Para el Facilitador)")
            
            if es_instructor or st.checkbox("Mostrar Claves Oficiales y Criterios de Evaluación", key="chk_claves"):
                st.markdown("""
                <div class="feedback-box">
                    <h4>🩺 Clave de la Evaluación Diagnóstica:</h4>
                    <ol>
                        <li><b>Arcanos Mayores:</b> Los 22 arcanos que representan el viaje completo de la conciencia / arquetipos universales.</li>
                        <li><b>Correspondencia de Palos:</b> Bastones = Fuego, Copas = Agua, Espadas = Aire, Oros = Tierra.</li>
                        <li><b>Mirada a la izquierda:</b> Hacia el pasado, lo femenino, el origen o la introspección.</li>
                        <li><b>Colores principales:</b> Azul (recepción/espiritualidad), Rojo (acción/voluntad), Amarillo (inteligencia/luz divina).</li>
                        <li><b>El Loco (Le Mat):</b> Potencial puro, impulso vital incipiente, libertad absoluta, viajero sin ataduras.</li>
                        <li><b>Figuras Sedentes vs De Pie:</b> Sedentes = estabilidad, poder establecido, reflexión. De pie = acción, dinamismo, transición.</li>
                        <li><b>Mano derecha:</b> Ejecución, voluntad manifiesta, acción.</li>
                        <li><b>La Justicia:</b> Septenario II (VIII-XIV) – Plano Mental y Transmutación.</li>
                        <li><b>Código cromático:</b> El uso pedagógico e iniciático del color como estado de la materia y el espíritu (no decorativo).</li>
                        <li><b>Objetivo general:</b> Identificar y analizar simbolismos visuales, código cromático y claves de interpretación de los 22 Arcanos Mayores para estructurar lecturas hermenéuticas.</li>
                    </ol>
                </div>

                <div class="feedback-box">
                    <h4>📝 Clave Examen Final Sumativo:</h4>
                    <p><b>Parte I (Opción Múltiple):</b></p>
                    <ul>
                        <li>1 -> <b>b)</b> Recepción, espiritualidad e introspección</li>
                        <li>2 -> <b>b)</b> Futuro y acción</li>
                        <li>3 -> <b>c)</b> Septenario III</li>
                        <li>4 -> <b>b)</b> Estabilidad y poder establecido</li>
                        <li>5 -> <b>b)</b> La Muerte (Arcano XIII)</li>
                    </ul>
                    <p><b>Parte II (Preguntas Abiertas):</b></p>
                    <ul>
                        <li><b>1. Manos ocultas:</b> Secretos, manipulación o energía no manifestada.</li>
                        <li><b>2. El Carro:</b> Triunfo, dirección consciente, dominio de fuerzas opuestas (caballos blanco/negro), movimiento victorioso.</li>
                        <li><b>3. Dominancia de Rojo:</b> Acción, impulso vital, plano material, trabajo humano consciente, instinto.</li>
                        <li><b>4. Tres Septenarios:</b> Sept. I (I-VII): Plano Material / Sept. II (VIII-XIV): Plano Mental / Sept. III (XV-XXI): Plano Espiritual.</li>
                        <li><b>5. La Estrella (XVII):</b> Fe, purificación, esperanza renovada, generosidad, entrega transparente, conexión con el cosmos (color azul dominante).</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.info("🔒 Ingresa la Clave Maestra en el panel lateral o marca la casilla para consultar las claves pedagógicas.")

    # --- WIKI CON GESTIÓN ADMINISTRATIVA ---
    with tab_wiki:
        st.subheader("📜 Bitácora de Conocimiento Esotérico")
        
        with st.expander("✍️ Crear Nueva Publicación en la Wiki"):
            titulo_post = st.text_input("Título de la publicación:", key="w_tit_new")
            contenido_post = st.text_area("¿Qué conocimiento deseas plasmar?:", key="w_cont_new")
            if st.button("Publicar en el Templo", key="btn_w_new"):
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
        
        for idx, post in enumerate(st.session_state.wiki_posts):
            st.markdown(f"""
            <div class="wiki-post">
                <h4>✨ {post['titulo']}</h4>
                <p style='font-size: 13px; opacity: 0.7; margin:0;'>Por: <b>{post['autor']}</b></p>
                <p style='font-size: 15px; color: #e0e0e0; margin-top:10px;'>{post['contenido']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            if es_instructor:
                col_edit, col_del, _ = st.columns([1, 1, 4])
                with col_edit:
                    with st.popover("✏️ Editar Post", key=f"popover_{post['id']}"):
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

            if post["comentarios"]:
                st.write("💬 *Comentarios:*")
                for c_idx, c in enumerate(post["comentarios"]):
                    st.markdown(f"""
                    <div class="wiki-comment">
                        <p style='font-size: 14px; margin: 0;'><b>{c['usuario']}:</b> {c['texto']}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    if es_instructor:
                        if st.button("❌ Eliminar comentario", key=f"del_c_{post['id']}_{c_idx}"):
                            post["comentarios"].pop(c_idx)
                            st.rerun()
            
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
