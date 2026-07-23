# Databricks notebook source
# MAGIC %md
# MAGIC #####Documentação Databricks
# MAGIC https://docs.databricks.com/pt/external-data/parquet.html
# MAGIC
# MAGIC #####Documentação Spark
# MAGIC https://spark.apache.org/docs/latest/sql-data-sources-parquet.html
# MAGIC
# MAGIC Pesquisar no google Parquet Documentação (databricks ou Spark)
# MAGIC

# COMMAND ----------

#Curiosidades comparado com CSV e Json
"""
80% (Aprox) menos armazenamento ao comparar com CSV e Json
30x (Aprox) Mais Rápido
90% (Aprox) Economia na leitura agiliza o cluster isso resulta em leituras e gravações mais rápidas.
Pode ser particionado
Quanto menor tamando de armazenamento menos dinheiro a empresa paga em recursos Cloud
Pesquise no google , comparação arquivo parquet com CSV 
"""

#Será que é isso tudo mesmo ? Vamos  ver na pratica

# COMMAND ----------

# MAGIC %md
# MAGIC ######Transformando DataFlame em Parquet
# MAGIC

# COMMAND ----------

display(dbutils.fs.ls("/Volumes/curso_databricks/aula/aula_volume/Anac"))

# COMMAND ----------

df = spark.read.json("/Volumes/curso_databricks/aula/aula_volume/Anac/V_OCORRENCIA_AMPLA.json")
display(df)

# COMMAND ----------

#Código em unica linha 
df.write.format("parquet").mode("overwrite").save("/Volumes/curso_databricks/aula/aula_volume/Anac/parquet")

# COMMAND ----------

df.write.format("parquet").mode("overwrite").option("compression", "gzip").save("/Volumes/curso_databricks/aula/aula_volume/Anac/parquet-zip")

# COMMAND ----------

# MAGIC %md
# MAGIC Comparação de tamanhos de arquivos

# COMMAND ----------

display(dbutils.fs.ls("/Volumes/curso_databricks/aula/aula_volume/Anac/parquet/"))

# COMMAND ----------

display(dbutils.fs.ls("/Volumes/curso_databricks/aula/aula_volume/Anac/parquet-zip/"))


# COMMAND ----------

#csv =     9869805  Bytes  9MB
#json=     20436383 Bytes  20MB
#parquet = 3308863  Bytes  3MB
#parquet compression = 2070130 Bytes  2MB

#Da para melhorar ainda mais?posso ser promovido por isso? pense em grande escala de economia 20 mil por mes ou 3 mil por mes qual melhor?

# COMMAND ----------

# MAGIC %md
# MAGIC ###### lendo arquivo Parquet

# COMMAND ----------

df_parquet=spark.read.parquet("/Volumes/curso_databricks/aula/aula_volume/Anac/parquet/")
df_parquet.display()

# COMMAND ----------

# MAGIC %md
# MAGIC Salvando parquet com Compactado

# COMMAND ----------

df_parquet_zip=(
    spark.read.format("parquet")
    .option("compression", "gzip")
    .load("/Volumes/curso_databricks/aula/aula_volume/Anac/parquet-zip/")
)
df_parquet_zip.display()
  

# COMMAND ----------

# da para melhorar?  ser promovidou ou conseguir uma oportunidade com esses conhecimentos a mais?