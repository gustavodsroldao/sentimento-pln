
import pandas as pd
from sklearn.model_selection import StratifiedKFold, cross_validate

from src.preprocessamento import prep


def validar(modelos, x_train, y_train, caminho_saida):
    kf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    resultados = []

    for nome, modelo in modelos.items():
        remover = nome in ["C", "D"]

        textos = x_train.apply(lambda x: prep(x, remover_stopwords=remover))

        res = cross_validate(
            modelo,
            textos,
            y_train,
            cv=kf,
            scoring=["accuracy", "f1_macro"]
        )

        resultados.append({
            "config": nome,
            "stopwords": "removidas" if remover else "mantidas",
            "vetorizador": "Bag of Words" if nome in ["A", "C"] else "TF-IDF",
            "vocabulario": len(modelo["vetorizador"].vocabulary_),
            "acc_cv_media": res["test_accuracy"].mean(),
            "acc_cv_desvio": res["test_accuracy"].std(),
            "f1_cv_media": res["test_f1_macro"].mean(),
            "f1_cv_desvio": res["test_f1_macro"].std()
        })

    tabela = pd.DataFrame(resultados)
    tabela.to_csv(caminho_saida, index=False)

    melhor = tabela.loc[tabela["f1_cv_media"].idxmax(), "config"]

    return melhor
