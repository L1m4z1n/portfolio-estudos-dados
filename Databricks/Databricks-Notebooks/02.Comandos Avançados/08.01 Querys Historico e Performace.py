# Databricks notebook source
# MAGIC %md
# MAGIC Você sabia que no Databricks, até um simples delete de arquivo aparece como uma "query" no histórico?
# MAGIC
# MAGIC Isso me te deixou curioso(a)? e a resposta é mais interessante do que parece.
# MAGIC
# MAGIC Quando rodei um `dbutils.fs.rm()` para apagar um arquivo em um Volume do Unity Catalog, o Databricks registrou a operação como uma consulta, com tempo de execução, start time e end time.
# MAGIC
# MAGIC **Mas por quê?**
# MAGIC
# MAGIC O Databricks instrumenta praticamente tudo que roda em um notebook — seja SQL, Python ou operação de sistema de arquivos — como um evento rastreável. Isso acontece por alguns motivos:
# MAGIC
# MAGIC - 📋 **Auditoria:** tudo fica registrado por usuário, cluster e horário
# MAGIC - 🔐 **Unity Catalog:** qualquer acesso a Volumes passa pela camada de governança
# MAGIC - 📊 **Interface unificada:** facilita monitorar o notebook inteiro em um só lugar
# MAGIC
# MAGIC No meu caso, os 0 bytes lidos/escritos e 0 rows confirmaram que não houve processamento Spark de verdade — foi só uma operação de filesystem registrada pelo sistema de auditoria.
# MAGIC
# MAGIC O Spark só otimiza com seu Catalyst Optimizer quando você trabalha com DataFrames, leituras de arquivos ou queries SQL. Um simples `dbutils.fs.rm()` não passa por esse motor.
# MAGIC
# MAGIC Pequeno detalhe, grande aprendizado. 🚀
# MAGIC
# MAGIC É esse tipo de curiosidade que transforma um engenheiro de dados em alguém que realmente entende a plataforma — não só usa.
# MAGIC
# MAGIC ---
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Acompanhe o histórico de queries para identificar:
# MAGIC - Operações que consomem mais tempo ou recursos
# MAGIC - Possíveis gargalos de performance
# MAGIC - Comportamento de operações administrativas (como deletes, renomeios, etc.)
# MAGIC
# MAGIC Entender o histórico é fundamental para otimizar e governar seu ambiente Databricks!

# COMMAND ----------

# MAGIC %md
# MAGIC E se você pudesse perguntar aos seus dados em linguagem natural, por exemplo:  
# MAGIC **"Quais foram as 5 queries que mais demoraram para rodar nos últimos 5 dias?"**
# MAGIC
# MAGIC Isso facilita a análise e torna o uso do Databricks ainda mais intuitivo!

# COMMAND ----------

# MAGIC %md
# MAGIC Vamos conhecer mais a tabela de 
# MAGIC FROM 
# MAGIC   `system`.`query`.`history`

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT `statement_id`, `executed_by`, `statement_text`, `total_duration_ms`, `start_time`, `end_time`
# MAGIC FROM `system`.`query`.`history`
# MAGIC WHERE `start_time` >= current_timestamp() - interval 5 days
# MAGIC ORDER BY `total_duration_ms` DESC
# MAGIC LIMIT 5

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select * from system.query.history limit 10

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from system.query.history 
# MAGIC where statement_type = 'DROP'

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC --Análise de performance das queries dos últimos 7 dias
# MAGIC SELECT
# MAGIC   DATE(start_time) as data_execucao,
# MAGIC   executed_by,
# MAGIC   client_application,
# MAGIC   execution_status,
# MAGIC   COUNT(*) as total_queries,
# MAGIC   ROUND(AVG(total_duration_ms) / 1000, 2) as tempo_medio_segundos,
# MAGIC   ROUND(MAX(total_duration_ms) / 1000, 2) as tempo_maximo_segundos,
# MAGIC   ROUND(AVG(read_bytes) / 1024 / 1024, 2) as mb_lidos_medio,
# MAGIC   SUM(
# MAGIC     CASE
# MAGIC       WHEN from_result_cache THEN 1
# MAGIC       ELSE 0
# MAGIC     END
# MAGIC   ) as queries_do_cache
# MAGIC FROM
# MAGIC   system.query.history
# MAGIC WHERE
# MAGIC   start_time >= CURRENT_DATE() - INTERVAL 7 DAYS
# MAGIC GROUP BY
# MAGIC   1,  2,  3,  4
# MAGIC ORDER BY
# MAGIC   1 DESC,  2
# MAGIC LIMIT 100;

# COMMAND ----------

# MAGIC %md
# MAGIC outras infos de sistema

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW SCHEMAS IN system

# COMMAND ----------

# MAGIC %sql
# MAGIC show tables in system.billing

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from system.billing.usage limit 10

# COMMAND ----------

