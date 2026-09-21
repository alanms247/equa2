import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# ========================================
# CONFIGURAÇÃO DA PÁGINA
# ========================================

st.set_page_config(
    page_title="MatFuturo - Equação do 2º Grau",
    page_icon="📐",
    layout="centered"
)

# ========================================
# ESTILO - CORES VERDES DA ESCOLA
# ========================================

st.markdown("""
<style>
    .stApp {
        background-color: #E8F5E9;
    }

    h1, h2, h3 {
        color: #2E7D32;
    }

    .cabecalho {
        color: #388E3C;
        font-size: 28px;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 10px;
    }

    .info {
        color: #333333;
        font-size: 18px;
        text-align: center;
        margin: 8px 0;
    }
</style>
""", unsafe_allow_html=True)

# ========================================
# CAMINHO DA IMAGEM
# ========================================

PASTA_APP = Path(__file__).parent
CAMINHO_IMAGEM = PASTA_APP / "imagem_escola.png"

# ========================================
# CABEÇALHO COM A IMAGEM ENVIADA
# ========================================

col1, col2 = st.columns([1, 1.5], vertical_alignment="center")

with col1:
    if CAMINHO_IMAGEM.exists():
        st.image(str(CAMINHO_IMAGEM), use_container_width=True)
    else:
        st.warning("A imagem 'imagem_escola.png' não foi encontrada.")

with col2:
    st.markdown(
        '<div class="cabecalho">Equação segundo grau</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="info">Cores da escola verde</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="info">Nome da escola: MatFuturo</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="info">App</div>',
        unsafe_allow_html=True
    )

# ========================================
# TÍTULO DO APLICATIVO
# ========================================

st.title("Calculadora de Equação do 2º Grau")

st.write("Resolva uma equação no formato:")
st.latex(r"ax^2 + bx + c = 0")

# ========================================
# ENTRADA DOS VALORES
# ========================================

st.subheader("Digite os valores")

col1, col2, col3 = st.columns(3)

with col1:
    a = st.number_input("Valor de a", value=1.0, step=1.0)

with col2:
    b = st.number_input("Valor de b", value=0.0, step=1.0)

with col3:
    c = st.number_input("Valor de c", value=0.0, step=1.0)

# ========================================
# FUNÇÕES AUXILIARES
# ========================================

def formatar_numero(valor):
    if abs(valor - round(valor)) < 1e-10:
        return str(int(round(valor)))
    return f"{valor:.4f}".rstrip("0").rstrip(".")


def formatar_equacao(a, b, c):
    partes = [f"{formatar_numero(a)}x^2"]

    if b >= 0:
        partes.append(f"+ {formatar_numero(b)}x")
    else:
        partes.append(f"- {formatar_numero(abs(b))}x")

    if c >= 0:
        partes.append(f"+ {formatar_numero(c)}")
    else:
        partes.append(f"- {formatar_numero(abs(c))}")

    return " ".join(partes) + " = 0"

# ========================================
# BOTÃO CALCULAR
# ========================================

if st.button("Calcular", use_container_width=True):

    if a == 0:
        st.error(
            "O valor de 'a' deve ser diferente de zero "
            "para a equação ser do 2º grau."
        )
        st.stop()

    # ========================================
    # DISCRIMINANTE
    # ========================================

    delta = b**2 - 4 * a * c

    st.subheader("Equação")
    st.latex(formatar_equacao(a, b, c))

    st.subheader("Resolução")
    st.latex(r"\Delta = b^2 - 4ac")
    st.latex(
        rf"\Delta = ({formatar_numero(b)})^2 - "
        rf"4({formatar_numero(a)})({formatar_numero(c)})"
    )
    st.latex(rf"\Delta = {formatar_numero(delta)}")

    # ========================================
    # RAÍZES
    # ========================================

    if delta > 0:
        raiz_delta = np.sqrt(delta)
        x1 = (-b + raiz_delta) / (2 * a)
        x2 = (-b - raiz_delta) / (2 * a)

        st.success("A equação possui duas raízes reais diferentes.")

        col1, col2 = st.columns(2)
        with col1:
            st.latex(rf"x_1 = {formatar_numero(x1)}")
        with col2:
            st.latex(rf"x_2 = {formatar_numero(x2)}")

    elif delta == 0:
        x1 = -b / (2 * a)
        st.success("A equação possui uma raiz real (raiz dupla).")
        st.latex(rf"x = {formatar_numero(x1)}")

    else:
        st.warning("A equação não possui raízes reais, pois Δ < 0.")

    # ========================================
    # FÓRMULA DE BHASKARA
    # ========================================

    st.subheader("Fórmula de Bhaskara")
    st.latex(r"x = \frac{-b \pm \sqrt{\Delta}}{2a}")

    # ========================================
    # GRÁFICO
    # ========================================

    st.subheader("Gráfico da função")
    st.write("Função associada à equação:")
    st.latex(
        rf"y = {formatar_numero(a)}x^2 + "
        rf"{formatar_numero(b)}x + "
        rf"{formatar_numero(c)}"
    )

    xv = -b / (2 * a)
    yv = a * xv**2 + b * xv + c

    xmin = xv - 8
    xmax = xv + 8

    x = np.linspace(xmin, xmax, 600)
    y = a * x**2 + b * x + c

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.plot(x, y, linewidth=2, label="f(x) = ax² + bx + c")
    ax.axhline(y=0, linewidth=1)
    ax.axvline(x=0, linewidth=1)

    ax.scatter([xv], [yv], s=70, zorder=5, label="Vértice")

    if delta > 0:
        ax.scatter([x1, x2], [0, 0], s=70, zorder=5, label="Raízes")
    elif delta == 0:
        ax.scatter([x1], [0], s=70, zorder=5, label="Raiz")

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Gráfico da função quadrática")
    ax.grid(True)
    ax.legend()

    st.pyplot(fig)
    plt.close(fig)

# ========================================
# RODAPÉ
# ========================================

st.divider()
st.caption("MatFuturo • Aplicativo de Equação do 2º Grau")
