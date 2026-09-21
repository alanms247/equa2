import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# ========================================
# CONFIGURAÇÃO DA PÁGINA
# ========================================

st.set_page_config(
    page_title="Equação do 1º Grau",
    page_icon="📈",
    layout="centered"
)

st.markdown("""
    <style>
        /* Fundo principal da página */
        .stApp {
            background-color: #0D47A1;
        }
    </style>
""", unsafe_allow_html=True)

# ========================================
# CAMINHO DA IMAGEM
# ========================================

PASTA_APP = Path(__file__).parent
CAMINHO_LOGO = PASTA_APP / "unnamed.jpg"

if CAMINHO_LOGO.exists():
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.image(
            str(CAMINHO_LOGO),
            use_container_width=True
        )
else:
    st.warning("A imagem unnamed.jpg não foi encontrada. ⚠️")


# ========================================
# TÍTULO
# ========================================

st.title("📈 Equação do 1º Grau")

st.write("Equação no formato:")

st.latex(r"ax + b = 0")


# ========================================
# ENTRADA DOS VALORES
# ========================================

a = st.number_input(
    "Digite o valor de a",
    value=1,
    step=1
)

b = st.number_input(
    "Digite o valor de b",
    value=0,
    step=1
)


# ========================================
# BOTÃO CALCULAR
# ========================================

if st.button("Calcular", use_container_width=True):

    # ========================================
    # VERIFICA O VALOR DE A
    # ========================================

    if a == 0:

        if b == 0:
            st.warning(
                "A equação possui infinitas soluções."
            )

        else:
            st.error(
                "A equação não possui solução."
            )

    else:

        # ====================================
        # CALCULA A RAIZ
        # ====================================

        x_raiz = -b / a

        # ====================================
        # RESULTADO
        # ====================================

        st.subheader("Resultado")

        st.write(
            "A raiz da equação é:"
        )

        st.success(
            f"x = {x_raiz:.2f}"
        )

        # ====================================
        # MOSTRA A EQUAÇÃO
        # ====================================

        st.subheader("Equação")

        if b >= 0:
            st.latex(
                f"{a}x + {b} = 0"
            )
        else:
            st.latex(
                f"{a}x - {abs(b)} = 0"
            )

        # ====================================
        # MOSTRA O CÁLCULO
        # ====================================

        st.subheader("Resolução")

        if b >= 0:
            st.latex(
                f"{a}x + {b} = 0"
            )
        else:
            st.latex(
                f"{a}x - {abs(b)} = 0"
            )

        st.latex(
            f"{a}x = {-b}"
        )

        st.latex(
            f"x = \\frac{{{-b}}}{{{a}}}"
        )

        st.latex(
            f"x = {x_raiz:.2f}"
        )

        # ====================================
        # GRÁFICO
        # ====================================

        st.subheader("📊 Gráfico da função")

        # Cria intervalo para o gráfico
        x = np.linspace(
            x_raiz - 10,
            x_raiz + 10,
            500
        )

        # Função do primeiro grau
        y = a * x + b

        # Cria gráfico
        fig, ax = plt.subplots(
            figsize=(8, 5)
        )

        # Desenha a reta
        ax.plot(
            x,
            y,
            linewidth=2,
            label=f"y = {a}x + {b}"
        )

        # Eixo X
        ax.axhline(
            y=0,
            linewidth=1
        )

        # Eixo Y
        ax.axvline(
            x=0,
            linewidth=1
        )

        # Marca a raiz
        ax.scatter(
            [x_raiz],
            [0],
            s=100,
            zorder=5,
            label=f"Raiz x = {x_raiz:.2f}"
        )

        # ====================================
        # CONFIGURAÇÃO DO GRÁFICO
        # ====================================

        ax.set_xlabel("x")
        ax.set_ylabel("y")

        ax.set_title(
            "Gráfico da Função do 1º Grau"
        )

        ax.grid(True)
        ax.legend()

        # ====================================
        # MOSTRA GRÁFICO
        # ====================================

        st.pyplot(fig)

        plt.close(fig)


# ========================================
# RODAPÉ
# ========================================

st.divider()

st.caption(
    "📚 Calculadora de Equação do 1º Grau"
)
