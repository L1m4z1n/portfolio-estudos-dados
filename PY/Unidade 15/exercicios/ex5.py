'''
## Exercício

Você é um analista de dados em uma empresa e conduziu uma pesquisa de satisfação do cliente durante uma semana. Você perguntou as clientes para classificar seu nível de satisfação com o serviço ao cliente em uma escala de 0 a 10. Você coletou respostas de 30 clientes por dia durante 7 dias, resultando em um total de 210 respostas.

No entanto, os dados que você recebeu estão em um array 1D de 210 elementos. Reorganize os dados de forma a ter as respostas por dia e faça uma análise descritiva básica, calculando a média geral de satisfação e a média diária.
'''
import numpy as np

# considere os seguintes dados aleatórios como início
rng = np.random.default_rng(seed=42)
respostas = rng.integers(low=0, high=10, size=210, endpoint=True)
#print(respostas)
'''
O seguinte modelo pode ser pensado para os dados recebidos:

    dia 1 cliente 1, dia 1 cliente 2, dia 1 cliente 3, ...
    dia 7 cliente 28, dia 7 cliente 29, dia 7 cliente 30
    
Assim, podemos fazer um reshape:
'''
resposta_reshape = np.reshape(respostas, (7,30))

media_geral = np.mean(resposta_reshape)
resposta_dia = (resposta_reshape.sum(axis=0))
resposta_geral = (resposta_reshape.sum(axis=1))
media_diaria = np.mean(resposta_reshape, axis=1)

for i, diaria in enumerate(resposta_geral,start=1):
    print(f"Cliente {i}: {diaria}")

print(media_diaria)