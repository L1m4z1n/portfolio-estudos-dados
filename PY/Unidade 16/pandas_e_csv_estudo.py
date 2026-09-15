#Pandas e CSV
#Resumo - quase sempre quando formos "ler" um arquivo csv, vamos usar o pandas. é prático e bem eficiente

#Funcionamento
#forma mais básica: (muitas vezes não usaremos a forma mais básica)
#dataframe = pd.read_csv(arquivo_com_extensao)

# - Vamos ler um arquivo real, com a base de dados de vendas da empresa "Contoso"

import pandas as pd
vendas_df = pd.read_csv(r'C:\Users\Miguel\OneDrive\Documentos\Hashtag_cursos\portfolio-estudos-dados\PY\Unidade 16\Contoso - Cadastro Produtos.csv', sep=';')
print(vendas_df)