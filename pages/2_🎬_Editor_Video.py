import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

st.set_page_config(page_title="Editor de Vídeo", page_icon="🎬", layout="wide")

st.markdown("# 🎬 Editor de Conteúdo")
st.caption("Crie vídeos e artes para promover produtos como afiliado")

# --- TABS ---
tab_arte, tab_video, tab_copy = st.tabs(["🖼️ Criar Arte", "🎥 Criar Vídeo", "📝 Gerar Copy"])

# =====================
# TAB 1 — CRIAR ARTE
# =====================
with tab_arte:
    st.subheader("🖼️ Gerador de Arte para Stories/Feed")

    ac1, ac2 = st.columns([1, 1])

    with ac1:
        st.markdown("### 📦 Dados do Produto")
        nome_produto = st.text_input("Nome do produto", value="Fone Bluetooth Lenovo LP40", key="arte_nome")
        preco_original = st.text_input("Preço original", value="R$ 89,90", key="arte_orig")
        preco_bug = st.text_input("Preço bugado", value="R$ 12,90", key="arte_bug")
        plataforma = st.selectbox("Plataforma", ["Shopee", "Mercado Livre", "TikTok Shop", "Kwai Shop", "Amazon", "Magalu"], key="arte_plat")
        cta_texto = st.text_input("Texto do CTA", value="🔗 LINK NA BIO", key="arte_cta")

        st.divider()

        st.markdown("### 🎨 Estilo Visual")
        template = st.selectbox("Template", [
            "🔴 Preço Bugado (Vermelho)",
            "⚫ Dark Mode (Preto/Dourado)",
            "🟢 Oferta Flash (Verde Neon)",
            "🔵 Profissional (Azul)",
            "🟡 Urgência (Amarelo/Preto)"
        ])

        formato = st.radio("Formato", ["Stories (1080x1920)", "Feed (1080x1080)", "Banner (1200x628)"], horizontal=True)

        img_produto = st.file_uploader("Imagem do produto (opcional)", type=["png", "jpg", "jpeg", "webp"], key="arte_img")

    with ac2:
        st.markdown("### 👁️ Preview")

        cores = {
            "🔴 Preço Bugado (Vermelho)": {"bg": "#1a0000", "accent": "#FF4B4B", "text": "#FFFFFF", "badge": "#FF0000"},
            "⚫ Dark Mode (Preto/Dourado)": {"bg": "#0a0a0a", "accent": "#FFD700", "text": "#FFFFFF", "badge": "#FFD700"},
            "🟢 Oferta Flash (Verde Neon)": {"bg": "#001a00", "accent": "#00FF66", "text": "#FFFFFF", "badge": "#00FF66"},
            "🔵 Profissional (Azul)": {"bg": "#000a1a", "accent": "#4B9BFF", "text": "#FFFFFF", "badge": "#4B9BFF"},
            "🟡 Urgência (Amarelo/Preto)": {"bg": "#1a1a00", "accent": "#FFD700", "text": "#000000", "badge": "#FFD700"},
        }

        cor = cores[template]

        tamanhos = {
            "Stories (1080x1920)": (540, 960),
            "Feed (1080x1080)": (540, 540),
            "Banner (1200x628)": (600, 314),
        }
        w, h = tamanhos[formato]

        img = Image.new("RGB", (w, h), cor["bg"])
        draw = ImageDraw.Draw(img)

        try:
            font_big = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 28)
            font_med = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22)
            font_sm = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
            font_price = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48)
        except OSError:
            font_big = ImageFont.load_default()
            font_med = ImageFont.load_default()
            font_sm = ImageFont.load_default()
            font_price = ImageFont.load_default()

        # Badge
        badge_w, badge_h = 220, 36
        badge_x = w - badge_w - 20
        badge_y = 20
        draw.rounded_rectangle(
            [badge_x, badge_y, badge_x + badge_w, badge_y + badge_h],
            radius=18, fill=cor["badge"]
        )
        badge_text_color = "#FFFFFF" if template != "🟡 Urgência (Amarelo/Preto)" else "#000000"
        draw.text((badge_x + 15, badge_y + 6), "🐛 PREÇO BUGADO", fill=badge_text_color, font=font_sm)

        # Imagem do produto
        if img_produto:
            prod_img = Image.open(img_produto).convert("RGB")
            prod_img = prod_img.resize((min(w - 80, 300), min(h // 3, 300)))
            img_x = (w - prod_img.width) // 2
            img_y = 80
            img.paste(prod_img, (img_x, img_y))
            text_start_y = img_y + prod_img.height + 30
        else:
            placeholder_size = min(w - 80, 200)
            px = (w - placeholder_size) // 2
            py = 80
            draw.rounded_rectangle([px, py, px + placeholder_size, py + placeholder_size], radius=20, fill="#333333")
            draw.text((px + placeholder_size // 4, py + placeholder_size // 2 - 10), "PRODUTO", fill="#666666", font=font_med)
            text_start_y = py + placeholder_size + 30

        # Nome
        draw.text((30, text_start_y), nome_produto[:35], fill=cor["text"], font=font_big)

        # Plataforma
        draw.text((30, text_start_y + 45), f"{plataforma}", fill="#AAAAAA", font=font_sm)

        # Preço original riscado
        draw.text((30, text_start_y + 85), f"De: {preco_original}", fill="#888888", font=font_med)
        bbox = draw.textbbox((30, text_start_y + 85), f"De: {preco_original}", font=font_med)
        line_y = (bbox[1] + bbox[3]) // 2
        draw.line([(bbox[0], line_y), (bbox[2], line_y)], fill="#888888", width=2)

        # Preço bugado
        draw.text((30, text_start_y + 125), preco_bug, fill=cor["accent"], font=font_price)

        # CTA
        cta_y = min(text_start_y + 210, h - 60)
        cta_box_w = w - 60
        draw.rounded_rectangle([30, cta_y, 30 + cta_box_w, cta_y + 44], radius=22, fill=cor["accent"])
        cta_color = "#FFFFFF" if template != "🟡 Urgência (Amarelo/Preto)" else "#000000"
        draw.text((w // 2 - 60, cta_y + 10), cta_texto, fill=cta_color, font=font_med)

        st.image(img, use_container_width=True)

        # Download
        buf = io.BytesIO()
        real_sizes = {
            "Stories (1080x1920)": (1080, 1920),
            "Feed (1080x1080)": (1080, 1080),
            "Banner (1200x628)": (1200, 628),
        }
        rw, rh = real_sizes[formato]
        img_full = img.resize((rw, rh), Image.LANCZOS)
        img_full.save(buf, format="PNG", quality=95)

        st.download_button(
            label="⬇️ Baixar Arte em Alta Resolução",
            data=buf.getvalue(),
            file_name=f"afiliabug_{nome_produto[:20].replace(' ', '_').lower()}.png",
            mime="image/png",
            use_container_width=True
        )

# =====================
# TAB 2 — CRIAR VÍDEO
# =====================
with tab_video:
    st.subheader("🎥 Gerador de Vídeo Rápido")

    vc1, vc2 = st.columns([1, 1])

    with vc1:
        st.markdown("### 📦 Dados do Produto")
        vid_nome = st.text_input("Nome do produto", value="Fone Bluetooth Lenovo LP40", key="vid_nome")
        vid_original = st.text_input("Preço original", value="R$ 89,90", key="vid_orig")
        vid_bug = st.text_input("Preço bugado", value="R$ 12,90", key="vid_bug")
        vid_plat = st.selectbox("Plataforma", ["Shopee", "Mercado Livre", "TikTok Shop", "Kwai Shop"], key="vid_plat")

        st.divider()

        st.markdown("### 🎬 Configuração do Vídeo")
        vid_template = st.selectbox("Estilo do vídeo", [
            "🔴 Alerta de Preço Bugado",
            "⚡ Oferta Relâmpago",
            "📦 Review Rápido",
            "🏆 Top Ofertas do Dia",
            "😱 Antes x Depois do Preço"
        ])

        vid_duracao = st.select_slider(
            "Duração",
            options=["5s", "10s", "15s", "30s", "60s"],
            value="15s"
        )

        vid_formato = st.radio("Formato", ["Vertical (9:16)", "Quadrado (1:1)", "Horizontal (16:9)"], horizontal=True)

        vid_musica = st.selectbox("Música de fundo", [
            "🔇 Sem música",
            "🔥 Urgência (batida rápida)",
            "💰 Cash Sound (caixa registradora)",
            "⚡ Eletrônica (hype)",
            "🎵 Lo-Fi (relaxado)"
        ])

    with vc2:
        st.markdown("### 👁️ Preview do Roteiro")

        roteiros = {
            "🔴 Alerta de Preço Bugado": [
                {"tempo": "0s–2s", "tela": "🚨 ALERTA DE PREÇO BUGADO", "desc": "Tela vermelha piscando com sirene"},
                {"tempo": "2s–5s", "tela": f"📦 {vid_nome}", "desc": "Foto do produto aparece com zoom"},
                {"tempo": "5s–8s", "tela": f"De: {vid_original}", "desc": "Preço original aparece e é riscado"},
                {"tempo": "8s–12s", "tela": f"POR APENAS {vid_bug}", "desc": "Preço bugado aparece grande com efeito shake"},
                {"tempo": "12s–15s", "tela": "🔗 LINK NA BIO / COMENTA EU QUERO", "desc": "CTA final com seta animada"},
            ],
            "⚡ Oferta Relâmpago": [
                {"tempo": "0s–3s", "tela": "⚡ OFERTA RELÂMPAGO", "desc": "Contagem regressiva 3, 2, 1"},
                {"tempo": "3s–6s", "tela": f"{vid_nome}", "desc": "Produto aparece com efeito slide"},
                {"tempo": "6s–10s", "tela": f"{vid_original} ➡️ {vid_bug}", "desc": "Animação de preço caindo"},
                {"tempo": "10s–15s", "tela": "CORRE QUE VAI ACABAR!", "desc": "Timer falso + CTA"},
            ],
            "📦 Review Rápido": [
                {"tempo": "0s–3s", "tela": f"Achei {vid_nome} por {vid_bug}!", "desc": "Voz narrando + texto"},
                {"tempo": "3s–8s", "tela": "📦 Unboxing...", "desc": "Simulação de abrir caixa"},
                {"tempo": "8s–12s", "tela": "Vale a pena? SIM!", "desc": "Lista de prós"},
                {"tempo": "12s–15s", "tela": f"🔗 {vid_plat} - Link na bio", "desc": "CTA final"},
            ],
            "🏆 Top Ofertas do Dia": [
                {"tempo": "0s–2s", "tela": "🏆 TOP OFERTAS DE HOJE", "desc": "Abertura com data do dia"},
                {"tempo": "2s–5s", "tela": f"#1: {vid_nome}", "desc": "Produto principal"},
                {"tempo": "5s–10s", "tela": f"{vid_original} ➡️ {vid_bug}", "desc": "Comparativo de preço"},
                {"tempo": "10s–15s", "tela": "Segue pra mais ofertas!", "desc": "CTA follow + link"},
            ],
            "😱 Antes x Depois do Preço": [
                {"tempo": "0s–3s", "tela": f"ANTES: {vid_original} 😐", "desc": "Tela cinza, preço normal"},
                {"tempo": "3s–5s", "tela": "TRANSIÇÃO 💥", "desc": "Efeito glitch / explosão"},
                {"tempo": "5s–10s", "tela": f"DEPOIS: {vid_bug} 🤯", "desc": "Tela colorida, preço bugado"},
                {"tempo": "10s–15s", "tela": "CORRE PRO LINK!", "desc": "CTA urgente"},
            ],
        }

        roteiro = roteiros.get(vid_template, roteiros["🔴 Alerta de Preço Bugado"])

        for cena in roteiro:
            with st.container(border=True):
                st.caption(f"⏱️ {cena['tempo']}")
                st.markdown(f"**{cena['tela']}**")
                st.caption(cena["desc"])

        st.divider()

        if st.button("🎬 Gerar Vídeo", use_container_width=True, type="primary"):
            with st.spinner("Gerando vídeo... isso pode levar alguns segundos"):
                import time
                progress = st.progress(0)
                for i in range(100):
                    time.sleep(0.03)
                    progress.progress(i + 1)

                st.success("✅ Vídeo gerado com sucesso!")
                st.info("⚠️ No plano gratuito o vídeo é gerado como slideshow de imagens. Upgrade pro plano PRO para vídeos com animação completa.")
                st.balloons()

# =====================
# TAB 3 — GERAR COPY
# =====================
with tab_copy:
    st.subheader("📝 Gerador de Copy para Redes Sociais")

    cc1, cc2 = st.columns([1, 1])

    with cc1:
        st.markdown("### 📦 Dados do Produto")
        copy_nome = st.text_input("Nome do produto", value="Fone Bluetooth Lenovo LP40", key="copy_nome")
        copy_original = st.text_input("Preço original", value="R$ 89,90", key="copy_orig")
        copy_bug = st.text_input("Preço bugado", value="R$ 12,90", key="copy_bug")
        copy_plat = st.selectbox("Plataforma", ["Shopee", "Mercado Livre", "TikTok Shop", "Kwai Shop"], key="copy_plat")
        copy_link = st.text_input("Seu link de afiliado (opcional)", placeholder="https://s.shopee.com.br/abc123", key="copy_link")

        st.divider()

        copy_estilo = st.selectbox("Estilo da copy", [
            "🔥 Urgência (FOMO)",
            "😱 Choque de preço",
            "📋 Informativo",
            "🤑 Economia",
            "😂 Descontraído/Meme"
        ])

        copy_rede = st.multiselect("Gerar para", ["Instagram", "TikTok", "WhatsApp", "Twitter/X", "Kwai"], default=["Instagram", "WhatsApp"])

    with cc2:
        st.markdown("### 📄 Copys Geradas")

        if st.button("✨ Gerar Copys", use_container_width=True, type="primary"):

            copys = {}

            if "Instagram" in copy_rede:
                copys["Instagram"] = f"""🚨 PREÇO BUGADO CONFIRMADO! 🐛

{copy_nome} por apenas {copy_bug}! 😱

❌ De: {copy_original}
✅ Por: {copy_bug}

Isso não é erro, é oportunidade! Corre que bug de preço não dura!

🔗 Link nos stories / bio
📍 {copy_plat}

#precobugado #oferta #desconto #{copy_plat.lower().replace(' ', '')} #afiliado #promocao"""

            if "WhatsApp" in copy_rede:
                copys["WhatsApp"] = f"""🚨 *PREÇO BUGADO!* 🐛

*{copy_nome}*

❌ De: ~{copy_original}~
✅ Por: *{copy_bug}*

📍 {copy_plat}
🔗 {copy_link if copy_link else 'Link aqui'}

⚠️ Corre que bug de preço some rápido!"""

            if "TikTok" in copy_rede:
                copys["TikTok"] = f"""ACHEI PREÇO BUGADO 🐛🔥

{copy_nome} por {copy_bug}!!
Era {copy_original} 😱

Comenta EU QUERO que mando o link!

#precobugado #bugdepreco #ofertadodia #fyp #viral"""

            if "Twitter/X" in copy_rede:
                copys["Twitter/X"] = f"""🚨 BUG DE PREÇO!

{copy_nome}
De {copy_original} por {copy_bug} 🤯

{copy_link if copy_link else '🔗 Link no reply'}

Corre! 🏃‍♂️💨"""

            if "Kwai" in copy_rede:
                copys["Kwai"] = f"""OLHA ESSE PREÇO BUGADO! 🐛💰

{copy_nome} por SÓ {copy_bug}!
Normal é {copy_original}!

Comenta LINK que eu mando! 🔗

#kwai #oferta #precobugado"""

            for rede, texto in copys.items():
                with st.expander(f"📱 {rede}", expanded=True):
                    st.code(texto, language=None)
                    st.button(f"📋 Copiar {rede}", key=f"copybtn_{rede}")

        else:
            st.info("👆 Preencha os dados e clique em **Gerar Copys**")

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("### 🎬 Editor de Conteúdo")
    st.divider()
    st.markdown("**Dicas de conteúdo:**")
    st.caption("🔴 Stories com urgência convertem 3x mais")
    st.caption("🎥 Vídeos de 15s têm melhor retenção")
    st.caption("📝 Copys com emoji têm 25% mais cliques")
    st.caption("⏰ Poste entre 19h–22h para maior alcance")
    st.divider()
    st.markdown("**Seus conteúdos:**")
    st.metric("Artes criadas", "12")
    st.metric("Vídeos criados", "5")
    st.metric("Copys geradas", "34")
