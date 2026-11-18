import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

from src.preprocessamento import prep


def treinar_config(x_train, y_train, remover_stopwords, vetorizador):
    textos = x_train.apply(prep, remover_stopwords=remover_stopwords)

    modelo = Pipeline([
        ("vetorizador", vetorizador),
        ("modelo", LogisticRegression(max_iter=1000)),
    ])
    modelo.fit(textos, y_train)
    return modelo


def treinar(caminho_csv, caminho_saida):
    df = pd.read_csv(caminho_csv)

    x_train, x_test, y_train, y_test = train_test_split(
        df["texto"], df["sentimento"],
        test_size=0.25, stratify=df["sentimento"], random_state=42,
    )

    modelos = {
        "A": treinar_config(x_train, y_train, False, CountVectorizer()),
        "B": treinar_config(x_train, y_train, False, TfidfVectorizer()),
        "C": treinar_config(x_train, y_train, True, CountVectorizer()),
        "D": treinar_config(x_train, y_train, True, TfidfVectorizer()),
    }

    with open(caminho_saida, "w", encoding="utf-8") as f:
        f.write("Tamanho do vocabulário aprendido no treino:\n")
        for nome, modelo in modelos.items():
            tamanho = len(modelo["vetorizador"].vocabulary_)
            f.write(f"Config {nome}: {tamanho}\n")

    return modelos, x_train, y_train, x_test, y_test
