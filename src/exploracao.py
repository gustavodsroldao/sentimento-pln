import pandas as pd


def explorar(caminho_csv, caminho_saida):
    df = pd.read_csv(caminho_csv)

    # Numero de linhas
    numero_linhas = len(df)

    # Distribuição de classes
    distribuicao_classes = df["sentimento"].value_counts()

    # Coluna nova na qual calcula o tamanho médio
    df["numero_palavras"] = df["texto"].astype(str).str.split().str.len()
    medidas_por_classe = df.groupby("sentimento")["numero_palavras"].mean()

    with open(caminho_saida, "w", encoding="utf-8") as f:
        f.write(f"Número de linhas: {numero_linhas}\n\n")

        f.write("Distribuição das classes:\n")
        for classe, qtd in distribuicao_classes.items():
            f.write(f"{classe}: {qtd} {qtd / numero_linhas:.1%}\n")

        f.write("\nTamanho médio dos textos em palavras por classe:\n")
        for classe, media in medidas_por_classe.items():
            f.write(f"{classe}: {media:.2f}\n")

        f.write("\n3 exemplos de cada classe:\n")
        for classe in df["sentimento"].unique():
            linhas = df[df["sentimento"] == classe]
            amostra = linhas["texto"].sample(min(3, len(linhas)))

            f.write(f"\nClasse: {classe}\n")
            for texto in amostra:
                f.write(f"-> {texto}\n")

    return df
