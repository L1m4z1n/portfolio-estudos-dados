# Databricks notebook source
# MAGIC %md
# MAGIC ######Sistema interno de arquivo
# MAGIC https://learn.microsoft.com/pt-br/azure/databricks/files/
# MAGIC
# MAGIC
# MAGIC ######O que são volumes?
# MAGIC https://learn.microsoft.com/pt-br/azure/databricks/files/volumes

# COMMAND ----------

# MAGIC %md
# MAGIC ######Teste MarkDown

# COMMAND ----------

# MAGIC %md
# MAGIC teste
# MAGIC
# MAGIC #teste
# MAGIC
# MAGIC ##teste
# MAGIC
# MAGIC ####teste

# COMMAND ----------

# DBTITLE 1,teste inicial
# obs

# COMMAND ----------

# MAGIC %sql
# MAGIC -- sql

# COMMAND ----------

'''
o meu texto 
ou obs

'''

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

# MAGIC %md
# MAGIC #comando mágico sql e fs

# COMMAND ----------

# MAGIC %md
# MAGIC #####%sql list

# COMMAND ----------

# MAGIC %sql
# MAGIC list '/Volumes/curso_databricks/aula/aula_volume'

# COMMAND ----------

# MAGIC %sql
# MAGIC list '/Volumes/curso_databricks/aula/aula_volume/Bike Store/'

# COMMAND ----------

# MAGIC %md
# MAGIC #####%fs

# COMMAND ----------

# MAGIC %fs
# MAGIC ls /Volumes/curso_databricks/aula/aula_volume

# COMMAND ----------

# MAGIC %fs
# MAGIC ls 'dbfs:/Volumes/curso_databricks/aula/aula_volume/Bike Store/'

# COMMAND ----------

# MAGIC %fs
# MAGIC ls '/Volumes/curso_databricks/aula/aula_volume/Bike Store/'

# COMMAND ----------

# MAGIC %md
# MAGIC ######Criando nova pasta 

# COMMAND ----------

# MAGIC %fs
# MAGIC ls '/Volumes/curso_databricks/aula/aula_volume/'

# COMMAND ----------

# MAGIC %fs
# MAGIC mkdirs '/Volumes/curso_databricks/aula/aula_volume/Bike Store2/'

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Vendo nova Pasta 

# COMMAND ----------

# MAGIC %fs
# MAGIC ls '/Volumes/curso_databricks/aula/aula_volume/Bike Store2/'

# COMMAND ----------

# MAGIC %md
# MAGIC ######Copiando Arquivo de uma pasta 

# COMMAND ----------

# MAGIC %fs
# MAGIC ls '/Volumes/curso_databricks/aula/aula_volume/Bike Store/'

# COMMAND ----------

# MAGIC %fs
# MAGIC cp '/Volumes/curso_databricks/aula/aula_volume/Bike Store/categories.csv' '/Volumes/curso_databricks/aula/aula_volume/Bike Store3/categories.csv'

# COMMAND ----------

# MAGIC %fs
# MAGIC cp '/Volumes/curso_databricks/aula/aula_volume/Bike Store/categories.csv' '/Volumes/curso_databricks/aula/aula_volume/Bike Store3/categories_rename.csv'

# COMMAND ----------

# MAGIC %fs
# MAGIC ls '/Volumes/curso_databricks/aula/aula_volume/Bike Store3/'

# COMMAND ----------

# MAGIC %md
# MAGIC ######Copiando pasta inteira
# MAGIC #######O parâmetro -r indica que a cópia será recursiva, ou seja, todos os arquivos e subpastas dentro da pasta serão copiados.

# COMMAND ----------

# MAGIC %fs
# MAGIC ls '/Volumes/curso_databricks/aula/aula_volume/Bike Store/'

# COMMAND ----------

# MAGIC %fs
# MAGIC cp -r '/Volumes/curso_databricks/aula/aula_volume/Bike Store/' '/Volumes/curso_databricks/aula/aula_volume/Bike Store6/' 

# COMMAND ----------

# MAGIC %fs
# MAGIC ls '/Volumes/curso_databricks/aula/aula_volume/'

# COMMAND ----------

dbutils.fs.cp('/Volumes/curso_databricks/aula/aula_volume/Bike Store/','/Volumes/curso_databricks/aula/aula_volume/Bike Store7/', recurse=True )


# COMMAND ----------

# MAGIC %fs
# MAGIC ls '/Volumes/curso_databricks/aula/aula_volume/Bike Store7/'

# COMMAND ----------

# MAGIC %md
# MAGIC ######Renomeando arquivo
# MAGIC ######usar metodo mv, mover para mesma pasta com outro nome 
# MAGIC

# COMMAND ----------

# MAGIC %fs
# MAGIC mv '/Volumes/curso_databricks/aula/aula_volume/Bike Store7/categories.csv' '/Volumes/curso_databricks/aula/aula_volume/Bike Store7/categories_renamed.csv'

# COMMAND ----------

# MAGIC %md
# MAGIC ######Deletando Pasta Bike_Store extras deixando somente a primeira OFICIAL

# COMMAND ----------

# MAGIC %fs
# MAGIC ls '/Volumes/curso_databricks/aula/aula_volume/'

# COMMAND ----------

# MAGIC %fs
# MAGIC rm '/Volumes/curso_databricks/aula/aula_volume/Bike Store2/'

# COMMAND ----------

# MAGIC %fs
# MAGIC rm -r '/Volumes/curso_databricks/aula/aula_volume/Bike Store3/'

# COMMAND ----------

dbutils.fs.rm('/Volumes/curso_databricks/aula/aula_volume/Bike Store6/', recurse=True)
dbutils.fs.rm('/Volumes/curso_databricks/aula/aula_volume/Bike Store7/', recurse=True)