import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Gran Promoción de la Marca", page_icon="🎁")

# 1. Descripción de la promoción (Instrucción 1)
st.title("¡Participa y Gana con Nosotros!")
st.image("https://via.placeholder.com/800x400.png?text=Logo+de+la+Promoción") # Reemplazar con logo real
st.write("""
### ¿Cómo participar?
Busca el logo de nuestra promoción en los productos adheridos. 
Dentro del empaque encontrarás un código único de 2 letras y 4 números.
¡Ingrésalo abajo para saber si eres uno de nuestros ganadores!
""")

# 2. Entrada de código (Instrucción 2)
st.subheader("Ingresa tu código")
codigo_usuario = st.text_input("Ejemplo: AA6767", max_chars=6).upper()

# 3. Lógica de validación (Instrucción 3)
codigos_ganadores = ["RT2344", "EE8877", "MK4400"]

if st.button("Verificar código"):
    if codigo_usuario in codigos_ganadores:
        st.balloons()
        st.success(f"¡FELICITACIONES! El código {codigo_usuario} es GANADOR. Ponte en contacto con nosotros.")
    elif codigo_usuario == "":
        st.warning("Por favor, ingresa un código.")
    else:
        st.error("Sigue participando. ¡No te rindas, la próxima podría ser la tuya!")