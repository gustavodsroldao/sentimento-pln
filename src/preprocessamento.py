import re

# A palavra "não" fica de fora de propósito: "não gostei" e "gostei"
# têm sentidos opostos, então remover o "não" inverte a opinião.
# Pelo mesmo motivo "nunca", "nem" e "sem" também ficam.
STOP = {
    "o", "a", "os", "as", "um", "uma", "uns", "umas",
    "e", "é", "de", "do", "da", "dos", "das", "em", "no", "na",
    "que", "para", "com", "por", "ao", "foi", "ser", "se", "eu", "me",
}

# Reaproveitado da última atividade feita em aula ;)
def prep(texto, remover_stopwords=True):
    # só letras (com acento), então pontuação e números caem fora
    palavras = re.findall(r"[a-záàâãéêíóôõúçü]+", str(texto).lower())

    if remover_stopwords:
        palavras = [p for p in palavras if p not in STOP]

    return " ".join(palavras)
