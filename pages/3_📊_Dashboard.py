import streamlit as st
import random
import datetime

st.set_page_config(page_title="Dashboard", page_icon="📊", layout="wide")

st.markdown("# 📊 Dashboard de Performance")
st.caption("Acompanhe seus resultados como afiliado em tempo real")

# --- PERÍODO ---
periodo = st.radio(
    "Período",
    ["Hoje", "7 dias", "15 dias", "30 dias", "Este mês", "Personalizado"],
    horizontal=True
)

if periodo == "Personalizado":
    dp1, dp2 = st.columns(2)
    with dp1:
        data_ini = st.date_input("De", value=datetime.date.today() - datetime.timedelta(days=30))
    with dp2:
        data_fim = st.date_input("Até", value=datetime.date.today())

st.divider()

# --- KPIs PRINCIPAIS ---
k1, k2, k3, k4, k5 = st.columns(5)

with k1:
    st.metric("Faturamento", "R$ 2.847,90", delta="+22% vs período anterior")
with k2:
    st.metric("Comissões", "R$ 412,35", delta="+18%")
with k3:
    st.metric("Cliques Totais", "8.432", delta="+31%")
with k4:
    st.metric("Conversões", "347", delta="+15%")
with k5:
    st.metric("Taxa de Conversão", "4.1%", delta="+0.6%")

st.divider()

# --- GRÁFICOS ---
g1, g2 = st.columns(2)

with g1:
    st.subheader("📈 Comissões por Dia")

    dias = 30
    datas = [(datetime.date.today() - datetime.timedelta(days=i)).strftime("%d/%m") for i in range(dias - 1, -1, -1)]
    valores_comissao = [round(random.uniform(5, 45), 2) for _ in range(dias)]

    chart_data_comissao = dict(zip(datas, valores_comissao))
    st.bar_chart(chart_data_comissao, height=300)

with g2:
    st.subheader("👆 Cliques por Dia")

    valores_cliques = [random.randint(80, 500) for _ in range(dias)]
    chart_data_cliques = dict(zip(datas, valores_cliques))
    st.line_chart(chart_data_cliques, height=300)

st.divider()

# --- TOP PRODUTOS ---
st.subheader("🏆 Top 5 Produtos que Mais Venderam")

top_produtos = [
    {"pos": "🥇", "produto": "Kit 3 Camisetas Dry Fit", "plat": "TikTok Shop", "vendas": 98, "comissao": "R$ 292,06", "taxa": "8.1%"},
    {"pos": "🥈", "produto": "Óculos de Sol Polarizado", "plat": "Shopee", "vendas": 67, "comissao": "R$ 132,66", "taxa": "9.9%"},
    {"pos": "🥉", "produto": "Tênis Nike Revolution 6", "plat": "Mercado Livre", "vendas": 52, "comissao": "R$ 374,40", "taxa": "5.8%"},
    {"pos": "4️⃣", "produto": "Smartwatch D20 Pro", "plat": "Kwai Shop", "vendas": 41, "comissao": "R$ 122,59", "taxa": "7.2%"},
    {"pos": "5️⃣", "produto": "Fone Bluetooth Lenovo LP40", "plat": "Shopee", "vendas": 28, "comissao": "R$ 45,36", "taxa": "8.2%"},
]

for p in top_produtos:
    with st.container(border=True):
        tc1, tc2, tc3, tc4, tc5 = st.columns([0.5, 3, 1.5, 1.5, 1.5])
        with tc1:
            st.markdown(f"### {p['pos']}")
        with tc2:
            st.markdown(f"**{p['produto']}**")
            st.caption(f"📍 {p['plat']}")
        with tc3:
            st.metric("Vendas", p["vendas"])
        with tc4:
            st.metric("Comissão", p["comissao"])
        with tc5:
            st.metric("Taxa Conv.", p["taxa"])

st.divider()

# --- PERFORMANCE POR PLATAFORMA ---
st.subheader("🏪 Performance por Plataforma")

pp1, pp2, pp3 = st.columns(3)

plataformas_stats = [
    {"nome": "Shopee", "emoji": "🟠", "cliques": 3241, "conversoes": 187, "comissao": 198.62, "ticket": 22.40},
    {"nome": "Mercado Livre", "emoji": "🟡", "cliques": 2105, "conversoes": 63, "comissao": 413.89, "ticket": 189.90},
    {"nome": "TikTok Shop", "emoji": "⚫", "cliques": 1876, "conversoes": 98, "comissao": 292.06, "ticket": 19.90},
    {"nome": "Kwai Shop", "emoji": "🟤", "cliques": 890, "conversoes": 41, "comissao": 122.59, "ticket": 29.90},
    {"nome": "Amazon", "emoji": "🔵", "cliques": 456, "conversoes": 15, "comissao": 89.70, "ticket": 399.90},
    {"nome": "Magalu", "emoji": "🟣", "cliques": 312, "conversoes": 8, "comissao": 47.92, "ticket": 149.90},
]

for idx, plat in enumerate(plataformas_stats):
    col_idx = idx % 3
    taxa_p = round(plat["conversoes"] / plat["cliques"] * 100, 1) if plat["cliques"] > 0 else 0
    col = [pp1, pp2, pp3][col_idx]

    with col:
        with st.container(border=True):
            st.markdown(f"### {plat['emoji']} {plat['nome']}")
            pm1, pm2 = st.columns(2)
            with pm1:
                st.metric("Cliques", f"{plat['cliques']:,}")
                st.metric("Conversões", plat["conversoes"])
            with pm2:
                st.metric("Comissão", f"R$ {plat['comissao']:.2f}")
                st.metric("Taxa", f"{taxa_p}%")
            st.caption(f"🎫 Ticket médio: R$ {plat['ticket']:.2f}")

st.divider()

# --- PERFORMANCE POR CANAL ---
st.subheader("📢 Performance por Canal de Divulgação")

canais_stats = [
    {"canal": "Instagram Stories", "emoji": "📸", "cliques": 2890, "conversoes": 145, "comissao": 312.40},
    {"canal": "TikTok", "emoji": "🎵", "cliques": 2340, "conversoes": 112, "comissao": 287.90},
    {"canal": "Bio do perfil", "emoji": "🔗", "cliques": 1560, "conversoes": 98, "comissao": 198.60},
    {"canal": "WhatsApp", "emoji": "💬", "cliques": 890, "conversoes": 52, "comissao": 134.20},
    {"canal": "YouTube Shorts", "emoji": "▶️", "cliques": 567, "conversoes": 23, "comissao": 89.50},
    {"canal": "Telegram", "emoji": "✈️", "cliques": 345, "conversoes": 18, "comissao": 45.30},
    {"canal": "Kwai", "emoji": "🎬", "cliques": 290, "conversoes": 14, "comissao": 38.90},
]

cc1, cc2 = st.columns([2, 1])

with cc1:
    canal_chart = {c["canal"]: c["cliques"] for c in canais_stats}
    st.bar_chart(canal_chart, horizontal=True, height=350)

with cc2:
    for c in canais_stats[:5]:
        taxa_c = round(c["conversoes"] / c["cliques"] * 100, 1) if c["cliques"] > 0 else 0
        st.markdown(f"{c['emoji']} **{c['canal']}**")
        st.caption(f"{c['cliques']:,} cliques · {c['conversoes']} conv. · {taxa_c}% · R$ {c['comissao']:.2f}")

st.divider()

# --- METAS ---
st.subheader("🎯 Metas do Mês")

meta1, meta2, meta3 = st.columns(3)

with meta1:
    with st.container(border=True):
        st.markdown("**💰 Meta de Comissão**")
        meta_comissao = 1000.00
        atual_comissao = 412.35
        pct_comissao = round(atual_comissao / meta_comissao * 100)
        st.progress(pct_comissao / 100)
        st.caption(f"R$ {atual_comissao:.2f} / R$ {meta_comissao:.2f} ({pct_comissao}%)")

with meta2:
    with st.container(border=True):
        st.markdown("**🛒 Meta de Vendas**")
        meta_vendas = 500
        atual_vendas = 347
        pct_vendas = round(atual_vendas / meta_vendas * 100)
        st.progress(pct_vendas / 100)
        st.caption(f"{atual_vendas} / {meta_vendas} vendas ({pct_vendas}%)")

with meta3:
    with st.container(border=True):
        st.markdown("**📢 Meta de Conteúdo**")
        meta_conteudo = 30
        atual_conteudo = 18
        pct_conteudo = round(atual_conteudo / meta_conteudo * 100)
        st.progress(pct_conteudo / 100)
        st.caption(f"{atual_conteudo} / {meta_conteudo} posts ({pct_conteudo}%)")

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("### 📊 Resumo Rápido")
    st.metric("Saldo disponível", "R$ 287,40")
    st.metric("Próximo pagamento", "R$ 124,95")
    st.caption("📅 Pagamento em 05/02/2024")
    st.divider()
    st.markdown("### 🔔 Alertas")
    st.warning("3 links expirando em 48h")
    st.info("Nova campanha Shopee: comissão 2x até sexta")
    st.success("Meta semanal de cliques batida! 🎉")
    st.divider()
    st.markdown("### 📥 Exportar Relatório")
    st.button("📄 Baixar PDF", use_container_width=True, key="dash_pdf")
    st.button("📊 Baixar CSV", use_container_width=True, key="dash_csv")
