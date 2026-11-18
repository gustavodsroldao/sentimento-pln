from src.exploracao import explorar

# A avaliação não pede, porém caso estivessemos trabalhando com a possibilidade da pasta resultados
# não existir deveriamos validar
# os.makedirs("resultados", exist_ok=True)

# Etapa 1 - Exploração
explorar("data/Avaliacoes.csv", "resultados/exploracao.txt")
