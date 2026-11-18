import pandas as pd

from src.preprocessamento import prep


def prever_dificeis(modelo, remover, caminho_csv, caminho_saida):
    casos = pd.read_csv(caminho_csv)

    textos = casos["texto"].apply(lambda texto: prep(texto, remover_stopwords=remover))

    previsto = modelo.predict(textos)
    probabilidades = modelo.predict_proba(textos)
    coluna_positivo = list(modelo.classes_).index("positivo")

    resultado = pd.DataFrame({
        "texto": casos["texto"],
        "tipo": casos["tipo"],
        "esperado": casos["sentimento_esperado"],
        "previsto": previsto,
        "prob_positivo": probabilidades[:, coluna_positivo],
    })
    resultado.to_csv(caminho_saida, index=False)
