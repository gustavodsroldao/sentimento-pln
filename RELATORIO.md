# RELATORIO: Análise de Sentimento com PLN

**Nome:** Gustavo da Silveira Roldão
**Repositório:** sentimento-pln
**Data:** 17/11/2026

## Tabela-resumo

| Config | Stopwords | Vetorizador | Vocabulário | Acurácia CV (média ± desvio) | F1 CV (média ± desvio) |
|---|---|---|---|---|---|
| A | mantidas | bow | 420 | 0,856 ± 0,093 | 0,856 ± 0,093 |
| B | mantidas | tf-idf | 420 | 0,846 ± 0,084 | 0,846 ± 0,084 |
| C | removidas | bow | 404 | 0,851 ± 0,089 | 0,851 ± 0,089 |
| D | removidas | tf-idf | 404 | 0,841 ± 0,082 | 0,841 ± 0,082 |

**Configuração escolhida:** A
**Acurácia no teste:** 0,82
**F1 no teste:** 0,81

---

## 1. Pré-processamento

Passei tudo para minúsculas e tirei pontuação e números, mantendo os acentos. Com isso "R$ 50" vira só "r".
Usei uma lista própria de 28 stopwords. O vocabulário foi de 420 para 404 palavras (16 a menos).
Deixei "não", "nunca", "nem" e "sem" fora da lista, senão "não gostei" viraria "gostei".

## 2. bow vs. tf-idf

Médias: A 0,856, C 0,851, B 0,846, D 0,841. A diferença é de uns 1,5 ponto e o desvio é perto de 0,09, então na prática estão empatadas.
Escolhi a A só por ter a maior média de F1 na validação cruzada, que era o critério.
O bow conta as palavras e o tf-idf dá mais peso às raras. Como os textos são curtos (cerca de 7,7 palavras), quase nada se repete e os dois dão resultado parecido.

## 3. Avaliação no teste

Dos 65 textos, acertou 25 negativos e 28 positivos. Errou 8 negativos e 4 positivos.
Negativo: precisão 0,86, recall 0,76, F1 0,81. Positivo: precisão 0,78, recall 0,88, F1 0,82.
O erro mais grave é tratar reclamação como elogio, e foi o mais comum (8 contra 4).
A acurácia engana pouco aqui porque as classes são equilibradas (33 e 32).

## 4. Validação cruzada vs. divisão única

Com só 65 textos de teste, a nota muda muito conforme quais caíram ali. Na validação cruzada (5 partes) olho média e desvio, que dão uma ideia mais firme.
Escolher pelo teste deixaria a nota final otimista, porque ele deixa de ser dado novo.
Vazamento seria ajustar o vetorizador com todos os textos. Evitei usando um Pipeline, que treina o vetorizador só com o treino, inclusive em cada fold.

## 5. Análise de erros e palavras influentes

- "Ficou lindo na sala, combinou perfeitamente com os móveis" (positivo) foi previsto negativo (0,52): "lindo" e "móveis" não aparecem no treino.
- "Camiseta encolheu e desbotou depois da primeira lavagem" (negativo) foi previsto positivo (0,59): reclama sem palavra clara de sentimento.
- "Panela de péssima qualidade, a comida gruda e queima" (negativo) foi previsto positivo (0,67), apesar do "péssima".

Entre as positivas, "bastante" tem o maior coeficiente (2,34), seguida de "bem" (0,91). Entre as negativas aparecem "dinheiro" (-0,70, de "perda de dinheiro"), "toda" (-0,68) e "mais" (-0,63), que não são de sentimento.
O modelo aprendeu padrões do treino, não o sentido das frases.

## 6. Casos difíceis e limitações

Negação: acertou 2 de 4 e errou "Não tenho nada a reclamar, tudo perfeito" (0,44) e "Sem defeitos, funciona direitinho" (0,44).
Ironia: acertou 2 de 3 e errou "Que ótimo, o produto chegou quebrado" (0,83 de positivo).
Nas duas frases mistas previu positivo (0,79 e 0,88), e em "Chegou ontem" (neutro) também, com 0,51, quase empate. Como só existem duas classes, essas não têm resposta certa; a probabilidade mostra a dúvida.
Isso ocorre porque bow e tf-idf ignoram a ordem das palavras, então "não" e "ruim" não se ligam.
Melhorias: n-gramas (como "não gostei") e embeddings ou um modelo de linguagem pré-treinado.
O dataset tem só 260 textos curtos, de assuntos misturados, sem classe neutra. Em produção, uma ironia ou reclamação educada pode passar como elogio sem ninguém notar.

---

## Declaração de uso de IA

- [ ] Não usei IA generativa em nenhuma parte deste trabalho.
- [x] Usei IA generativa **somente** para: Entender melhor a implementação da validação cruzada, na qual utilizei a linguagem C# para me referenciar. Além disso validei também se minha implementação de modelos estava correta.
