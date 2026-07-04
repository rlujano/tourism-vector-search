import re
import unicodedata
from typing import Iterable, List, Optional, Sequence, Tuple

STOP_WORDS = {
    "a", "al", "ante", "bajo", "con", "de", "del", "des", "en", "es", "esta",
    "este", "la", "las", "los", "para", "por", "que", "y", "un", "una", "unos",
    "unas", "se", "su", "sus", "el", "lo", "los", "como", "desde", "hacia", "o",
    "si", "sin", "sobre", "entre", "dentro", "fuera", "muy", "mas", "más"
}

ARCHAEOLOGY_TERMS = (
    "arqueolog",
    "prehistor",
    "piramid",
    "templo",
    "ruina",
    "ciudadela",
    "fortaleza",
    "ceremonial",
    "sito",
    "sitio",
    "monolito",
    "civiliz",
    "tumba",
    "sarc",
    "inca",
    "chimu",
    "moche",
    "chachapoya",
    "nazca",
    "caral",
    "huaca",
    "sacsa",
    "ollantaytambo",
    "pisac",
)


def normalize_text(text: str) -> str:
    text = unicodedata.normalize("NFKD", str(text or "").lower())
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return text.strip()


def tokenize(text: str) -> List[str]:
    tokens = []
    for token in normalize_text(text).split():
        if not token or token in STOP_WORDS:
            continue
        token = re.sub(r"(s|es)$", "", token)
        if token and len(token) > 2:
            tokens.append(token)
    return tokens


def keyword_score(query_text: str, attraction) -> float:
    query_tokens = set(tokenize(query_text))
    if not query_tokens:
        return 0.0

    text_parts = [
        attraction.name,
        attraction.description,
        attraction.location,
        attraction.category,
    ]
    text = " ".join(text_parts)
    normalized_text = normalize_text(text)
    text_tokens = set(tokenize(text))

    score = 0.0

    shared_tokens = query_tokens & text_tokens
    if shared_tokens:
        score += 0.18 * min(len(shared_tokens), 4)

    if any(token.startswith("arqueolog") for token in query_tokens):
        if any(term in normalized_text for term in ARCHAEOLOGY_TERMS):
            score += 0.35
        if any(term in normalized_text for term in ("arqueologico", "arqueologica", "cultura", "ceremonial")):
            score += 0.2
        if "arqueologico" in normalize_text(getattr(attraction, "category", "")):
            score += 0.35

    if any(token in {"peru", "peru"} for token in query_tokens):
        if "peru" in normalized_text:
            score += 0.1

    if any(token in {"lugar", "lugar", "sitio", "sitios"} for token in query_tokens):
        if any(term in normalized_text for term in ("sitio", "lugar", "complejo", "centro", "ciudadela", "reserva", "museo", "monasterio", "isla", "huaca")):
            score += 0.08

    return min(score, 1.0)


def rank_attractions(
    query_text: str,
    attractions: Sequence[object],
    semantic_scores: Optional[Sequence[Tuple[int, float]]] = None,
) -> List[Tuple[float, object]]:
    semantic_lookup = {idx: score for idx, score in (semantic_scores or [])}

    scored = []
    for index, attraction in enumerate(attractions):
        lexical = keyword_score(query_text, attraction)
        semantic = semantic_lookup.get(index, 0.0)
        if semantic > 0:
            semantic = max(0.0, min(1.0, 1.0 - semantic))
        combined = round((lexical * 0.7) + (semantic * 0.3), 4)
        scored.append((combined, attraction))

    scored.sort(key=lambda item: (-item[0], attractions.index(item[1])))
    return scored
