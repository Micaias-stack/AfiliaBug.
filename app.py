import streamlit as st

st.set_page_config(
    page_title="AfiliaBug",
    page_icon="🐛",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS CUSTOM ---
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(90deg, #FF4B4B, #FF8C00);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0;
    }
    .sub-header {
        text-align: center;
        color: #AAAAAA;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<p class="main-header">🐛 AfiliaBug</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Ache preços bugados. Crie vídeos. Lucre como afiliado.</p>', unsafe_allow_html=True)

st.divider()

# --- MÉTRICAS RESUMO ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="🔥 Bugs Ativos", value="23", delta="+5 hoje")
with col2:
    st.metric(label="🔗 Seus Links", value="47", delta="+3 novos")
with col3:
    st.metric(label="👆 Cliques Hoje", value="1.2K", delta="+18%")
with col4:
    st.metric(label="💰 Comissão Mês", value="R$ 3.450", delta="+R$ 620")

st.divider()

# --- FEED RÁPIDO ---
st.subheader("⚡ Últimos Preços Bugados")

bugs_exemplo = [
    {
        "produto": "Fone Bluetooth Lenovo LP40",
        "plataforma": "Shopee",
        "preco_original": "R$ 89,90",
        "preco_bug": "R$ 12,90",
        "desconto": "86%",
        "tempo": "3 min atrás"
    },
    {
        "produto": "Tênis Nike Revolution 6",
        "plataforma": "Mercado Livre",
        "preco_original": "R$ 349,90",
        "preco_bug": "R$ 89,90",
        "desconto": "74%",
        "tempo": "7 min atrás"
    },
    {
        "produto": "Kit 3 Camisetas Dry Fit",
        "plataforma": "TikTok Shop",
        "preco_original": "R$ 129,90",
        "preco_bug": "R$ 19,90",
        "desconto": "85%",
        "tempo": "12 min atrás"
    },
    {
        "produto": "Smartwatch D20 Pro",
        "plataforma": "Kwai Shop",
        "preco_original": "R$ 199,90",
        "preco_bug": "R$ 29,90",
        "desconto": "85%",
        "tempo": "18 min atrás"
    },
]

for bug in bugs_exemplo:
    with st.container():
        c1, c2, c3, c4 = st.columns([3, 1.5, 1.5, 1])
        with c1:
            st.markdown(f"**{bug['produto']}**")
            st.caption(f"📍 {bug['plataforma']} · {bug['tempo']}")
        with c2:
            st.markdown(f"~{bug['preco_original']}~")
            st.markdown(f"**🔴 {bug['preco_bug']}**")
        with c3:
            st.markdown(f"### -{bug['desconto']}")
        with c4:
            st.button("🔗 Gerar Link", key=f"btn_{bug['produto']}")
        st.divider()

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("## 🐛 AfiliaBug")
    st.divider()
    st.markdown("### ⚙️ Suas Plataformas")
    st.checkbox("Shopee", value=True)
    st.checkbox("Mercado Livre", value=True)
    st.checkbox("TikTok Shop", value=True)
    st.checkbox("Kwai Shop", value=True)
    st.checkbox("Amazon", value=False)
    st.checkbox("Magalu", value=False)
    st.divider()
    st.markdown("### 🔔 Notificações")
    st.toggle("Push de Preço Bugado", value=True)
    st.slider("Desconto mínimo pra alertar", 30, 90, 60, suffix="%")
    st.divider()
    st.caption("AfiliaBug v1.0 · Feito para afiliados 🚀")
