import streamlit as st
import random

st.set_page_config(page_title="Meus Links", page_icon="🔗", layout="wide")

st.markdown("# 🔗 Meus Links de Afiliado")
st.caption("Gerencie, rastreie e otimize todos os seus links")

# --- KPIs ---
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.metric("Total de Links", "47", delta="+3 hoje")
with m2:
    st.metric("Cliques Hoje", "1.247", delta="+18%")
with m3:
    st.metric("Conversões Hoje", "89", delta="+12%")
with m4:
    st.metric("Taxa de Conversão", "7.1%", delta="+0.8%")

st.divider()

# --- CRIAR NOVO LINK ---
with st.expander("➕ Criar Novo Link de Afiliado", expanded=False):
    with st.form("novo_link_form"):
        nl1, nl2 = st.columns(2)
        with nl1:
            nl_url = st.text_input("URL do produto", placeholder="https://shopee.com.br/produto-exemplo...")
            nl_plat = st.selectbox("Plataforma", [
                "Shopee", "Mercado Livre", "TikTok Shop",
                "Kwai Shop", "Amazon", "Magalu"
            ])
            nl_nome = st.text_input("Nome/apelido do link", placeholder="Ex: Fone LP40 Stories")
        with nl2:
            nl_campanha = st.text_input("Campanha (UTM)", placeholder="Ex: stories_julho")
            nl_canal = st.selectbox("Canal de divulgação", [
                "Instagram Stories", "TikTok", "Kwai", "YouTube Shorts",
                "Bio do perfil", "WhatsApp", "Telegram", "Outro"
            ])
            nl_tags = st.text_input("Tags (separadas por vírgula)", placeholder="Ex: fone, bluetooth, shopee")

        nl_submit = st.form_submit_button("🔗 Gerar Link Rastreável", use_container_width=True)

        if nl_submit:
            if nl_url:
                link_gerado = f"https://afiliabug.link/{random.randint(10000, 99999)}"
                st.success("Link criado com sucesso!")
                st.code(link_gerado, language=None)
            else:
                st.error("Cole a URL do produto para gerar o link.")

st.divider()

# --- FILTROS ---
f1, f2, f3 = st.columns(3)
with f1:
    filtro_plat = st.multiselect("Filtrar por plataforma", [
        "Shopee", "Mercado Livre", "TikTok Shop",
        "Kwai Shop", "Amazon", "Magalu"
    ])
with f2:
    filtro_canal = st.multiselect("Filtrar por canal", [
        "Instagram Stories", "TikTok", "Kwai", "YouTube Shorts",
        "Bio do perfil", "WhatsApp", "Telegram"
    ])
with f3:
    filtro_ordenar = st.selectbox("Ordenar por", [
        "Mais cliques", "Mais conversões", "Mais recentes", "Maior comissão"
    ])

# --- DADOS SIMULADOS ---
links_data = [
    {
        "nome": "Fone LP40 - Stories",
        "produto": "Fone Bluetooth Lenovo LP40",
        "plat": "Shopee",
        "canal": "Instagram Stories",
        "link": "afiliabug.link/38291",
        "cliques": 342,
        "conversoes": 28,
        "comissao": 45.36,
        "criado": "2024-01-15",
        "status": "ativo",
        "tags": ["fone", "bluetooth", "shopee"]
    },
    {
        "nome": "Tênis Nike - TikTok",
        "produto": "Tênis Nike Revolution 6",
        "plat": "Mercado Livre",
        "canal": "TikTok",
        "link": "afiliabug.link/49102",
        "cliques": 891,
        "conversoes": 52,
        "comissao": 374.40,
        "criado": "2024-01-14",
        "status": "ativo",
        "tags": ["tenis", "nike", "ml"]
    },
    {
        "nome": "Kit Camiseta - Bio",
        "produto": "Kit 3 Camisetas Dry Fit",
        "plat": "TikTok Shop",
        "canal": "Bio do perfil",
        "link": "afiliabug.link/57382",
        "cliques": 1203,
        "conversoes": 98,
        "comissao": 292.06,
        "criado": "2024-01-13",
        "status": "ativo",
        "tags": ["camiseta", "kit", "moda"]
    },
    {
        "nome": "Smartwatch D20 - Kwai",
        "produto": "Smartwatch D20 Pro",
        "plat": "Kwai Shop",
        "canal": "Kwai",
        "link": "afiliabug.link/61948",
        "cliques": 567,
        "conversoes": 41,
        "comissao": 122.59,
        "criado": "2024-01-12",
        "status": "ativo",
        "tags": ["smartwatch", "relogio", "kwai"]
    },
    {
        "nome": "Paleta Sombras - WhatsApp",
        "produto": "Paleta de Sombras Ruby Rose",
        "plat": "Shopee",
        "canal": "WhatsApp",
        "link": "afiliabug.link/72654",
        "cliques": 234,
        "conversoes": 19,
        "comissao": 23.60,
        "criado": "2024-01-11",
        "status": "ativo",
        "tags": ["maquiagem", "beleza", "shopee"]
    },
    {
        "nome": "Air Fryer - YouTube",
        "produto": "Fritadeira Air Fryer 4L",
        "plat": "Magalu",
        "canal": "YouTube Shorts",
        "link": "afiliabug.link/83019",
        "cliques": 456,
        "conversoes": 15,
        "comissao": 134.85,
        "criado": "2024-01-10",
        "status": "expirado",
        "tags": ["airfryer", "cozinha", "magalu"]
    },
    {
        "nome": "Óculos Polarizado - Telegram",
        "produto": "Óculos de Sol Polarizado",
        "plat": "Shopee",
        "canal": "Telegram",
        "link": "afiliabug.link/91847",
        "cliques": 678,
        "conversoes": 67,
        "comissao": 132.66,
        "criado": "2024-01-09",
        "status": "ativo",
        "tags": ["oculos", "moda", "shopee"]
    },
    {
        "nome": "Mochila 40L - Stories",
        "produto": "Mochila Impermeável 40L",
        "plat": "Mercado Livre",
        "canal": "Instagram Stories",
        "link": "afiliabug.link/10293",
        "cliques": 189,
        "conversoes": 11,
        "comissao": 39.49,
        "criado": "2024-01-08",
        "status": "ativo",
        "tags": ["mochila", "esporte", "ml"]
    },
]

# --- APLICAR FILTROS ---
filtered = links_data

if filtro_plat:
    filtered = [l for l in filtered if l["plat"] in filtro_plat]
if filtro_canal:
    filtered = [l for l in filtered if l["canal"] in filtro_canal]

sort_map = {
    "Mais cliques": ("cliques", True),
    "Mais conversões": ("conversoes", True),
    "Mais recentes": ("criado", True),
    "Maior comissão": ("comissao", True),
}
sort_key, sort_rev = sort_map[filtro_ordenar]
filtered.sort(key=lambda x: x[sort_key], reverse=sort_rev)

# --- EXIBIR LINKS ---
st.markdown(f"**{len(filtered)} links encontrados**")
st.text("")

for link in filtered:
    taxa = round(link["conversoes"] / link["cliques"] * 100, 1) if link["cliques"] > 0 else 0
    status_emoji = "🟢" if link["status"] == "ativo" else "🔴"

    with st.container(border=True):
        lc1, lc2, lc3, lc4, lc5 = st.columns([2.5, 1.2, 1.2, 1.2, 1])

        with lc1:
            st.markdown(f"**{link['nome']}** {status_emoji}")
            st.caption(f"📦 {link['produto']}")
            st.caption(f"📍 {link['plat']} · 📢 {link['canal']} · 📅 {link['criado']}")
            st.code(link["link"], language=None)

        with lc2:
            st.metric("Cliques", f"{link['cliques']:,}")

        with lc3:
            st.metric("Conversões", f"{link['conversoes']}", delta=f"{taxa}% taxa")

        with lc4:
            st.metric("Comissão", f"R$ {link['comissao']:.2f}")

        with lc5:
            st.button("📋 Copiar", key=f"copy_{link['link']}")
            st.button("📊 Stats", key=f"stats_{link['link']}")
            if link["status"] == "ativo":
                st.button("⏸️ Pausar", key=f"pause_{link['link']}")
            else:
                st.button("▶️ Reativar", key=f"react_{link['link']}")

st.divider()

# --- TOP PERFORMERS ---
st.subheader("🏆 Top Performers da Semana")

tp1, tp2, tp3 = st.columns(3)

with tp1:
    with st.container(border=True):
        st.markdown("### 🥇 Mais Cliques")
        st.markdown("**Kit 3 Camisetas Dry Fit**")
        st.caption("TikTok Shop · Bio do perfil")
        st.metric("Cliques", "1.203")

with tp2:
    with st.container(border=True):
        st.markdown("### 🥈 Mais Conversões")
        st.markdown("**Kit 3 Camisetas Dry Fit**")
        st.caption("TikTok Shop · Bio do perfil")
        st.metric("Conversões", "98")

with tp3:
    with st.container(border=True):
        st.markdown("### 🥉 Maior Comissão")
        st.markdown("**Tênis Nike Revolution 6**")
        st.caption("Mercado Livre · TikTok")
        st.metric("Comissão", "R$ 374,40")

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("### ⚡ Ações Rápidas")
    st.button("🔗 Criar Link Rápido", use_container_width=True, key="sb_criar")
    st.button("📊 Exportar CSV", use_container_width=True, key="sb_csv")
    st.button("📄 Exportar PDF", use_container_width=True, key="sb_pdf")
    st.divider()
    st.markdown("### 📊 Resumo")
    st.metric("Links Ativos", "41")
    st.metric("Links Expirados", "6")
    st.metric("Comissão Total", "R$ 1.164,82")
    st.divider()
    st.markdown("### 🏷️ Tags Populares")
    st.caption("shopee (3) · moda (2) · bluetooth (1) · nike (1) · cozinha (1)")
