# Databricks notebook source
# MAGIC %md
# MAGIC #####Documentação CSV
# MAGIC ######Pesquisar csv documentation databricks\
# MAGIC https://docs.databricks.com/pt/external-data/csv.html

# COMMAND ----------

display(dbutils.fs.ls("/Volumes/curso_databricks/aula/aula_volume/Anac"))

# COMMAND ----------

#ler CSV avançado
arquivo_origem= "/Volumes/curso_databricks/aula/aula_volume/Anac/V_OCORRENCIA_AMPLA.csv"
df_anac=(spark.read
          .format("csv")
          .option("header", "true")
          .option("sep", ";")
          .option("skipRows", 1)
          .load(arquivo_origem)
  
)
df_anac.display()

# COMMAND ----------

arquivo_origem= "/Volumes/curso_databricks/aula/aula_volume/Anac/V_OCORRENCIA_AMPLA.csv"
df_anac=(spark.read
          .format("csv")
          .options(header= True,
                   sep=";",
                   skipRows=1)

          .load(arquivo_origem)
  
)
df_anac.display()

# COMMAND ----------

#exemplo de varias opções 
caminho__origem="/Volumes/curso_databricks/aula/aula_volume/Anac/V_OCORRENCIA_AMPLA.csv"

df_anac = (spark.read
    .format("csv")
    .options(
        skipRows=1,                      # Pula a primeira linha (útil para ignorar metadados)
        header=True,                     # Usa a primeira linha como cabeçalho
        sep=";",                         # Define o separador de campo como ponto e vírgula
        inferSchema=True,                # Detecta automaticamente os tipos de dados das colunas
        quote='"',                       # Define o caractere de aspas para campos com delimitadores
        escape="\\",                     # Define o caractere de escape para aspas ou delimitadores
        multiLine=False,                 # Define se linhas podem conter quebras de linha
        charset="UTF-8",                 # Define o charset para leitura do arquivo
        nullValue="",                    # Define o valor que será interpretado como nulo
        dateFormat="yyyy-MM-dd",         # Define o formato de datas
        timestampFormat="yyyy-MM-dd HH:mm:ss", # Define o formato de timestamps
        ignoreLeadingWhiteSpace=True,    # Ignora espaços em branco à esquerda dos valores
        ignoreTrailingWhiteSpace=True,   # Ignora espaços em branco à direita dos valores
        mode="PERMISSIVE",               # Modo de tratamento de erros (PERMISSIVE ignora linhas malformadas)
        comment="#",                     # Define o caractere de comentário para ignorar linhas
        encoding="UTF-8",                # Define a codificação do arquivo
        emptyValue="",                   # Define o valor para campos vazios
        nanValue="NaN"                   # Define o valor que será interpretado como NaN
    )
    .load(caminho__origem)
)
df_anac.display()

# COMMAND ----------

# MAGIC %sql
# MAGIC -- leitura rapida do arquivo só para ver os dados como validações ou exploração por exemplo
# MAGIC SELECT * FROM read_files(
# MAGIC   '/Volumes/curso_databricks/aula/aula_volume/Anac/V_OCORRENCIA_AMPLA.csv',
# MAGIC   format => 'csv',
# MAGIC   header => true,
# MAGIC   skipRows => 1,
# MAGIC   sep => ';',
# MAGIC   inferSchema => true
# MAGIC
# MAGIC )
# MAGIC where Classificacao_da_Ocorrencia = 'Incidente'
# MAGIC and UF = 'RJ'
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Salvando Arquivo em Volume

# COMMAND ----------

#ler CSV 
arquivo_origem= "/Volumes/curso_databricks/aula/aula_volume/Anac/V_OCORRENCIA_AMPLA.csv"
df_anac=(spark.read
          .format("csv")
          .option("header", "true")
          .option("sep", ";")
          .option("skipRows", 1)
          .load(arquivo_origem)
  
)
df_anac.display()

# COMMAND ----------

#Salvar arquivo em Volume para ver o resultado e arquivos gerados
caminho_destino = '/Volumes/curso_databricks/aula/aula_volume/Anac/output'
(df_anac.write
    .format("csv")
    .option("header", True)
    .option("sep", ";")
    .mode("overwrite")
    .save(caminho_destino)
)

# COMMAND ----------

display(dbutils.fs.ls(caminho_destino))

# COMMAND ----------

'''
_SUCCESS
_committed_8527903177252253576
_started_8527903177252253576
part-00000-tid-8527903177252253576-e1f1eccd-7445-4b08-98ed-2c819503c3bf-397-1-c000.csv


Quando você salva um DataFrame no formato CSV usando Spark, são gerados vários arquivos no diretório de destino:
- **_SUCCESS**: Indica que a operação de escrita foi concluída com sucesso.
- **_committed_*** e **_started_***: Arquivos de controle internos do Spark para rastrear o progresso e o commit da escrita.
- **part-*.csv**: Arquivos de dados, cada um contendo uma parte dos dados do DataFrame. Spark salva os dados em múltiplos arquivos (partições) para otimizar o processamento distribuído.

Esses arquivos são padrão do Spark e garantem integridade, rastreabilidade e desempenho na manipulação de grandes volumes de dados.

Ao ler um diretório com várias partições (vários arquivos part-*.csv), Spark automaticamente lê todos os arquivos de dados do diretório e combina as partições em um único DataFrame, permitindo o processamento distribuído e eficiente.

'''''


# COMMAND ----------

#ler dados salvos, agora como passou pelo spark otimizado no passo o caminho do CSV mas sim a pasta raiz
arq_origem="/Volumes/curso_databricks/aula/aula_volume/Anac/output"
df_anac_teste=(spark.read
          .format("csv")
          .option("header", "true")
          .option("sep", ";")
          .option("skipRows", 1)
          .load(arquivo_origem)
)
df_anac_teste.display()

# COMMAND ----------

# lendo um arquivo especifico comundo em dados exploratórios
#ler dados salvos, agora como passou pelo spark otimizado no passo o caminho do CSV mas sim a pasta raiz
arq_origem="dbfs:/Volumes/curso_databricks/aula/aula_volume/Anac/output/part-00000-tid-7072013334175157512-bb1ae027-4c6b-43f2-97cc-63fa2e0b1b12-562-1-c000.csv"
df_anac_teste2=(spark.read
          .format("csv")
          .option("header", "true")
          .option("sep", ";")
          .option("skipRows", 1)
          .load(arquivo_origem)
)
df_anac_teste2.display()


# COMMAND ----------

# forçar gerar mais de um arquivo particionado
caminho_destino = '/Volumes/curso_databricks/aula/aula_volume/Anac/output-repartition'
df_anac_teste.repartition(4).write \
    .format("csv") \
    .option("header", True) \
    .option("sep", ";") \
    .mode("overwrite") \
    .save(caminho_destino)


# COMMAND ----------

display(dbutils.fs.ls(caminho_destino))

# COMMAND ----------

#Ler dados

caminho_origem = '/Volumes/curso_databricks/aula/aula_volume/Anac/output-repartition'
df_anac = (spark.read
    .format("csv") 
    .option("skipRows", 1)
    .option("header", True) 
    .option("sep", ";") 
    .load(caminho_origem)
)
df_anac.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Salvando Arquivo em Tamanho reduzido
# MAGIC https://spark.apache.org/docs/latest/sql-data-sources-csv.html > pesquisar por 'compression' no Control+F no navegador
# MAGIC
# MAGIC
# MAGIC Pesquisar no google conversor bytes para mb

# COMMAND ----------

caminho__origem="/Volumes/curso_databricks/aula/aula_volume/Anac/V_OCORRENCIA_AMPLA.csv"

df_anac=(spark.read
    .format("csv")
    .option("skipRows", 1)
    .option("header", True)
    .option("sep", ";")
    .option("inferSchema", True)
    .load(caminho__origem)
    )
df_anac.display()

# COMMAND ----------

#salvar normal na pasta compact 
caminho_destino = '/Volumes/curso_databricks/aula/aula_volume/Anac/compact-simple'
(df_anac.write
    .format("csv")
    .option("header", True)
    .option("sep", ";")
    .mode("overwrite")
    .save(caminho_destino)
)

# COMMAND ----------

#Salvar Compactado
#salvar normal na pasta compact 
caminho_destino = '/Volumes/curso_databricks/aula/aula_volume/Anac/compact-zip'
(df_anac.write
    .format("csv")
    .option("compression", "gzip")
    .option("header", True)
    .option("sep", ";")
    .mode("overwrite")
    .save(caminho_destino)
)

# COMMAND ----------

#Salvar Compactado
#salvar normal na pasta compact 
caminho_destino = '/Volumes/curso_databricks/aula/aula_volume/Anac/compact-zip-snappy'
(df_anac.write
    .format("csv")
    .option("compression", "snappy")
    .option("header", True)
    .option("sep", ";")
    .mode("overwrite")
    .save(caminho_destino)
)

# COMMAND ----------

display(dbutils.fs.ls('/Volumes/curso_databricks/aula/aula_volume/Anac/compact-simple'))



# COMMAND ----------

display(dbutils.fs.ls('/Volumes/curso_databricks/aula/aula_volume/Anac/compact-zip'))


# COMMAND ----------

display(dbutils.fs.ls('/Volumes/curso_databricks/aula/aula_volume/Anac/compact-zip-snappy'))


# COMMAND ----------

'''
Se o arquivo tinha 8.706.757 e ficou com 2.431.519 após zipar, podemos calcular assim:

Taxa de compressão
8.706.757÷2.431.519≈3,58

Ou seja:

O arquivo ficou cerca de 3,58 vezes menor.
Em porcentagem, reduziu aproximadamente 72,1% do tamanho original.

Cálculo da economia:

Espaço economizado:
8.706.757−2.431.519=6.275.238
Percentual restante:
2.431.519÷8.706.757×100≈27,9

Então você pagaria apenas cerca de 27,9% do armazenamento original.

Exemplo:

Se armazenar o original custasse R$100
O zipado custaria cerca de R$27,90
Economia de R$72,10.



'''

# COMMAND ----------

#ler dados de uma pasta compactar 
caminho__origem='/Volumes/curso_databricks/aula/aula_volume/Anac/compact-zip'

df_anac=(spark.read
    .format("csv")
    .option("compression", "gzip")
    .option("header", True)
    .option("sep", ";")
    .option("inferSchema", True)
    .load(caminho__origem)
    )
df_anac.display()
