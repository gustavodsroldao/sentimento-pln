import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix

from src.preprocessamento import prep


def avaliar(modelo, remover, x_teste, y_teste):
    textos = x_teste.apply(lambda texto: prep(texto, remover_stopwords=remover))

    previsto = modelo.predict(textos)
    probabilidades = modelo.predict_proba(textos)

    classes = modelo.classes_
    matriz = confusion_matrix(y_teste, previsto, labels=classes)
    matriz = pd.DataFrame(matriz, index=classes, columns=classes)
    matriz.to_csv("resultados/matriz_confusao.csv", index_label="real")

    with open("resultados/relatorio_classificacao.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(classification_report(y_teste, previsto))

    erros = pd.DataFrame({
        "texto": x_teste,
        "real": y_teste,
        "previsto": previsto,
        "probabilidade": probabilidades.max(axis=1),
    })
    erros = erros[erros["real"] != erros["previsto"]]
    erros.to_csv("resultados/erros.csv", index=False)

    palavras = modelo["vetorizador"].get_feature_names_out()
    coeficientes = modelo["modelo"].coef_[0]

    tabela = pd.DataFrame({"palavra": palavras, "coeficiente": coeficientes})
    tabela = tabela.sort_values("coeficiente")

    negativas = tabela.head(10)
    positivas = tabela.tail(10).iloc[::-1]

    influentes = pd.concat([positivas, negativas])
    influentes["empurra_para"] = ["positivo"] * 10 + ["negativo"] * 10
    influentes.to_csv("resultados/palavras_influentes.csv", index=False)
