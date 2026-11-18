from src.exploracao import explorar
from src.modelos import treinar

# A avaliação não pede, porém caso estivessemos trabalhando com a possibilidade da pasta resultados
# não existir deveriamos validar
# os.makedirs("resultados", exist_ok=True)

# Etapa 1 - Exploração
explorar("data/Avaliacoes.csv", "resultados/exploracao.txt")

# Etapa 3 - Vetorização e modelos
modelos = treinar("data/Avaliacoes.csv", "resultados/vocabulario.txt")
