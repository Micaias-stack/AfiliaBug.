import datetime
import random


# --- BANCO SIMULADO EM MEMÓRIA ---

_links_db = []
_conversoes_db = []


def salvar_link(nome, produto, plataforma, canal, url_original, url_rastreavel, tags=None):
    """Salva um novo link de afiliado no banco simulado."""

    link = {
        "id": random.randint(10000, 99999),
        "nome": nome,
        "produto": produto,
        "plataforma": plataforma,
        "canal": canal,
        "url_original": url_original,
        "url_rastreavel": url_rastreavel,
        "tags": tags or [],
        "cliques": 0,
        "conversoes": 0,
        "comissao_total": 0.0,
        "status": "ativo",
        "criado_em": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    _links_db.append(link)
    return link


def listar_links(plataforma=None, canal=None, status=None):
    """Retorna links filtrados."""

    resultado = _links_db

    if plataforma:
        resultado = [l for l in resultado if l["plataforma"] == plataforma]
    if canal:
        resultado = [l for l in resultado if l["canal"] == canal]
    if status:
        resultado = [l for l in resultado if l["status"] == status]

    return resultado


def registrar_clique(link_id):
    """Incrementa clique de um link."""

    for link in _links_db:
        if link["id"] == link_id:
            link["cliques"] += 1
            return True
    return False


def registrar_conversao(link_id, valor_comissao):
    """Registra conversão e comissão em um link."""

    for link in _links_db:
        if link["id"] == link_id:
            link["conversoes"] += 1
            link["comissao_total"] += valor_comissao

            _conversoes_db.append({
                "link_id": link_id,
                "valor": valor_comissao,
                "data": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            })
            return True
    return False


def obter_estatisticas():
    """Retorna resumo geral das métricas."""

    total_links = len(_links_db)
    total_cliques = sum(l["cliques"] for l in _links_db)
    total_conversoes = sum(l["conversoes"] for l in _links_db)
    total_comissao = sum(l["comissao_total"] for l in _links_db)
    taxa = round(total_conversoes / total_cliques * 100, 1) if total_cliques > 0 else 0

    return {
        "total_links": total_links,
        "total_cliques": total_cliques,
        "total_conversoes": total_conversoes,
        "total_comissao": round(total_comissao, 2),
        "taxa_conversao": taxa,
    }


def pausar_link(link_id):
    """Pausa um link ativo."""

    for link in _links_db:
        if link["id"] == link_id:
            link["status"] = "pausado"
            return True
    return False


def reativar_link(link_id):
    """Reativa um link pausado/expirado."""

    for link in _links_db:
        if link["id"] == link_id:
            link["status"] = "ativo"
            return True
    return False
