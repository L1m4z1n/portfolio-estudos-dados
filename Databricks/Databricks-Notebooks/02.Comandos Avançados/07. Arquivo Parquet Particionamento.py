# Databricks notebook source
# MAGIC %md
# MAGIC ###### Documentação parquet
# MAGIC https://spark.apache.org/docs/latest/sql-data-sources-parquet.html 
# MAGIC
# MAGIC https://spark.apache.org/docs/latest/sql-data-sources-parquet.html

# COMMAND ----------

# MAGIC %md
# MAGIC ### Particionamento em Parquet ou Delta: Vantagens, Exemplos e Boas Práticas
# MAGIC
# MAGIC O particionamento de dados em formatos como Parquet ou Delta consiste em dividir grandes conjuntos de dados em subdiretórios baseados em valores de uma ou mais colunas (ex: data, estado, categoria). Isso permite que consultas leiam apenas os arquivos relevantes, otimizando performance e reduzindo custos de leitura.
# MAGIC
# MAGIC **Vantagens:**
# MAGIC - **Leitura eficiente:** Apenas partições relevantes são lidas, acelerando consultas.
# MAGIC - **Escalabilidade:** Facilita o processamento distribuído em grandes volumes de dados.
# MAGIC - **Gerenciamento:** Organiza dados de forma lógica, facilitando manutenção e arquivamento.
# MAGIC
# MAGIC **Exemplo de uso em Spark:**
# MAGIC python
# MAGIC df.write.partitionBy("coluna_particao").parquet("/caminho/para/parquet_particionado")
# MAGIC
# MAGIC Ou para Delta:
# MAGIC python
# MAGIC df.write.partitionBy("coluna_particao").format("delta").save("/caminho/para/delta_particionado")
# MAGIC
# MAGIC
# MAGIC **Volume recomendado:**  
# MAGIC Particionamento é recomendado para tabelas a partir de algumas centenas de milhares de linhas ou arquivos acima de 1GB. Para volumes pequenos, particionar pode não trazer ganhos e até prejudicar a performance.
# MAGIC
# MAGIC **Cuidado com excesso de partições:**  
# MAGIC Particionar demais pode gerar muitos arquivos pequenos ("small files problem"), aumentando o tempo de leitura e o overhead do metastore. Isso pode fazer com que consultas SQL ou Spark SQL realizem um scan completo do dataset, anulando os ganhos de performance.
# MAGIC
# MAGIC **Boas práticas:**
# MAGIC - Escolha colunas com baixa cardinalidade para particionar (ex: ano, mês, estado).
# MAGIC - Evite particionar por colunas com muitos valores únicos (ex: IDs).
# MAGIC - Monitore o número de arquivos e o tamanho médio das partições.
# MAGIC
# MAGIC **Referências:**
# MAGIC - [Documentação Parquet](https://spark.apache.org/docs/latest/sql-data-sources-parquet.html)
# MAGIC - [Documentação Delta Lake](https://docs.delta.io/latest/delta-batch.html#partitioning)

# COMMAND ----------

'''
path
└── to
    └── table
        ├── gender=male
        │   ├── ...
        │   │
        │   ├── country=US
        │   │   └── data.parquet
        │   ├── country=CN
        │   │   └── data.parquet
        │   └── ...
        └── gender=female
            ├── ...
            │
            ├── country=US
            │   └── data.parquet
            ├── country=CN
            │   └── data.parquet
            └── ...
'''

# COMMAND ----------

df_parquet=spark.read.parquet("/Volumes/curso_databricks/aula/aula_volume/Anac/parquet/")
df_parquet.display()

# COMMAND ----------

#verificando dados distintos de colunas com spark sql Classificacao_da_Ocorrência

display(df_parquet.select("Classificacao_da_Ocorrência").distinct())

# COMMAND ----------

#verificando dados distintos de colunas com spark sql UF
display(df_parquet.select("UF").distinct())



# COMMAND ----------

# MAGIC %md
# MAGIC Salvar em particionamento UF, outra para Ocorrencias e outro usando os 2

# COMMAND ----------

# MAGIC %md
# MAGIC Salvar partition = UF

# COMMAND ----------

(
df_parquet.write
  .format("parquet")
  .partitionBy("UF")
  .mode("overwrite")
  .save("/Volumes/curso_databricks/aula/aula_volume/Anac/parquet_partition_UF/")
)

# COMMAND ----------

#ver arquivo particionado
display(dbutils.fs.ls("/Volumes/curso_databricks/aula/aula_volume/Anac/parquet_partition_UF/"))

# COMMAND ----------

#Descendo mais um nivel 
display(dbutils.fs.ls("/Volumes/curso_databricks/aula/aula_volume/Anac/parquet_partition_UF/UF=MG/"))


# COMMAND ----------

# MAGIC %md
# MAGIC Partition = Ocorrencia

# COMMAND ----------

(
df_parquet.write
  .format("parquet")
  .partitionBy("Classificacao_da_Ocorrência")
  .mode("overwrite")
  .save("/Volumes/curso_databricks/aula/aula_volume/Anac/parquet_partition_ocorrencia/")
)

# COMMAND ----------

#ver arquivo particionado
display(dbutils.fs.ls("/Volumes/curso_databricks/aula/aula_volume/Anac/parquet_partition_ocorrencia/"))

# COMMAND ----------

#ver arquivo particionado subnivel
display(dbutils.fs.ls("/Volumes/curso_databricks/aula/aula_volume/Anac/parquet_partition_ocorrencia/Classificacao_da_Ocorrência=Incidente Grave/"))

# COMMAND ----------

#lendo pasta geral
df_uf_geral=spark.read.parquet("/Volumes/curso_databricks/aula/aula_volume/Anac/parquet_partition_UF/")
display(df_uf_geral)


# COMMAND ----------

from pyspark.sql.functions import lit
# ler apenas uma partição especifica
df_uf_mg = spark.read.parquet("/Volumes/curso_databricks/aula/aula_volume/Anac/parquet_partition_UF/UF=MG/")

df_uf_mg=df_uf_mg.withColumn("UF", lit("MG"))

display(df_uf_mg)

# COMMAND ----------

# MAGIC %md
# MAGIC ######Salvando em mais de 1 partição 

# COMMAND ----------

#simulando o responsavel de Mg onde a Classificacao da Ocorrência seja igual a Acidente trabalharia com o arquivo 
#dbfs:/FileStore/tables/Anac/parquet_Multiparticionado/UF=MG/Classificacao_da_Ocorrência=Acidente/
#e nao todo o arquivo original , ganhando performace na leitura 

# COMMAND ----------

(
df_parquet.write
  .format("parquet")
  .partitionBy("UF","Classificacao_da_Ocorrência")
  .mode("overwrite")
  .save("/Volumes/curso_databricks/aula/aula_volume/Anac/parquet_multipartition/")
)

# COMMAND ----------

#ver arquivo particionado subnivel
display(dbutils.fs.ls("/Volumes/curso_databricks/aula/aula_volume/Anac/parquet_multipartition/"))

# COMMAND ----------

#ver arquivo particionado subnivel2
display(dbutils.fs.ls("/Volumes/curso_databricks/aula/aula_volume/Anac/parquet_multipartition/UF=MG/"))

# COMMAND ----------

# MAGIC %md
# MAGIC Dados Acidente do analista de MG

# COMMAND ----------

df_minas_grave=spark.read.parquet('/Volumes/curso_databricks/aula/aula_volume/Anac/parquet_multipartition/UF=MG/Classificacao_da_Ocorrência=Incidente Grave/')
df_minas_grave.display()

# COMMAND ----------

# MAGIC %sql
# MAGIC -- exemplo de consulta otimizada
# MAGIC SELECT * FROM suatabela 
# MAGIC where UF = 'MG'
# MAGIC and Classificacao_da_Ocorrência='Incidente Grave'