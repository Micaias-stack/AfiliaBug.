import streamlit as st

st.set_page_config(
    page_title="AfiliaBug 🐞",
    page_icon="🐞",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- HEADER ---
h1, h2 = st.columns([1, 11])
with h1:
    st.markdown("# 🐞")
with h2:
    st.markdown("# AfiliaBug")
    st.caption("Encontre preços bugados · Gere links · Crie vídeos · Acompanhe resultados")

st.divider()

# --- KPIs RÁPIDOS ---
st.subheader("📊 Resumo de Hoje")

k1, k2, k3, k4, k5 = st.columns(5)
with k1:
    st.metric("Bugs Encontrados", "23", delta="+5 hoje")
with k2:
    st.metric("Links Ativos", "47", delta="+3")
with k3:
    st.metric("Cliques Hoje", "1.247", delta="+18%")
with k4:
    st.metric("Conversões", "89", delta="+12%")
with k5:
    st.metric("Comissão do Dia", "R$ 342,50", delta="+22%")

st.divider()

# --- DESTAQUES ---
st.subheader("🔥 Bugs Quentes Agora")

d1, d2, d3 = st.columns(3)

with d1:
    with st.container(border=True):
        st.markdown("### 🎧 Fone Bluetooth LP40")
        st.markdown("~~R$ 89,90~~ → **R$ 12,49**")
        st.caption("🏪 Shopee · ⏰ Expira em 2h")
        st.progress(0.86, text="86% vendido")
        st.button("🔗 Gerar Link", key="bug1", use_container_width=True)

with d2:
    with st.container(border=True):
        st.markdown("### 👟 Tênis Nike Revolution 6")
        st.markdown("~~R$ 349,90~~ → **R$ 89,90**")
        st.caption("🏪 Mercado Livre · ⏰ Expira em 5h")
        st.progress(0.72, text="72% vendido")
        st.button("🔗 Gerar Link", key="bug2", use_container_width=True)

with d3:
    with st.container(border=True):
        st.markdown("### 👕 Kit 3 Camisetas Dry Fit")
        st.markdown("~~R$ 129,90~~ → **R$ 29,70**")
        st.caption("🏪 TikTok Shop · ⏰ Expira em 8h")
        st.progress(0.54, text="54% vendido")
        st.button("🔗 Gerar Link", key="bug3", use_container_width=True)

st.divider()

# --- COMO FUNCIONA ---
st.subheader("🚀 Como Funciona")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("### 1️⃣ Encontre")
    st.markdown("Nosso scanner monitora preços bugados em tempo real nas maiores plataformas.")

with c2:
    st.markdown("### 2️⃣ Gere o Link")
    st.markdown("Crie seu link de afiliado rastreável com um clique.")

with c3:
    st.markdown("### 3️⃣ Divulgue")
    st.markdown("Use nosso editor de vídeo para criar conteúdo pronto para TikTok e Reels.")

with c4:
    st.markdown("### 4️⃣ Lucre")
    st.markdown("Acompanhe cliques, conversões e comissões no dashboard em tempo real.")

st.divider()

# --- PLATAFORMAS ---
st.subheader("🏪 Plataformas Monitoradas")

p1, p2, p3, p4, p5, p6 = st.columns(6)
with p1:
    st.markdown("#### 🟠 Shopee")
    st.caption("234 bugs ativos")
with p2:
    st.markdown("#### 🔵 Mercado Livre")
    st.caption("189 bugs ativos")
with p3:
    st.markdown("#### ⚫ TikTok Shop")
    st.caption("156 bugs ativos")
with p4:
    st.markdown("#### 🟡 Kwai Shop")
    st.caption("98 bugs ativos")
with p5:
    st.markdown("#### 🟤 Amazon")
    st.caption("142 bugs ativos")
with p6:
    st.markdown("#### 🔴 Magalu")
    st.caption("87 bugs ativos")

st.divider()

# --- RANKING ---
st.subheader("🏆 Top Afiliados da Semana")

ranking = [
    {"pos": "🥇", "nome": "Ana Silva", "vendas": 234, "comissao": "R$ 4.521,30"},
    {"pos": "🥈", "nome": "Carlos Tech", "vendas": 198, "comissao": "R$ 3.890,00"},
    {"pos": "🥉", "nome": "Julia Moda", "vendas": 176, "comissao": "R$ 3.245,80"},
    {"pos": "4º", "nome": "Pedro Gamer", "vendas": 154, "comissao": "R$ 2.980,50"},
    {"pos": "5º", "nome": "Mari Beleza", "vendas": 143, "comissao": "R$ 2.670,20"},
]

for r in ranking:
    rc1, rc2, rc3, rc4 = st.columns([0.5, 3, 1.5, 1.5])
    with rc1:
        st.markdown(f"**{r['pos']}**")
    with rc2:
        st.markdown(f"**{r['nome']}**")
    with rc3:
        st.markdown(f"🛒 {r['vendas']} vendas")
    with rc4:
        st.markdown(f"💰 {r['comissao']}")

st.divider()

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("### 🐞 AfiliaBug")
    st.caption("v1.0.0 · Beta")
    st.divider()
    st.markdown("### ⚡ Acesso Rápido")
    st.page_link("pages/1_🔥_Precos_Bugados.py", label="🔥 Preços Bugados", icon="🔥")
    st.page_link("pages/2_🎬_Editor_Video.py", label="🎬 Editor de Vídeo", icon="🎬")
    st.page_link("pages/3_📊_Dashboard.py", label="📊 Dashboard", icon="📊")
    st.page_link("pages/4_🔗_Meus_Links.py", label="🔗 Meus Links", icon="🔗")
    st.divider()
    st.markdown("### 📈 Status do Scanner")
    st.success("✅ Scanner ativo")
    st.caption("Última varredura: há 3 min")
    st.caption("Próxima varredura: em 2 min")
