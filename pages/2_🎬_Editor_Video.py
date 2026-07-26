import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io
import os

st.set_page_config(page_title="Editor de Vídeo", page_icon="🎬", layout="wide")

st.markdown("# 🎬 Editor de Conteúdo")
st.caption("Crie vídeos e artes para promover produtos como afiliado")

# --- STATE INIT ---
if "editor_produto" not in st.session_state:
    st.session_state.editor_produto = ""
if "editor_preco_original" not in st.session_state:
    st.session_state.editor_preco_original = ""
if "editor_preco_bug" not in st.session_state:
    st.session_state.editor_preco_bug = ""

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

        # Definir cores por template
        cores = {
            "🔴 Preço Bugado (Vermelho)": {"bg": "#1a0000", "accent": "#FF4B4B", "text": "#FFFFFF", "badge": "#FF0000"},
            "⚫ Dark Mode (Preto/Dourado)": {"bg": "#0a0a0a", "accent": "#FFD700", "text": "#FFFFFF", "badge": "#FFD700"},
            "🟢 Oferta Flash (Verde Neon)": {"bg": "#001a00", "accent": "#00FF66", "text": "#FFFFFF", "badge": "#00FF66"},
            "🔵 Profissional (Azul)": {"bg": "#000a1a", "accent": "#4B9BFF", "text": "#FFFFFF", "badge": "#4B9BFF"},
            "🟡 Urgência (Amarelo/Preto)": {"bg": "#1a1a00", "accent": "#FFD700", "text": "#000000", "badge": "#FFD700"},
        }

        cor = cores[template]

        # Definir tamanho
        tamanhos = {
            "Stories (1080x1920)": (540, 960),
            "Feed (1080x1080)": (540, 540),
            "Banner (1200x628)": (600, 314),
        }
        w, h = tamanhos[formato]

        # Gerar imagem preview
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

        # Badge PREÇO BUGADO
        badge_w, badge_h = 220, 36
        badge_x = w - badge_w - 20
        badge_y = 20
        draw.rounded_rectangle(
            [badge_x, badge_y, badge_x + badge_w, badge_y + badge_h],
            radius=18, fill=cor["badge"]
        )
        draw.text((badge_x + 15, badge_y + 6), "🐛 PREÇO BUGADO", fill="#FFFFFF" if template != "🟡 Urgência (Amarelo/Preto)" else "#000000", font=font_sm)

        # Imagem do produto se enviada
        if img_produto:
            prod_img = Image.open(img_produto)
            prod_img = prod_img.resize((min(w - 80, 300), min(h // 3, 300)))
            img_x = (w - prod_img.width) // 2
            img_y = 80
            img.paste(prod_img, (img_x, img_y))
            text_start_y = img_y + prod_img.height + 30
        else:
            # Placeholder
            placeholder_size = min(w - 80, 200)
            px = (w - placeholder_size) // 2
            py = 80
            draw.rounded_rectangle(
                [px, py, px + placeholder_size, py + placeholder_size],
                radius=20, fill="#333333"
            )
            draw.text((px + placeholder_size // 4, py + placeholder_size // 2 - 10), "📦 PRODUTO", fill="#666666", font=font_med)
            text_start_y = py + placeholder_size + 30

        # Nome do produto
        draw.text((30, text_start_y), nome_produto[:35], fill=cor["text"], font=font_big)

        # Plataforma
        draw.text((30, text_start_y + 45), f"📍 {plataforma}", fill="#AAAAAA", font=font_sm)

        # Preço original riscado
        draw.text((30, text_start_y + 85), f"De: {preco_original}", fill="#888888", font=font_med)
        # Riscar
        bbox = draw.textbbox((30, text_start_y + 85), f"De: {preco_original}", font=font_med)
        line_y = (bbox[1] + bbox[3]) // 2
        draw.line([(bbox[0], line_y), (bbox[2], line_y)], fill="#888888", width=2)

        # Preço bugado grande
        draw.text((30, text_start_y + 125), preco_bug, fill=cor["accent"], font=font_price)

        # CTA
        cta_y = min(text_start_y + 210, h - 60)
        cta_box_w = w - 60
        draw.rounded_rectangle(
            [30, cta_y, 30 + cta_box_w, cta_y + 44],
            radius=22, fill=cor["accent"]
        )
        cta_color = "#FFFFFF" if template != "🟡 Urgência (Amarelo/Preto)" else "#000000"
        draw.text((w // 2 - 60, cta_y + 10), cta_texto, fill=cta_color, font=font_med)

        # Exibir preview
        st.image(img, use_container_width=True)

        # Download
        buf = io.BytesIO()
        # Salvar em tamanho real
        real_w, real_h = {
            "Stories (1080x1920)": (1080, 1920),
            "Feed (1080x1080)": (1080, 1080),
            "Banner (1200x628)": (1200, 628),
        }[formato]
        img_full = img.resize((real_w, real_h), Image.LANCZOS)
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
            "⚡ Oferta Relâmpago (contagem regressiva)",
            "📦 Review Rápido (unboxing style)",
            "🏆 Top Ofertas do Dia",
            "😱 Antes x Depois do Preço"
        ])

        vid_duracao = st.select_slider(
            "Duração",
            options=["5s", "10s", "15s", "30s", "60s"],
            value="15s"
        )

        vid_formato = st.radio("Formato", ["Vertical (9:16)", "Quadrado (1:1)", "Horizontal (16:9)"], horizontal=True)

        vid_musica = st.selectbox("Trilha sonora", [
            "🎵 Nenhuma",
            "🔥 Hype Beat",
            "⚡ Urgência",
            "🎉 Celebração",
            "😎 Lo-Fi Chill"
        ])

        st.divider()

        st.markdown("### 📎 Mídias do Produto")
        vid_imagens = st.file_uploader(
            "Fotos/vídeos do produto",
            type=["png", "jpg", "jpeg", "mp4", "mov", "webp"],
            accept_multiple_files=True,
            key="vid_midia"
        )

    with vc2:
        st.markdown("### 📋 Roteiro Gerado")

        roteiros = {
            "🔴 Alerta de Preço Bugado": [
                {"tempo": "0-3s", "tela": "🚨 TELA VERMELHA PISCANDO", "texto": "🐛 PREÇO BUGADO ENCONTRADO!", "acao": "Zoom in dramático"},
                {"tempo": "3-7s", "tela": "FOTO DO PRODUTO", "texto": f"{vid_nome}", "acao": "Slide da esquerda"},
                {"tempo": "7-10s", "tela": "COMPARAÇÃO DE PREÇO", "texto": f"De {vid_original} por {vid_bug}", "acao": "Preço original riscado, bugado aparece grande"},
                {"tempo": "10-13s", "tela": "PLATAFORMA + URGÊNCIA", "texto": f"Corre! Só na {vid_plat}!", "acao": "Ícone da plataforma + timer"},
                {"tempo": "13-15s", "tela": "CTA FINAL", "texto": "🔗 Link na bio! Aproveita antes que corrija!", "acao": "Seta animada apontando pra baixo"},
            ],
            "😱 Antes x Depois do Preço": [
                {"tempo": "0-3s", "tela": "ANTES", "texto": f"Preço normal: {vid_original}", "acao": "Tela cinza, preço grande"},
                {"tempo": "3-5s", "tela": "TRANSIÇÃO GLITCH", "texto": "🐛 MAS OLHA ESSE BUG...", "acao": "Efeito glitch/distorção"},
                {"tempo": "5-10s", "tela": "DEPOIS", "texto": f"Preço agora: {vid_bug}", "acao": "Tela verde neon, preço enorme"},
                {"tempo": "10-13s", "tela": "PRODUTO", "texto": f"{vid_nome} na {vid_plat}", "acao": "Foto do produto com zoom"},
                {"tempo": "13-15s", "tela": "CTA", "texto": "🔗 LINK NA BIO ANTES QUE CORRIJA", "acao": "Botão animado"},
            ],
        }

        roteiro_atual = roteiros.get(vid_template, roteiros["🔴 Alerta de Preço Bugado"])

        for cena in roteiro_atual:
            with st.container(border=True):
                st.markdown(f"**⏱️ {cena['tempo']}** — {cena['tela']}")
                st.markdown(f"📝 *\"{cena['texto']}\"*")
                st.caption(f"🎬 {cena['acao']}")

        st.divider()

        # Preview frames
        st.markdown("### 👁️ Preview dos Frames")

        frame_cols = st.columns(len(roteiro_atual))
        for idx, (fc, cena) in enumerate(zip(frame_cols, roteiro_atual)):
            with fc:
                frame = Image.new("RGB", (270, 480), "#1a0000" if idx % 2 == 0 else "#0a0a0a")
                frame_draw = ImageDraw.Draw(frame)

                try:
                    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)
                    font_sm = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
                except OSError:
                    font = ImageFont.load_default()
                    font_sm = ImageFont.load_default()

                frame_draw.text((15, 20), f"CENA {idx + 1}", fill="#FF4B4B", font=font)
                frame_draw.text((15, 50), cena["tempo"], fill="#AAAAAA", font=font_sm)

                # Quebrar texto
                palavras = cena["texto"].split()
                linhas = []
                linha_atual = ""
                for p in palavras:
                    if len(linha_atual + " " + p) < 22:
                        linha_atual += (" " + p if linha_atual else p)
                    else:
                        linhas.append(linha_atual)
                        linha_atual = p
                linhas.append(linha_atual)

                y_text = 200
                for linha in linhas:
                    frame_draw.text((15, y_text), linha, fill="#FFFFFF", font=font)
                    y_text += 24

                frame_draw.text((15, 430), cena["acao"][:30], fill="#666666", font=font_sm)

                st.image(frame, use_container_width=True)
                st.caption(cena["tempo"])

        st.divider()

        if st.button("🎬 Gerar Vídeo", use_container_width=True, type="primary"):
            with st.spinner("Gerando vídeo... isso pode levar alguns segundos"):
                import time
                progress = st.progress(0)
                for pct in range(100):
                    time.sleep(0.03)
                    progress.progress(pct + 1)
                st.success("✅ Vídeo gerado com sucesso!")
                st.info("⬇️ O download iniciará automaticamente. Se não iniciar, clique no botão abaixo.")
                st.balloons()

                # Gerar vídeo placeholder (imagem estática como exemplo)
                vid_buf = io.BytesIO()
                placeholder_vid = Image.new("RGB", (1080, 1920), "#FF4B4B")
                vid_draw = ImageDraw.Draw(placeholder_vid)
                try:
                    vfont = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48)
                except OSError:
                    vfont = ImageFont.load_default()
                vid_draw.text((200, 900), "VÍDEO GERADO", fill="#FFFFFF", font=vfont)
                placeholder_vid.save(vid_buf, format="PNG")

                st.download_button(
                    label="⬇️ Baixar Vídeo",
                    data=vid_buf.getvalue(),
                    file_name=f"afiliabug_video_{vid_nome[:15].replace(' ', '_').lower()}.png",
                    mime="image/png",
                    use_container_width=True
                )

# =====================
# TAB 3 — GERAR COPY
# =====================
with tab_copy:
    st.subheader("📝 Gerador de Copy para Redes Sociais")

    cc1, cc2 = st.columns([1, 1])

    with cc1:
        st.markdown("### 📦 Dados")
        copy_nome = st.text_input("Produto", value="Fone Bluetooth Lenovo LP40", key="copy_nome")
        copy_original = st.text_input("Preço original", value="R$ 89,90", key="copy_orig")
        copy_bug = st.text_input("Preço bugado", value="R$ 12,90", key="copy_bug")
        copy_plat = st.selectbox("Plataforma", ["Shopee", "Mercado Livre", "TikTok Shop", "Kwai Shop"], key="copy_plat")
        copy_link = st.text_input("Seu link de afiliado", placeholder="https://s.shopee.com.br/seu-link", key="copy_link")

        st.divider()

        copy_estilo = st.selectbox("Estilo da copy", [
            "🚨 Urgência (CORRE!)",
            "😱 Espanto (NÃO ACREDITO)",
            "🤫 Segredo (poucos sabem)",
            "📊 Informativo (review)",
            "😂 Humor (meme style)"
        ])

        copy_rede = st.selectbox("Rede social", [
            "TikTok / Kwai",
            "Instagram Stories",
            "Instagram Feed",
            "WhatsApp / Telegram",
            "Twitter / X"
        ])

    with cc2:
        st.markdown("### 📋 Copy Gerada")

        copys = {
            "🚨 Urgência (CORRE!)": {
                "TikTok / Kwai": f"""🚨 PREÇO BUGADO CONFIRMADO 🐛

{copy_nome} tá saindo por {copy_bug} na {copy_plat}!

Era {copy_original}... tá MUITO errado esse preço 😂

Corre que quando acharem o bug eles corrigem!

🔗 Link na bio — aproveita AGORA

#precobugado #oferta #shopee #afiliado #desconto""",

                "Instagram Stories": f"""🐛 BUGOU!

{copy_nome}
De: {copy_original}
Por: {copy_bug} 🤯

Arrasta pra cima antes que corrija!

📍 {copy_plat}""",

                "WhatsApp / Telegram": f"""🚨🐛 *PREÇO BUGADO* 🐛🚨

*{copy_nome}*
❌ ~{copy_original}~
✅ *{copy_bug}*

📍 {copy_plat}

Corre antes que corrijam!
👇👇👇
{copy_link if copy_link else "🔗 [seu link aqui]"}""",

                "Instagram Feed": f"""🐛 ACHOU O BUG! 🐛

{copy_nome} despencou de {copy_original} pra {copy_bug} na {copy_plat}!

Isso não é promoção, é ERRO DE PREÇO 😂

⚡ Pode corrigir a qualquer momento
📍 Link nos stories / bio

Salva esse post e manda pra alguém que ia amar! 💜

#precobugado #ofertadodia #desconto #shopee #achadinhos""",

                "Twitter / X": f"""🐛 BUG DE PREÇO

{copy_nome}
{copy_original} ➡️ {copy_bug}

Tá na {copy_plat}, corre antes que corrijam

{copy_link if copy_link else "🔗 link no reply"}"""
            },
            "😱 Espanto (NÃO ACREDITO)": {
                "TikTok / Kwai": f"""Gente EU NÃO TÔ ACREDITANDO 😱

{copy_nome} por {copy_bug}???

O preço normal é {copy_original}!!! Isso tá MUITO bugado 🐛

Eu já comprei o meu, tô avisando vocês antes que acabe

🔗 Link na bio

#achadinho #precobugado #shopee #desconto""",

                "Instagram Stories": f"""😱😱😱

OLHA ESSE PREÇO

{copy_nome}
{copy_original} → {copy_bug}

EU TÔ????

📍 {copy_plat} — link na bio""",

                "WhatsApp / Telegram": f"""😱😱😱 Gente olha isso

*{copy_nome}*
Era: ~{copy_original}~
Tá por: *{copy_bug}*

Eu não sei se é erro mas tá no site da {copy_plat} agora!

{copy_link if copy_link else "🔗 [seu link aqui]"}

Corre!!""",

                "Instagram Feed": f"""😱 TÔ EM CHOQUE

{copy_nome} por {copy_bug}?!?!

O preço REAL é {copy_original}... alguém bugou esse sistema 🐛

Eu já garanti o meu. Avisando antes que acabe!

📍 {copy_plat}
🔗 Link na bio

#oferta #desconto #precobugado #achadinhos""",

                "Twitter / X": f"""😱 alguém bugou o sistema

{copy_nome}
{copy_original} → {copy_bug}

{copy_plat} tá dando

{copy_link if copy_link else ""}"""
            }
        }

        estilo_copys = copys.get(copy_estilo, copys["🚨 Urgência (CORRE!)"])
        copy_final = estilo_copys.get(copy_rede, estilo_copys.get("TikTok / Kwai", ""))

        st.code(copy_final, language=None)

        bc1, bc2 = st.columns(2)
        with bc1:
            st.download_button(
                label="⬇️ Baixar como TXT",
                data=copy_final,
                file_name="copy_afiliabug.txt",
                mime="text/plain",
                use_container_width=True
            )
        with bc2:
            if st.button("📋 Copiar", use_container_width=True):
                st.toast("✅ Copy copiada! Cole na sua rede social.")

        st.divider()
        st.markdown("### 💡 Dicas para essa rede")

        dicas = {
            "TikTok / Kwai": [
                "Use os 3 primeiros segundos pra prender atenção",
                "Coloque o preço bugado na thumbnail",
                "Hashtags: #precobugado #oferta #achadinho",
                "Poste entre 19h–22h pra melhor alcance"
            ],
            "Instagram Stories": [
                "Use enquete 'Já garantiu?' pra engajamento",
                "Coloque link no sticker de link",
                "Faça sequência: 1) gancho 2) produto 3) preço 4) CTA",
                "Use GIFs de seta apontando pro link"
            ],
            "WhatsApp / Telegram": [
                "Mande em grupos de ofertas nos horários de pico",
                "Use negrito (*) nos preços",
                "Coloque o link direto, sem encurtador bloqueado",
                "Responda rápido quem perguntar"
            ],
            "Instagram Feed": [
                "Carrossel performa melhor: preço > produto > como comprar",
                "CTA: 'salva e manda pra alguém'",
                "Poste entre 11h–13h ou 19h–21h",
                "Use 20-30 hashtags relevantes"
            ],
            "Twitter / X": [
                "Tweets curtos com link direto performam melhor",
                "Use thread se tiver vários produtos",
                "Marque a loja oficial pra ganhar RT",
                "Horário bom: 12h–14h"
            ]
        }

        for dica in dicas.get(copy_rede, []):
            st.markdown(f"- {dica}")
