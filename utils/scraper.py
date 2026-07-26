import random
import datetime


def gerar_produtos_simulados(quantidade=20):
    """Gera lista de produtos simulados com preços bugados."""

    produtos_base = [
        {"nome": "Fone Bluetooth Lenovo LP40", "categoria": "Eletrônicos", "img": "🎧"},
        {"nome": "Tênis Nike Revolution 6", "categoria": "Moda", "img": "👟"},
        {"nome": "Kit 3 Camisetas Dry Fit", "categoria": "Moda", "img": "👕"},
        {"nome": "Smartwatch D20 Pro", "categoria": "Eletrônicos", "img": "⌚"},
        {"nome": "Paleta de Sombras Ruby Rose", "categoria": "Beleza", "img": "💄"},
        {"nome": "Fritadeira Air Fryer 4L", "categoria": "Casa", "img": "🍟"},
        {"nome": "Óculos de Sol Polarizado", "categoria": "Moda", "img": "🕶️"},
        {"nome": "Mochila Impermeável 40L", "categoria": "Esporte", "img": "🎒"},
        {"nome": "Carregador Portátil 10000mAh", "categoria": "Eletrônicos", "img": "🔋"},
        {"nome": "Ring Light 10 Polegadas", "categoria": "Eletrônicos", "img": "💡"},
        {"nome": "Cinto Tático Militar", "categoria": "Moda", "img": "👔"},
        {"nome": "Câmera Wi-Fi 360°", "categoria": "Eletrônicos", "img": "📷"},
        {"nome": "Garrafa Térmica 500ml", "categoria": "Casa", "img": "🧴"},
        {"nome": "Pelúcia Stitch 25cm", "categoria": "Brinquedos", "img": "🧸"},
        {"nome": "Base Líquida Matte HD", "categoria": "Beleza", "img": "💋"},
        {"nome": "Teclado Mecânico RGB", "categoria": "Eletrônicos", "img": "⌨️"},
        {"nome": "Legging Fitness Feminina", "categoria": "Moda", "img": "👖"},
        {"nome": "Organizador de Maquiagem", "categoria": "Beleza", "img": "🗄️"},
        {"nome": "Luminária LED de Mesa", "categoria": "Casa", "img": "🔦"},
        {"nome": "Mini Projetor Portátil", "categoria": "Eletrônicos", "img": "📽️"},
        {"nome": "Bolsa Feminina Transversal", "categoria": "Moda", "img": "👜"},
        {"nome": "Kit Pincéis Maquiagem 12pcs", "categoria": "Beleza", "img": "🖌️"},
        {"nome": "Caixa de Som Bluetooth", "categoria": "Eletrônicos", "img": "🔊"},
        {"nome": "Tapete Antiderrapante Banheiro", "categoria": "Casa", "img": "🛁"},
        {"nome": "Anel Ajustável Prata 925", "categoria": "Moda", "img": "💍"},
    ]

    plataformas = ["Shopee", "Mercado Livre", "TikTok Shop", "Kwai Shop", "Amazon", "Magalu"]

    produtos = []
    selecionados = random.sample(produtos_base, min(quantidade, len(produtos_base)))

    for p in selecionados:
        preco_original = round(random.uniform(29.90, 499.90), 2)
        desconto = random.randint(40, 92)
        preco_bugado = round(preco_original * (1 - desconto / 100), 2)
        comissao_pct = round(random.uniform(3, 20), 1)
        comissao_valor = round(preco_bugado * comissao_pct / 100, 2)
        vendas = random.randint(50, 9999)
        avaliacao = round(random.uniform(3.8, 5.0), 1)
        horas = random.randint(1, 48)
        plataforma = random.choice(plataformas)

        produtos.append({
            "nome": p["nome"],
            "categoria": p["categoria"],
            "emoji": p["img"],
            "plataforma": plataforma,
            "preco_original": preco_original,
            "preco_bugado": preco_bugado,
            "desconto": desconto,
            "comissao_pct": comissao_pct,
            "comissao_valor": comissao_valor,
            "vendas": vendas,
            "avaliacao": avaliacao,
            "tempo_restante": f"{horas}h",
            "link": f"https://afiliabug.link/{random.randint(10000, 99999)}",
            "encontrado_em": (datetime.datetime.now() - datetime.timedelta(hours=horas)).strftime("%d/%m %H:%M"),
        })

    return produtos


def buscar_produto_por_url(url: str):
    """Simula busca de produto a partir de URL colada."""

    if not url or not url.startswith("http"):
        return None

    return {
        "nome": "Produto Encontrado via URL",
        "preco_original": round(random.uniform(49.90, 399.90), 2),
        "preco_atual": round(random.uniform(9.90, 99.90), 2),
        "plataforma": random.choice(["Shopee", "Mercado Livre", "TikTok Shop"]),
        "disponivel": True,
    }
