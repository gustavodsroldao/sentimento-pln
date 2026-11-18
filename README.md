# Análise de Sentimento com PLN

Trabalho da disciplina de Algoritmos de IA (ULBRA). O objetivo é classificar avaliações de produtos como positivas ou negativas usando regressão logística, e comparar como o pré-processamento e a vetorização mudam o resultado.

## O que a atividade faz

1. **Exploração** do dataset (`data/Avaliacoes.csv`, 260 textos curtos).
2. **Pré-processamento**: minúsculas, sem pontuação e números, com lista própria de stopwords (mantendo "não", "nunca", "nem" e "sem").
3. **Vetorização e modelos**: 4 configurações, combinando stopwords mantidas ou removidas com bow ou tf-idf.
4. **Validação cruzada** (5 folds) para escolher a melhor configuração.
5. **Avaliação final** no conjunto de teste: matriz de confusão, erros e palavras mais influentes.
6. **Casos difíceis** (negação, ironia, frases mistas e neutras) em `data/casos_dificeis.csv`.

A análise e as conclusões estão no [RELATORIO.md](RELATORIO.md).

## Como rodar

Requer Python 3.14 ou superior.

```bash
pip install -r requirements.txt
python main.py
```

Os arquivos gerados ficam na pasta `resultados/`.

## Estrutura

- `main.py`: roda todas as etapas em ordem.
- `src/`: um módulo por etapa (`exploracao`, `preprocessamento`, `modelos`, `validacao`, `avaliacao`, `dificeis`).
- `data/`: dataset e casos difíceis.
- `resultados/`: saídas geradas (comparação, erros, vocabulário, predições).

## Autor

Gustavo da Silveira Roldão
