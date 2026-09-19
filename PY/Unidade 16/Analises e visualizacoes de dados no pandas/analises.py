'''
# Resumos e um pouco de Visualização no pandas


## Resumo

Vamos ver alguns métodos para analisar nossas tabelas (dataframes)

Além disso, vamos usar os plot de gráfico padrões do pandas, mas no projeto de DataScience veremos outras mais bonitas e também muito práticas.

OBS: O pandas usa o matplotlib (que vimos na seção de "módulos e bibliotecas") para plotar gráficos.<br>
Se quiser personalizar mais do que o padrão do pandas, importe o matplotlib e use os métodos do matplotlib

- Preparando as bases de dados (o que fizemos na última aula)
'''

import pandas as pd
from IPython.display import display
#importando os arquivos
vendas_df = pd.read_csv(r'C:\Users\Miguel\OneDrive\Documentos\Hashtag_cursos\portfolio-estudos-dados\PY\Unidade 16\tratamento_dados\Contoso - Vendas - 2017.csv', sep=';',encoding='ISO-8859-1')
produtos_df = pd.read_csv(r'C:\Users\Miguel\OneDrive\Documentos\Hashtag_cursos\portfolio-estudos-dados\PY\Unidade 16\tratamento_dados\Contoso - Cadastro Produtos.csv', sep=';',encoding='ISO-8859-1')
lojas_df = pd.read_csv(r'C:\Users\Miguel\OneDrive\Documentos\Hashtag_cursos\portfolio-estudos-dados\PY\Unidade 16\tratamento_dados\Contoso - Lojas.csv', sep=';',encoding='ISO-8859-1')
clientes_df = pd.read_csv(r'C:\Users\Miguel\OneDrive\Documentos\Hashtag_cursos\portfolio-estudos-dados\PY\Unidade 16\tratamento_dados\Contoso - Clientes.csv', sep=';',encoding='ISO-8859-1')


# Ajustar nome das colunas
produtos_df.rename(columns={'ÿNome do Produto': 'Nome do Produto'}, inplace=True)
clientes_df.rename(columns={'ÿID Cliente': 'ID Cliente'}, inplace=True)
lojas_df.rename(columns={'ÿID Loja': 'ID Loja'}, inplace=True)


#limpando apenas as colunas que queremos
clientes_df = clientes_df[['ID Cliente', 'E-mail']]
produtos_df = produtos_df[['ID Produto', 'Nome do Produto']]
lojas_df = lojas_df[['ID Loja', 'Nome da Loja']]


#mesclando e renomeando os dataframes
vendas_df = vendas_df.merge(produtos_df, on='ID Produto')
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')
vendas_df = vendas_df.merge(clientes_df, on='ID Cliente').rename(columns={'E-mail': 'E-mail do Cliente'})
display(vendas_df)

'''
### Qual cliente que comprou mais vezes?

- Usaremos o método .value_counts() para contar quantas vezes cada valor do Dataframe aparece
- Usaremos o método .plot() para exibir um gráfico
'''
frequencia_clientes = vendas_df['E-mail do Cliente'].value_counts()
display(frequencia_clientes)
frequencia_clientes[:5].plot(figsize=(15,5))

'''
### Qual a Loja que mais vendeu?

- Usaremos o .groupby para agrupar o nosso dataframe, de acordo com o que queremos (somando as quantidades de vendas, por exemplo)

- Agora precisamos pegar o maior valor. Temos 2 formas:
    1. Ordenar o dataframe em ordem decrescente de Quantidade Vendida
        - Método .sort_values
    2. Pegar o Maior valor diretamente
        - Métodos .max() e .idxmax()


'''
#ordenando o dataframe

#podemos plotar em um gráfico


#pegando o maior valor e se índice


'''
### Qual produto que menos vendeu?

- Já temos uma lista criada para isso, basta verificarmos o final da lista (já que ela está ordenada) ou então usarmos os métodos:
    1. min()
    2. idxmin()
'''