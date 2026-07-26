import streamlit as st
import random

st.set_page_config(page_title="Preços Bugados", page_icon="🔥", layout="wide")

st.markdown("# 🔥 Radar de Preços Bugados")
st.caption("Monitoramento em tempo real de glitches de preço nos marketplaces")

# --- FILTROS ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    plataforma = st.multiselect(
        "Plataforma",
        ["Shopee", "Mercado Livre", "TikTok Shop", "Kwai Shop", "Amazon", "Magalu"],
        default=["Shopee", "Mercado Livre", "TikTok Shop"],
    )

with col2:
    categoria = st.selectbox(
        "Categoria",
        ["Todas", "Eletrônicos", "Moda", "Casa", "Beleza", "Esportes", "Brinquedos"],
    )

with col3:
    desconto_min = st.slider(
        "Desconto mínimo (%)",
        min_value=30,
        max_value=95,
        value=60,
        step=1,
        format="%d%%",
    )

with col4:
    ordenar = st.selectbox("Ordenar por", ["Mais recentes", "Maior desconto", "Menor preço"])

st.divider()

# --- DADOS SIMULADOS ---
produtos_bugs = [
    {"produto": "Fone Lenovo LP40", "cat": "Eletrônicos", "plat": "Shopee",
     "original": 89.90, "bug": 12.90, "comissao": 12, "vendas_h": 340, "img": "🎧"},
    {"produto": "Tênis Nike Revolution 6", "cat": "Esportes", "plat": "Mercado Livre",
     "original": 349.90, "bug": 89.90, "comissao": 8, "vendas_h": 128, "img": "👟"},
    {"produto": "Camiseta Dry Fit Kit 3", "cat": "Moda", "plat": "TikTok Shop",
     "original": 129.90, "bug": 19.90, "comissao": 15, "vendas_h": 567, "img": "👕"},
    {"produto": "Smartwatch D20 Pro", "cat": "Eletrônicos", "plat": "Kwai Shop",
     "original": 199.90, "bug": 29.90, "comissao": 10, "vendas_h": 231, "img": "⌚"},
    {"produto": "Aspirador Robô Xiaomi", "cat": "Casa", "plat": "Amazon",
     "original": 1299.90, "bug": 399.90, "comissao": 7, "vendas_h": 89, "img": "🤖"},
    {"produto": "Paleta de Sombras Ruby Rose", "cat": "Beleza", "plat": "Shopee",
     "original": 49.90, "bug": 6.90, "comissao": 18, "vendas_h": 890, "img": "💄"},
    {"produto": "Mochila Impermeável 40L", "cat": "Esportes", "plat": "Mercado Livre",
     "original": 189.90, "bug": 39.90, "comissao": 9, "vendas_h": 145, "img": "🎒"},
    {"produto": "Ring Light 10 Polegadas", "cat": "Eletrônicos", "plat": "TikTok Shop",
     "original": 99.90, "bug": 22.90, "comissao": 14, "vendas_h": 312, "img": "💡"},
    {"produto": "Fritadeira Air Fryer 4L", "cat": "Casa", "plat": "Magalu",
     "original": 399.90, "bug": 149.90, "comissao": 6, "vendas_h": 203, "img": "🍟"},
    {"produto": "Óculos de Sol Polarizado", "cat": "Moda", "plat": "Shopee",
     "original": 79.90, "bug": 9.90, "comissao": 20, "vendas_h": 1023, "img": "🕶️"},
]

# --- APLICAR FILTROS ---
filtered = produtos_bugs

if plataforma:
    filtered = [p for p in filtered if p["plat"] in plataforma]

if categoria != "Todas":
    filtered = [p for p in filtered if p["cat"] == categoria]

filtered = [
    p for p in filtered
    if ((p["original"] - p["bug"]) / p["original"] * 100) >= desconto_min
]

if ordenar == "Maior desconto":
    filtered.sort(key=lambda x: (x["original"] - x["bug"]) / x["original"], reverse=True)
elif ordenar == "Menor preço":
    filtered.sort(key=lambda x: x["bug"])

# --- EXIBIR PRODUTOS ---
st.markdown(f"**{len(filtered)} produtos encontrados**")
st.text("")

if not filtered:
    st.warning("Nenhum produto encontrado com esses filtros. Tente reduzir o desconto mínimo.")
else:
    for i in range(0, len(filtered), 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            if i + j < len(filtered):
                p = filtered[i + j]
                desconto = round((p["original"] - p["bug"]) / p["original"] * 100)
                comissao_valor = round(p["bug"] * p["comissao"] / 100, 2)
                minutos = random.randint(1, 45)

                with col:
                    with st.container(border=True):
                        st.markdown(f"### {p['img']} {p['produto']}")
                        st.caption(f"📍 {p['plat']} · ⏱️ {minutos} min atrás · 🛒 {p['vendas_h']} vendas/hora")

                        m1, m2, m3 = st.columns(3)
                        with m1:
                            st.metric("Preço Original", f"R$ {p['original']:.2f}")
                        with m2:
                            st.metric("Preço Bug", f"R$ {p['bug']:.2f}", delta=f"-{desconto}%")
                        with m3:
                            st.metric("Sua Comissão", f"R$ {comissao_valor:.2f}", delta=f"{p['comissao']}%")

                        bc1, bc2, bc3 = st.columns(3)
                        with bc1:
                            st.button("🔗 Gerar Link", key=f"link_{i+j}")
                        with bc2:
                            st.button("🎬 Criar Vídeo", key=f"video_{i+j}")
                        with bc3:
                            st.button("📋 Copiar Info", key=f"copy_{i+j}")

st.divider()

# --- SEÇÃO DE ALERTA PERSONALIZADO ---
st.subheader("🔔 Criar Alerta de Preço Bugado")

with st.form("alerta_form"):
    ac1, ac2 = st.columns(2)

    with ac1:
        alerta_produto = st.text_input(
            "Produto ou palavra-chave",
            placeholder="Ex: iPhone, Air Fryer, Tênis...",
        )
        alerta_plat = st.multiselect(
            "Plataformas",
            ["Shopee", "Mercado Livre", "TikTok Shop", "Kwai Shop", "Amazon", "Magalu"],
            default=["Shopee"],
        )

    with ac2:
        alerta_desconto = st.slider(
            "Desconto mínimo pra alertar (%)",
            min_value=30,
            max_value=95,
            value=70,
            step=1,
            format="%d%%",
        )
        alerta_preco_max = st.number_input(
            "Preço máximo (R$)",
            min_value=0.0,
            value=100.0,
            step=10.0,
        )

    submitted = st.form_submit_button("✅ Criar Alerta", use_container_width=True)

    if submitted:
        if alerta_produto:
            st.success(
                f"Alerta criado! Você será notificado quando '{alerta_produto}' tiver desconto de "
                f"{alerta_desconto}%+ nas plataformas selecionadas."
            )
        else:
            st.error("Digite o nome do produto ou palavra-chave.")

# --- SIDEBAR STATS ---
with st.sidebar:
    st.markdown("### 📊 Estatísticas do Radar")
    st.metric("Produtos monitorados", "12.847")
    st.metric("Bugs encontrados hoje", "23")
    st.metric("Bugs na última hora", "4")
    st.divider()
    st.markdown("### ⏰ Horários com mais bugs")
    st.caption("🔴 10h–12h → Shopee atualiza preços")
    st.caption("🔴 14h–16h → Mercado Livre muda ofertas")
    st.caption("🔴 20h–22h → TikTok Shop promos noturnas")
    st.divider()
    if st.button("🔄 Atualizar Radar", use_container_width=True):
        st.rerun()
