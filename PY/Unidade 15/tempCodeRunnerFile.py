import numpy as np

# Salários dos funcionários
salarios = np.array([3000, 3500, 4000, 2000, 4500, 4000, 5000])

# Calcular a média salarial
media_salarial = np.mean(salarios)

print(media_salarial)

# Identificar funcionários com salários acima da média
funcionarios_acima_media = np.where(salarios > media_salarial)
print(funcionarios_acima_media)