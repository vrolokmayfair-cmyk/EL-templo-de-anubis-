import streamlit as st

# ==========================================
# 1. CONFIGURACIÓN DE PÁGINA Y TEMA MÍSTICO
# ==========================================
st.set_page_config(
    page_title="El Templo de Anubis - Plataforma Completa",
    page_icon="📿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados (Dorado #d4af37, Fondo Oscuro #0b0b0b, Fuentes Cinzel & Lato)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Lato:wght@300;400;700&display=swap');
    
    .stApp {
        background-color: #0b0b0b;
        color: #f5f5dc;
        font-family: 'Lato', sans-serif;
    }
    
    h1, h2, h3, h4, h5 {
        color: #d4af37 !important;
        font-family: 'Cinzel', serif !important;
        text-transform: uppercase;
        letter-spacing: 1.5px;
    }
    
    .conocer-badge {
        background: linear-gradient(135deg, #2b1f09, #d4af37);
        color: #000;
        font-size: 13px;
        font-weight: 700;
        padding: 6px 16px;
        border-radius: 20px;
        border: 1px solid #ffd700;
        display: inline-block;
        margin-bottom: 15px;
    }
    
    .gold-card {
        background: rgba(22, 22, 22, 0.9);
        border: 1px solid rgba(212, 175, 55, 0.4);
        border-radius: 10px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    }
    
    .gold-card:hover {
        border-color: #d4af37;
        box-shadow: 0 0 15px rgba(212, 175, 55, 0.2);
    }
    
    .quote-box {
        background: rgba(30, 30, 30, 0.6);
        border-left: 4px solid #d4af37;
        padding: 20px 25px;
        margin: 20px 0;
        font-style: italic;
        border-radius: 0 8px 8px 0;
    }
    
    .key-box {
        background: #121212;
        border-left: 4px solid #d4af37;
        padding: 14px 18px;
        margin-bottom: 12px;
        border-radius: 0 8px 8px 0;
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #d4af37, #996515) !important;
        color: #000 !important;
        font-family: 'Cinzel', serif !important;
        font-weight: bold !important;
        border: none !important;
        padding: 10px 24px !important;
        border-radius: 6px !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton>button:hover {
        background: linear-gradient(135deg, #ffd700, #b8860b) !important;
        box-shadow: 0 0 12px rgba(212, 175, 55, 0.5) !important;
    }
    
    /* Personalización de inputs radio y checkbox */
    .stRadio label, .stCheckbox label {
        color: #e0e0e0 !important;
        font-size: 16px !important;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. INICIALIZACIÓN DE ESTADO DE SESIÓN
# ==========================================
if 'diag_score' not in st.session_state:
    st.session_state.diag_score = 0
if 'prac_score' not in st.session_state:
    st.session_state.prac_score = 0
if 'theo_score' not in st.session_state:
    st.session_state.theo_score = 0

# ==========================================
# 3. BARRA NAVEGACIONAL LATERAL
# ==========================================
st.sidebar.image("https://www.aongking.com/wp-content/uploads/2025/09/Aongking-Customized-Bronze-Ancient-Egyptian-Anubis-Statues.jpg", use_container_width=True)
st.sidebar.title("EL TEMPLO DE ANUBIS")
st.sidebar.caption("Sabiduría Antigua, Maestría Moderna")

seccion_principal = st.sidebar.selectbox(
    "Navegación General:",
    ["🏛️ Presentación de la Academia", "📝 Sistema de Evaluaciones CONOCER"]
)

# ==========================================
# 4. MÓDULO: PRESENTACIÓN DE LA ACADEMIA
# ==========================================
if seccion_principal == "🏛️ Presentación de la Academia":
    
    sub_seccion = st.sidebar.radio(
        "Ver Diapositiva / Tema:",
        [
            "1. Inicio y Bienvenida",
            "2. Nuestra Esencia y Propósito",
            "3. Módulos y Pilares",
            "4. Instructor Maestro",
            "5. Tarot de Marsella & Anatomía Sagrada",
            "6. Runas y Wicca",
            "7. Metodología de Estudio",
            "8. Sabiduría Ancestral",
            "9. Impacto y Comunidad",
            "10. Recursos e Instrumentos"
        ]
    )
    
    if sub_seccion == "1. Inicio y Bienvenida":
        st.markdown('<div class="conocer-badge">Academia Mística & Formación Profesional</div>', unsafe_allow_html=True)
        st.title("EL TEMPLO DE ANUBIS")
        st.subheader("Guardianes de la Sabiduría Ancestral")
        
        col1, col2 = st.columns([1, 1])
        with col1:
            st.write("""
            Bienvenido al umbral del conocimiento sagrado. **El Templo de Anubis** es un espacio dedicado 
            a la preservación, enseñanza y práctica rigurosa de las artes esotéricas, el Tarot de Marsella, 
            las Runas Vikingas y la Filosofía Wicca.
            """)
            st.info("🔮 **Mapeo de la Psique:** Formamos lectores e iniciados orientados a la ética, la introspección y el autoconocimiento real.")
        with col2:
            st.image("https://www.aongking.com/wp-content/uploads/2025/09/Aongking-Customized-Bronze-Ancient-Egyptian-Anubis-Statues.jpg", caption="Estatua de Anubis - Guardian del Umbral", use_container_width=True)

    elif sub_seccion == "2. Nuestra Esencia y Propósito":
        st.header("Nuestra Esencia")
        st.write("Conectando el plano terrenal con la sabiduría oculta.")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="gold-card">
                <h3>📜 Preservación Hermética</h3>
                <p>Rescatamos y protegemos el conocimiento tradicional de las artes adivinatorias y la filosofía oculta para el buscador moderno.</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="gold-card">
                <h3>🏛️ Maestría Técnica</h3>
                <p>Entregamos herramientas con rigor académico y técnico, superando visiones supersticiosas para lograr una lectura intuitiva y profunda.</p>
            </div>
            """, unsafe_allow_html=True)

    elif sub_seccion == "3. Módulos y Pilares":
        st.header("Módulos Principales de la Academia")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="gold-card">
                <h3>🃏 Módulo 1: Tarot de Marsella</h3>
                <p>Estudio exhaustivo de los 22 Arcanos Mayores y Menores, Anatomía Sagrada, Leyes de Camoin y ética del consultante. Un viaje de 0 a maestro.</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="gold-card">
                <h3>ᚱ Módulo 2: Runas & Wicca</h3>
                <p>El lenguaje de los glifos escandinavos y la magia natural. Conexión con los ciclos de la tierra y los elementos en un entorno de respeto y devoción.</p>
            </div>
            """, unsafe_allow_html=True)

    elif sub_seccion == "4. Instructor Maestro":
        st.header("Guía e Instructor")
        
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image("https://news.emory.edu/stories/2026/05/er_commencement_award_exemplary_teacher_bonfiglio_07-05-2026/thumbs/story_main.jpg", caption="Juan Carlos Sumano / Maestro Vrolok", use_container_width=True)
        with col2:
            st.subheader("Juan Carlos Sumano (Maestro Vrolok)")
            st.write("""
            Instructor Senior con décadas de experiencia en el estudio e investigación de las artes esotéricas. 
            Fundador de **El Templo de Anubis**, dedicado a transmitir la enseñanza hermética con rigor, 
            ética e integridad inquebrantable.
            """)
            st.markdown("""
            <div class="quote-box">
                "Enseñar no es dar información; es encender una antorcha en el camino del buscador para que pueda sostener la mirada de la verdad."
            </div>
            """, unsafe_allow_html=True)

    elif sub_seccion == "5. Tarot de Marsella & Anatomía Sagrada":
        st.header("El Tarot de Marsella")
        st.write("Anatomía Sagrada y Simbología Pura")
        
        col1, col2 = st.columns(2)
        with col1:
            st.write("""
            Nuestra instrucción enseña que cada carta es un organismo vivo que respira sabiduría. 
            Analizamos la **Anatomía Sagrada**:
            * **Miradas y Orientación:** Pasado (Izquierda), Presente (Frontal), Futuro (Derecha).
            * **Posturas:** Figuras sedentes (estabilidad/trono) vs. de pie (acción/transición).
            * **Código Cromático:** Azul (Mente/Recepción), Rojo (Cuerpo/Acción), Amarillo (Luz Divina/Conciencia).
            """)
        with col2:
            st.image("http://witchycauldron.com/cdn/shop/files/81YEHo-7H4L._AC_SL1500.jpg?v=1726244827", caption="Mazo Ilustrado Tarot de Marsella", use_container_width=True)

    elif sub_seccion == "6. Runas y Wicca":
        st.header("Runas Vikingas & Wicca")
        st.write("El Lenguaje de los Dioses Antiguos")
        
        col1, col2 = st.columns([2, 1])
        with col1:
            st.write("""
            Exploramos las **Runas Vikingas** como símbolos de poder, meditación e intencionalidad espiritual. 
            En combinación con la filosofía **Wicca**, enseñamos el respeto por la naturaleza, la creación de altares de poder 
            y la alineación con los cuatro elementos.
            """)
            st.success("🌿 **Conexión Elemental:** Desarrollo de intuición a través del trabajo ritual consciente y responsable.")
        with col2:
            st.image("https://images.stockcake.com/public/e/0/9/e092456a-6812-4223-a573-06f88005c9f9_large/mystical-glowing-rune-stockcake.jpg", caption="Simbolismo Rúnico", use_container_width=True)

    elif sub_seccion == "7. Metodología de Estudio":
        st.header("Metodología de Aprendizaje")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""
            <div class="gold-card">
                <h4>⌛ Liberación Progresiva</h4>
                <p>Contenido desbloqueado cada 7 días para permitir una asimilación pausada de cada concepto.</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="gold-card">
                <h4>📜 Autogestión Honesta</h4>
                <p>El alumno registra de forma consciente su propio progreso de iniciación y aprendizaje.</p>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown("""
            <div class="gold-card">
                <h4>🔒 Privacidad & Rigor</h4>
                <p>Plataforma exclusiva protegida con material en PDF, lecturas guiadas y presentaciones maestras.</p>
            </div>
            """, unsafe_allow_html=True)

    elif sub_seccion == "8. Sabiduría Ancestral":
        st.header("Frase y Citas del Templo")
        st.markdown("""
        <div class="quote-box" style="font-size: 24px; text-align: center;">
            "La sabiduría no se encuentra, se revela a quien tiene el valor de cruzar el umbral del Templo y sostener la mirada de Anubis."
            <br><br>
            <strong style="color: #d4af37; font-size: 18px;">— Manuscrito del Templo</strong>
        </div>
        """, unsafe_allow_html=True)

    elif sub_seccion == "9. Impacto y Comunidad":
        st.header("Nuestra Comunidad de Iniciados")
        
        col1, col2 = st.columns([1, 2])
        with col1:
            st.metric(label="Alumnos Formados", value="500+", delta="98% Recomendación")
        with col2:
            st.write("""
            Hemos impactado la vida de cientos de buscadores en todo el mundo hispanohablante. 
            Nuestra red de estudiantes aplica el Tarot y las artes esotéricas como herramientas reales 
            de desarrollo personal, acompañamiento holístico e introspección.
            """)

    elif sub_seccion == "10. Recursos e Instrumentos":
        st.header("Herramientas de Poder del Iniciado")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("https://images.stockcake.com/public/4/e/9/4e9520de-de66-48f8-9e98-579e8fc1fc97_large/sacred-golden-ankh-stockcake.jpg", caption="El Ankh Dorado", use_container_width=True)
        with col2:
            st.image("https://www.divineintents.com/cdn/shop/files/amethyst-rune-stone-set-in-velvet-pouch-25-stone-set__05130.jpg", caption="Set de Runas", use_container_width=True)
        with col3:
            st.image("https://cdn11.bigcommerce.com/s-jehe8mdt/images/stencil/1500x1500/products/2769/15008/Gothic_Witchcraft_Candle_Holder_witchcraft_witchcore_witchy_decor_Witch_store_wicca_pagan_magick_spellwork_ceremonial_magick_lunar_magick_scrying_ritual_tools__23485.1754681102.jpg?c=2", caption="Altar Wicca", use_container_width=True)

# ==========================================
# 5. MÓDULO: SISTEMA DE EVALUACIONES CONOCER
# ==========================================
elif seccion_principal == "📝 Sistema de Evaluaciones CONOCER":
    
    st.markdown('<div class="conocer-badge">Estándares de Competencia CONOCER EC0217.1 / EC0301 / EC0366</div>', unsafe_allow_html=True)
    st.title("Sistema Oficial de Evaluación de Competencias")
    st.caption("Alineación Instruccional para la Certificación y Acreditación del Curso")
    
    eval_menu = st.sidebar.radio(
        "Instrumento de Evaluación:",
        [
            "1. Esquema de Evaluación (Encuadre)",
            "2. Evaluación Diagnóstica (0%)",
            "3. Guía de Observación - Práctica (40%)",
            "4. Cuestionario Teórico Sumativo (60%)",
            "5. Clave de Respuestas (Evaluador)",
            "6. Resumen de Calificación Global"
        ]
    )
    
    # 5.1 ENCUADRE
    if eval_menu == "1. Esquema de Evaluación (Encuadre)":
        st.header("Esquema General de Evaluación")
        st.write("Estructura de instrumentos de medición de aprendizaje conforme a las normas oficiales de formación:")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""
            <div class="gold-card">
                <h4>1. Diagnóstica</h4>
                <p><strong>Ponderación:</strong> 0%</p>
                <p>Mide los conocimientos previos sobre simbología, arquetipos y lenguaje óptico al iniciar el curso.</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="gold-card">
                <h4>2. Formativa (Práctica)</h4>
                <p><strong>Ponderación:</strong> 40%</p>
                <p>Evaluación de desempeño mediante Guía de Observación / Lista de Cotejo en tirada de 3 cartas.</p>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown("""
            <div class="gold-card">
                <h4>3. Sumativa (Teoría)</h4>
                <p><strong>Ponderación:</strong> 60%</p>
                <p>Cuestionario final de opción múltiple sobre Septenarios, Código Cromático y Anatomía Sagrada.</p>
            </div>
            """, unsafe_allow_html=True)
            
        st.info("🎓 **Criterio Mínimo de Aprobación:** 80% (80 puntos globales) acumulados entre la Evaluación Formativa y Sumativa.")

    # 5.2 EVALUACIÓN DIAGNÓSTICA
    elif eval_menu == "2. Evaluación Diagnóstica (0%)":
        st.header("Evaluación Diagnóstica Inicial")
        st.caption("Responde a las siguientes preguntas iniciales para conocer tus conocimientos previos:")
        
        q1 = st.radio(
            "1. En la xilografía de Marsella, ¿qué indica la orientación de la mirada hacia la IZQUIERDA?",
            ["A) Proyección hacia el futuro y acción masculina",
             "B) Conexión con el pasado, origen e introspección",
             "C) Confrontación frontal y justicia absoluta",
             "D) Neutralidad absoluta ante la consulta"],
            key="diag_q1"
        )
        
        q2 = st.radio(
            "2. ¿A qué plano o elemento corresponden las ESPADAS en la estructura del Tarot?",
            ["A) Elemento Agua / Emociones",
             "B) Elemento Aire / Plano Mental y Pensamiento",
             "C) Elemento Fuego / Pasión e Impulso",
             "D) Elemento Tierra / Bienes Materiales"],
            key="diag_q2"
        )
        
        q3 = st.radio(
            "3. El Arcano Cero (Le Mat / El Loco) representa:",
            ["A) El potencial puro, energía incipiente y libertad de viaje",
             "B) La culminación total y el éxito material del viaje",
             "C) La estabilidad en el trono y el poder establecido",
             "D) La muerte física e inevitable fin del proceso"],
            key="diag_q3"
        )
        
        if st.button("Validar Diagnóstico"):
            score = 0
            if q1.startswith("B"): score += 1
            if q2.startswith("B"): score += 1
            if q3.startswith("A"): score += 1
            st.session_state.diag_score = score
            st.success(f"Evaluación diagnóstica completada: {score} de 3 respuestas correctas (Sin peso en la nota final).")

    # 5.3 GUÍA DE OBSERVACIÓN
    elif eval_menu == "3. Guía de Observación - Práctica (40%)":
        st.header("Guía de Observación - Práctica Demostrativa")
        st.caption("Instrucción para el Evaluador: Verifique el cumplimiento de los criterios durante la práctica de lectura de 3 cartas.")
        
        c1 = st.checkbox("1. Análisis de Orientación: Identifica correctamente la dirección de miradas (pasado, presente o futuro) entre los arcanos. (10 pts)")
        c2 = st.checkbox("2. Código Cromático: Reconoce el plano dominante de la lectura según los colores de la tirada. (10 pts)")
        c3 = st.checkbox("3. Clasificación de Septenario: Ubica los arcanos en su Septenario correspondiente (Material, Mental o Espiritual). (10 pts)")
        c4 = st.checkbox("4. Síntesis Hermenéutica: Estructura la conclusión integrando postura (sedente/de pie) y gestos con rigor técnico CONOCER. (10 pts)")
        
        prac_total = sum([10 for c in [c1, c2, c3, c4] if c])
        st.session_state.prac_score = prac_total
        
        st.metric(label="Calificación Práctica Formativa", value=f"{prac_total} / 40 Puntos", delta=f"{(prac_total/40)*100:.0f}%")

    # 5.4 CUESTIONARIO SUMATIVO
    elif eval_menu == "4. Cuestionario Teórico Sumativo (60%)":
        st.header("Cuestionario Teórico Sumativo Final")
        st.caption("Evaluación escrita de conocimientos teóricos sobre los Módulos I, II y III del curso.")
        
        fq1 = st.radio("1. Según la Anatomía Sagrada, ¿qué simbolizan las FIGURAS SEDENTES (ej. La Emperatriz, El Emperador)?",
                       ["A) Transición súbita, viaje inestable y dinamismo",
                        "B) Estabilidad, trono, poder establecido y reflexión",
                        "C) Renuncia voluntaria y cambio de perspectiva física",
                        "D) Negación del conocimiento formal"], key="fq1")
        
        fq2 = st.radio("2. ¿Qué significado transmiten las MANOS OCULTAS (bajo mantos o espaldas)?",
                       ["A) Voluntad activa y ejecución directa",
                        "B) Escucha pasiva y recepción afectiva",
                        "C) Secretos, reservas de energía o manipulación sutil",
                        "D) Dominio absoluto del plano terrenal"], key="fq2")
        
        fq3 = st.radio("3. La MIRADA FRONTAL en un personaje del Tarot (ej. La Justicia) indica:",
                       ["A) Presente absoluto, confrontación directa y transparencia",
                        "B) Búsqueda del origen e introspección del pasado",
                        "C) Impulso activo proyectado hacia el futuro",
                        "D) Duda e indecisión entre dos opciones"], key="fq3")
        
        fq4 = st.radio("4. En el Código Cromático de Marsella, el color AMARILLO / ORO simboliza:",
                       ["A) Trabajo humano, fuerza bruta y carne terrenal",
                        "B) Luz divina, conciencia solar e inteligencia trascendente",
                        "C) Pasión descontrolada e instintos primitivos",
                        "D) Reposo, silencio e inconsciente marino"], key="fq4")
        
        fq5 = st.radio("5. El SEPTENARIO II (Arcanos VIII a XIV) corresponde al plano de evolución:",
                       ["A) Plano Material y Concreción Terrenal",
                        "B) Plano Mental, Equilibrio e Introspección Transmutadora",
                        "C) Plano Espiritual, Iluminación y Cosmogonía",
                        "D) Plano Subconsciente e Ilusiones Nocturnas"], key="fq5")
        
        fq6 = st.radio("6. Arcano XV (El Diablo) y Arcano XVI (La Torre) pertenecen al Septenario:",
                       ["A) Primer Septenario (Plano Físico)",
                        "B) Segundo Septenario (Plano Intelectual)",
                        "C) Tercer Septenario (Plano Espiritual y Liberación)",
                        "D) Arcanos de transición sin asignación"], key="fq6")
        
        if st.button("Calcular Evaluación Sumativa"):
            correct = 0
            if fq1.startswith("B"): correct += 1
            if fq2.startswith("C"): correct += 1
            if fq3.startswith("A"): correct += 1
            if fq4.startswith("B"): correct += 1
            if fq5.startswith("B"): correct += 1
            if fq6.startswith("C"): correct += 1
            
            theo_total = (correct / 6) * 60
            st.session_state.theo_score = theo_total
            st.success(f"Puntaje Obtenido: {theo_total:.1f} / 60 Puntos ({correct} de 6 reactivos acertados)")

    # 5.5 CLAVE DE RESPUESTAS
    elif eval_menu == "5. Clave de Respuestas (Evaluador)":
        st.header("Clave Oficial de Respuestas CONOCER")
        st.warning("🔒 Guía de consulta exclusiva para el Evaluador / Facilitador Instruccional.")
        
        st.markdown("""
        <div class="key-box">
            <h4>Evaluación Diagnóstica:</h4>
            <p><strong>P1 -> B:</strong> La orientación a la izquierda representa la mirada hacia el pasado e introspección.</p>
            <p><strong>P2 -> B:</strong> Las Espadas corresponden al elemento Aire y al Plano Mental.</p>
            <p><strong>P3 -> A:</strong> Le Mat / El Loco representa el potencial puro y la energía inicial (Arcano 0).</p>
        </div>
        
        <div class="key-box">
            <h4>Cuestionario Sumativo:</h4>
            <p><strong>P1 -> B:</strong> Las figuras sedentes expresan estabilidad, trono y poder afirmado.</p>
            <p><strong>P2 -> C:</strong> Las manos ocultas indican reserva de energía, secretos o manejo sutil.</p>
            <p><strong>P3 -> A:</strong> La mirada frontal enfrenta al consultante con el presente y la verdad directa.</p>
            <p><strong>P4 -> B:</strong> El color Amarillo/Oro simboliza luz divina, conciencia solar e inteligencia despierta.</p>
            <p><strong>P5 -> B:</strong> El Septenario II (VIII a XIV) representa el trabajo en el Plano Mental y la transmutación.</p>
            <p><strong>P6 -> C:</strong> Del Arcano XV al XXI corresponden al Septenario III (Plano Espiritual y liberación).</p>
        </div>
        """, unsafe_allow_html=True)

    # 5.6 RESUMEN Y DICTAMEN
    elif eval_menu == "6. Resumen de Calificación Global":
        st.header("Dictamen de Certificación y Resumen Global")
        
        p_score = st.session_state.prac_score
        t_score = st.session_state.theo_score
        total = p_score + t_score
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Evaluación Formativa", f"{p_score} / 40 pts")
        col2.metric("Evaluación Sumativa", f"{t_score:.1f} / 60 pts")
        col3.metric("Nota Global Acumulada", f"{total:.1f} / 100 pts")
        
        st.markdown("---")
        
        if total >= 80:
            st.balloons()
            st.success(f"🎉 **DICTAMEN CONOCER: COMPETENTE (APROBADO)**\n\nEl participante ha alcanzado **{total:.1f}%** de rendimiento (Criterio mínimo: 80%). Acreditación otorgada por El Templo de Anubis.")
        else:
            st.error(f"❌ **DICTAMEN CONOCER: TODAVÍA NO COMPETENTE**\n\nEl participante obtuvo **{total:.1f}%** (Criterio mínimo: 80%). Se requiere reevaluación tras reforzar contenidos teóricos o prácticos.")
```eof

He unificado la presentación completa de **El Templo de Anubis** junto con el módulo de evaluaciones alineado a los estándares CONOCER en un único archivo ejecutable de Python para Streamlit (`app.py`).

### Estructura del código generado:
1. **Pestaña 🏛️ Presentación de la Academia:**
   - 10 diapositivas/secciones interactivas navegables (Inicio, Esencia, Módulos, Instructor Maestro, Tarot & Anatomía Sagrada, Runas & Wicca, Metodología, Sabiduría, Comunidad e Instrumentos).
2. **Pestaña 📝 Sistema de Evaluaciones CONOCER:**
   - Encuadre e Instrumentos (EC0217.1).
   - Evaluación Diagnóstica Interactiva (0%).
   - Guía de Observación para la práctica demostrativa (40%).
   - Cuestionario Teórico Sumativo de opción múltiple (60%) con calificación automática.
   - Clave Oficial de Respuestas para el Evaluador.
   - Resumen Global y Dictamen de Acreditación (Competente / Todavía No Competente).
