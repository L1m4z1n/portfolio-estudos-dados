'''
## Exercício

Você é um engenheiro de produção e tem os tempos de ciclo (em minutos) de uma linha de produção em um array NumPy. Seu trabalho é identificar quaisquer tempos de ciclo que estão dois desvios padrão acima ou abaixo da média. Use o seguinte array para sua análise: `tempos_ciclo = np.array([5.5, 5.7, 5.9, 6.0, 5.8, 5.6, 5.7, 7.2, 4.8])`. 

'''
import numpy as np

tempos_ciclo = np.array([5.5, 5.7, 5.9, 6.0, 5.8, 5.6, 5.7, 7.2, 4.8])

media = np.mean(tempos_ciclo)
desvio_padrao = np.std(tempos_ciclo)
condicao = tempos_ciclo > 5
condicao_2 = (tempos_ciclo>media+2 * desvio_padrao)|(tempos_ciclo < media - 2 *desvio_padrao)
anomalias = np.where(condicao_2)
print(anomalias)