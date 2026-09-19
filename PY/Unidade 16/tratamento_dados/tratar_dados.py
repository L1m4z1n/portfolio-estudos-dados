'''
# Comparando, Tratando e Mesclando DataFrames

## Objetivo

Vamos modificar os IDs para os nomes dos produtos, dos clientes e das lojas, para nossas análises ficarem mais intuitivas futuramente. Para isso, vamos criar um data frame com todos os detalhes.

- Usaremos o método merge para isso e, depois se quisermos, podemos pegar apenas as colunas que queremos do dataframe final.

### Criando nossos dataframes

'''

import pandas as pd
from IPython.display import display

#às vezes precisaremos mudar o encoding. Possiveis valores para testar:
#encoding='latin1', encoding='ISO-8859-1', encoding='utf-8' ou então encoding='cp1252'
vendas_df = pd.read_csv(r'C:\Users\Miguel\OneDrive\Documentos\Hashtag_cursos\portfolio-estudos-dados\PY\Unidade 16\tratamento_dados\Contoso - Vendas - 2017.csv', sep=';',encoding='ISO-8859-1')
produtos_df = pd.read_csv(r'C:\Users\Miguel\OneDrive\Documentos\Hashtag_cursos\portfolio-estudos-dados\PY\Unidade 16\tratamento_dados\Contoso - Cadastro Produtos.csv', sep=';',encoding='ISO-8859-1')
lojas_df = pd.read_csv(r'C:\Users\Miguel\OneDrive\Documentos\Hashtag_cursos\portfolio-estudos-dados\PY\Unidade 16\tratamento_dados\Contoso - Lojas.csv', sep=';',encoding='ISO-8859-1')
clientes_Df = pd.read_csv(r'C:\Users\Miguel\OneDrive\Documentos\Hashtag_cursos\portfolio-estudos-dados\PY\Unidade 16\tratamento_dados\Contoso - Clientes.csv', sep=';',encoding='ISO-8859-1')


#usaremos o display para ver todos os dataframes
display(vendas_df)
display(produtos_df)
display(lojas_df)
display(clientes_Df)


'''
### Vamos tirar as colunas inúteis do clientes_df ou pegar apenas as colunas que quisermos

.drop([coluna1, coluna2, coluna3]) -> retira as colunas: coluna1, coluna2, coluna3
'''
clientes_Df = clientes_Df.drop(['Unnamed: 7','Unnamed: 8','Unnamed: 9','Unnamed: 10',])

clientes_Df= clientes_Df[['ID Cliente','E-mail']]
produtos_df = produtos_df[['ID Produto','Nome do Produto']]
lojas_df = [['ID Loja','Nome da Loja']]
display(produtos_df)

'''
### Agora vamos juntar os dataframes para ter 1 único dataframe com tudo "bonito"

novo_dataframe = dataframe1.merge(dataframe2, on='coluna')

- Obs: O merge precisa das colunas com o mesmo nome para funcionar. Se não tiver, você precisa alterar o nome da coluna com o .rename

dataframe.rename({'coluna1': 'novo_coluna_1'})
'''
#juntando os dataframes
vendas_df = vendas_df.merge(produtos_df, on='ID Produto')
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')
vendas_df = vendas_df.merge(clientes_Df, on='ID Cliente')

#exibindo o dataframe final
display(vendas_df)

#vamos renomear o e-mail para ficar claro que é do cliente
vendas_df = vendas_df.rename(columns={'E-mail': 'E-mail do Cliente'})

### Agora podemos começar as análises
