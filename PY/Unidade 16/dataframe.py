'''
# DataFrame


## Resumo

É como se fosse uma tabela.

- As colunas funcionam "como chaves de dicionário"
- As linhas funcionam "como listas"

## Funcionamento

Temos um dataframe chamado vendas_df

vendas_df['coluna_x'] -> uma lista com os valores da coluna_x (em formato dataframe, é um dataframe com 1 coluna só)
vendas_df[0] -> NÃO FUNCIONA ASSIM PARA DATAFRAMES
vendas_df[:3] -> pega até a linha de índice 3 do dataframe
vendas_df[['coluna_x', 'coluna_y', 'coluna_z']] -> cria um novo dataframe com as colunas coluna_x, coluna_y e coluna_z
vendas_df['coluna_x'][0] -> pega o itemd a 1ª linha da coluna coluna_x

- Vamos ler um arquivo real, com a Base de Dados de Vendas da Empresa "Contoso"


'''
import pandas as pd
vendas_df = pd.read_csv(r'C:\Users\Miguel\OneDrive\Documentos\Hashtag_cursos\portfolio-estudos-dados\PY\Unidade 16\Contoso - Cadastro Produtos.csv', sep=';')
vendas_df['ID Produto'][0]

'''
- O 1º passo de toda Análise de Dados é você entender o que existe na sua base de dados

Usaremos o .info() para isso
'''
vendas_df.info()

'''
- Vamos criar então agora uma lista de Clientes
'''

lista_clientes = vendas_df['ID Cliente']
lista_clientes

'''
- Vamos criar agora uma lista com os produtos e as quantidades de vendas dele, caso a gente queira analisar só os produtos (independente de data ou de cliente)
'''

lista_colunas = ['ID Produto', 'Quantidade Vendida', 'Quantidade Devolvida']
produtos_quantidade = vendas_df[]
produtos_quantidade