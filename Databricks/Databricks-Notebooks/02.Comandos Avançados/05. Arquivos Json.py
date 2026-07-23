# Databricks notebook source
# MAGIC %md
# MAGIC #####Sites
# MAGIC https://jsonviewer.stack.hu/
# MAGIC
# MAGIC https://codebeautify.org/jsonviewer
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC #####Ler um arquivo json
# MAGIC https://spark.apache.org/docs/latest/sql-data-sources-json.html

# COMMAND ----------

df = spark.read.json("/Volumes/curso_databricks/aula/aula_volume/Anac/V_OCORRENCIA_AMPLA.json")
display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Renomear Colunas

# COMMAND ----------

 df=(df
     .withColumnRenamed("Aerodromo_de_Destino","Destino")
    .withColumnRenamed("Aerodromo_de_Origem","Origem")
    .withColumnRenamed("Classificacao_da_Ocorrência","Classificacao") 
    
    )
 df.display()

# COMMAND ----------

 # Read = Ler de algum lugar (Arquivo, tabela e etc)
 # write = Escrever\Gravar  Salvar em algum lugar (Arquivo, tabela e etc)


# COMMAND ----------

# MAGIC %md
# MAGIC #####Salvar arquivo json zipado

# COMMAND ----------

(df.write
 .format("json")
 .option("compression", "gzip")
 .mode("overwrite")
 .save("/Volumes/curso_databricks/aula/aula_volume/Anac_json")

)

# COMMAND ----------

display(dbutils.fs.ls("/Volumes/curso_databricks/aula/aula_volume/Anac_json"))

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Lendo Json Compactado

# COMMAND ----------

df_json = spark.read.json("/Volumes/curso_databricks/aula/aula_volume/Anac_json")
display(df_json)

# COMMAND ----------

#ler com a option compression 
df_json_compression = (spark.read
                       .format("json")
                       .option("compression","gzip")
                       .load("/Volumes/curso_databricks/aula/aula_volume/Anac_json"))
display(df_json_compression)