import re
import unicodedata
from typing import List, Optional, Sequence, Tuple

STOP_WORDS = {
    "a", "al", "ante", "bajo", "con", "de", "del", "des", "en", "es", "esta",
    "este", "la", "las", "los", "para", "por", "que", "y", "un", "una", "unos",
    "unas", "se", "su", "sus", "el", "lo", "los", "como", "desde", "hacia", "o",
    "si", "sin", "sobre", "entre", "dentro", "fuera", "muy", "mas", "más"
}


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
        score += 0.15 * min(len(shared_tokens), 4)

    location_tokens = [token for token in query_tokens if token in normalize_text(attraction.location).split()]
    if location_tokens:
        score += 0.2

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
