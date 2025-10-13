import streamlit as st
import pandas as pd

# --- CONFIGURACIÓN DEL DASHBOARD ---
st.set_page_config(page_title="Quiz: Salud de Cuidadores Primarios", layout="centered")

# --- BASE DE PREGUNTAS DIRECTAMENTE EN EL CÓDIGO ---
data = [
    {
        "pregunta": "¿Qué se entiende por cuidador primario informal?",
        "opcion_a": "Un profesional de la salud que trabaja en hospitales.",
        "opcion_b": "Una persona que cuida a alguien dependiente sin recibir pago ni formación profesional.",
        "opcion_c": "Un cuidador contratado por el Estado.",
        "opcion_d": "Un voluntario de una institución de beneficencia.",
        "respuesta_correcta": "b",
        "retro_correcta": "✅ Correcto: Es quien brinda atención continua sin recibir pago ni formación profesional.",
        "retro_incorrecta": "❌ Incorrecto: El cuidador informal no es profesional ni remunerado."
    },
    {
        "pregunta": "¿Cuál es una consecuencia frecuente del rol de cuidador primario en la salud mental?",
        "opcion_a": "Reducción del estrés y mayor bienestar emocional.",
        "opcion_b": "Aumento del tiempo libre y la satisfacción personal.",
        "opcion_c": "Aparición de síntomas de ansiedad, depresión o sobrecarga.",
        "opcion_d": "Mejoría en la calidad del sueño.",
        "respuesta_correcta": "c",
        "retro_correcta": "✅ Correcto: La carga emocional del cuidado prolongado genera ansiedad y depresión.",
        "retro_incorrecta": "❌ Incorrecto: El cuidado prolongado incrementa el estrés, no lo reduce."
    },
    {
        "pregunta": "¿Qué factor físico es común entre los cuidadores primarios debido al esfuerzo continuo?",
        "opcion_a": "Dolores musculares y fatiga crónica.",
        "opcion_b": "Aumento de la resistencia física.",
        "opcion_c": "Disminución del cansancio corporal.",
        "opcion_d": "Incremento de la fuerza muscular.",
        "respuesta_correcta": "a",
        "retro_correcta": "✅ Correcto: Las tareas repetitivas y el esfuerzo físico generan fatiga crónica.",
        "retro_incorrecta": "❌ Incorrecto: El exceso de esfuerzo no mejora la salud física, la deteriora."
    },
    {
        "pregunta": "¿Qué recurso psicológico puede ayudar a los cuidadores a mantener su salud mental?",
        "opcion_a": "Aislamiento social.",
        "opcion_b": "Terapia o grupos de apoyo.",
        "opcion_c": "Evitar hablar de sus emociones.",
        "opcion_d": "Dedicarse exclusivamente al cuidado sin descanso.",
        "respuesta_correcta": "b",
        "retro_correcta": "✅ Correcto: El apoyo psicológico reduce la sobrecarga y fortalece la resiliencia.",
        "retro_incorrecta": "❌ Incorrecto: El aislamiento y el silencio agravan el estrés."
    },
    {
        "pregunta": "¿Qué característica del rol de cuidador contribuye más al agotamiento físico y emocional?",
        "opcion_a": "La falta de tiempo para sí mismo.",
        "opcion_b": "La flexibilidad de horarios.",
        "opcion_c": "La independencia del cuidado.",
        "opcion_d": "El apoyo constante de otros familiares.",
        "respuesta_correcta": "a",
        "retro_correcta": "✅ Correcto: La dedicación continua y falta de autocuidado provocan agotamiento.",
        "retro_incorrecta": "❌ Incorrecto: La falta de descanso es el principal factor de riesgo."
    },
    {
        "pregunta": "¿Cómo puede afectar la falta de sueño al cuidador primario?",
        "opcion_a": "Mejora la concentración y el estado de ánimo.",
        "opcion_b": "No tiene efectos significativos.",
        "opcion_c": "Aumenta la irritabilidad, el cansancio y los errores en el cuidado.",
        "opcion_d": "Incrementa la energía física.",
        "respuesta_correcta": "c",
        "retro_correcta": "✅ Correcto: El sueño insuficiente causa irritabilidad y errores en el cuidado.",
        "retro_incorrecta": "❌ Incorrecto: Dormir poco deteriora la salud mental y física."
    },
    {
        "pregunta": "¿Qué práctica favorece la salud física del cuidador primario?",
        "opcion_a": "Descuidar la alimentación para priorizar el cuidado.",
        "opcion_b": "Evitar cualquier tipo de ejercicio.",
        "opcion_c": "Mantener una dieta equilibrada y realizar actividad física regular.",
        "opcion_d": "Dormir menos para aprovechar el tiempo.",
        "respuesta_correcta": "c",
        "retro_correcta": "✅ Correcto: La buena alimentación y el ejercicio fortalecen la salud general.",
        "retro_incorrecta": "❌ Incorrecto: Descuidar el cuerpo incrementa el agotamiento."
    },
    {
        "pregunta": "¿Qué término se utiliza para describir el desgaste emocional del cuidador por la carga prolongada?",
        "opcion_a": "Empatía funcional.",
        "opcion_b": "Síndrome de burnout o de sobrecarga del cuidador.",
        "opcion_c": "Motivación intrínseca.",
        "opcion_d": "Resiliencia emocional.",
        "respuesta_correcta": "b",
        "retro_correcta": "✅ Correcto: El burnout refleja agotamiento físico y emocional prolongado.",
        "retro_incorrecta": "❌ Incorrecto: No se trata de una fortaleza, sino de un desgaste."
    },
    {
        "pregunta": "¿Qué factor social protege la salud mental del cuidador primario?",
        "opcion_a": "El aislamiento y la autosuficiencia.",
        "opcion_b": "La falta de comunicación familiar.",
        "opcion_c": "El apoyo social y familiar constante.",
        "opcion_d": "Evitar pedir ayuda para no molestar a los demás.",
        "respuesta_correcta": "c",
        "retro_correcta": "✅ Correcto: Las redes de apoyo reducen el estrés y mejoran la calidad de vida.",
        "retro_incorrecta": "❌ Incorrecto: El aislamiento aumenta el riesgo de sobrecarga emocional."
    },
    {
        "pregunta": "¿Por qué es importante atender la salud física y mental de los cuidadores?",
        "opcion_a": "Porque mejora el bienestar del cuidador y la calidad del cuidado brindado.",
        "opcion_b": "Porque sólo beneficia al paciente.",
        "opcion_c": "Porque no tiene repercusión en el proceso de cuidado.",
        "opcion_d": "Porque se trata de una obligación legal.",
        "respuesta_correcta": "a",
        "retro_correcta": "✅ Correcto: El bienestar del cuidador influye directamente en el del paciente.",
        "retro_incorrecta": "❌ Incorrecto: Cuidar del propio bienestar mejora el proceso de atención."
    }
]

preguntas = pd.DataFrame(data)

# --- ESTADOS DE SESIÓN ---
if "indice" not in st.session_state:
    st.session_state.indice = 0
if "puntaje" not in st.session_state:
    st.session_state.puntaje = 0
if "respondido" not in st.session_state:
    st.session_state.respondido = False
if "respuesta_usuario" not in st.session_state:
    st.session_state.respuesta_usuario = None

# --- FUNCIÓN PARA MOSTRAR PREGUNTAS ---
def mostrar_pregunta(indice):
    fila = preguntas.iloc[indice]
    st.markdown(f"### Pregunta {indice + 1}: {fila['pregunta']}")
    opciones = [fila['opcion_a'], fila['opcion_b'], fila['opcion_c'], fila['opcion_d']]
    return fila, opciones

# --- INTERFAZ PRINCIPAL ---
st.title("🧩 Quiz: Salud mental y física de cuidadores primarios")

if st.session_state.indice < len(preguntas):
    fila, opciones = mostrar_pregunta(st.session_state.indice)
    respuesta = st.radio("Selecciona tu respuesta:", opciones, index=None, key=f"resp_{st.session_state.indice}")

    if st.button("Responder"):
        if respuesta is None:
            st.warning("Selecciona una opción antes de continuar.")
        else:
            correcta = fila["respuesta_correcta"]
            mapa = {
                "a": fila["opcion_a"],
                "b": fila["opcion_b"],
                "c": fila["opcion_c"],
                "d": fila["opcion_d"]
            }

            if respuesta == mapa[correcta]:
                st.success(fila["retro_correcta"])
                st.session_state.puntaje += 1
            else:
                st.error(fila["retro_incorrecta"])

            st.session_state.respondido = True

    if st.session_state.respondido:
        if st.button("Siguiente ➜"):
            st.session_state.indice += 1
            st.session_state.respondido = False
            st.rerun()

else:
    total = len(preguntas)
    st.subheader("🎯 Resultado final")
    st.success(f"Tu puntaje: **{st.session_state.puntaje} / {total}**")
    porcentaje = int((st.session_state.puntaje / total) * 100)
    st.progress(porcentaje)

    if porcentaje == 100:
        st.balloons()
        st.write("🌟 ¡Excelente trabajo! Dominaste el tema.")
    elif porcentaje >= 70:
        st.write("💪 Buen resultado, conoces bien el tema.")
    else:
        st.write("📘 Puedes repasar los conceptos y volver a intentarlo.")

    if st.button("🔁 Reiniciar quiz"):
        st.session_state.indice = 0
        st.session_state.puntaje = 0
        st.session_state.respondido = False
        st.rerun()
