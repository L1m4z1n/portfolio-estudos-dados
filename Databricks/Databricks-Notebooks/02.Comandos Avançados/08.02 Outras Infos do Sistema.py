# Databricks notebook source
# MAGIC %md
# MAGIC outras infos de sistema
# MAGIC
# MAGIC
# MAGIC Databricks SQL
# MAGIC https://www.databricks.com/br/product/pricing/databricks-sql
# MAGIC
# MAGIC Preços do Azure Databricks
# MAGIC https://azure.microsoft.com/pt-br/pricing/details/databricks/
# MAGIC
# MAGIC Pricing calculator
# MAGIC https://www.databricks.com/br/product/pricing/product-pricing/instance-types
# MAGIC
# MAGIC
# MAGIC Preços de Máquinas Virtuais do Linux
# MAGIC https://azure.microsoft.com/pt-br/pricing/details/virtual-machines/linux/
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Diferença entre SQL Warehouse (Serverless), Cluster Compute e DBU no Databricks
# MAGIC
# MAGIC - **SQL Warehouse (Serverless)**: Serviço gerenciado do Databricks para execução de queries SQL, dashboards e BI, sem necessidade de gerenciar clusters. Recursos são alocados automaticamente conforme a demanda. Pagamento por uso, medido em DBUs/hora.
# MAGIC
# MAGIC - **Cluster Compute (Databricks)**: Conjunto de máquinas virtuais dedicadas para processamento de dados, notebooks, jobs e workloads Spark. Você gerencia o tamanho, tipo e tempo de vida do cluster. Pagamento por uso, também medido em DBUs/hora.
# MAGIC
# MAGIC - **Como são pagos**:
# MAGIC   - **SQL Warehouse (Serverless)**: Pagamento automático por uso (DBUs/hora), sem necessidade de provisionar ou gerenciar infraestrutura.
# MAGIC   - **Cluster Compute**: Pagamento por uso (DBUs/hora), conforme o tipo e tamanho do cluster criado.
# MAGIC
# MAGIC - **O que é DBU?**
# MAGIC   - **DBU (Databricks Unit)**: Unidade de cobrança do Databricks baseada no consumo de recursos computacionais (CPU, RAM, tipo de workload) por hora. O valor em $/DBU varia conforme o tipo de cluster ou serviço utilizado.

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

# DBTITLE 1,📚 Guia Completo: System Tables do Databricks
# MAGIC %md
# MAGIC # 📚 Guia Completo: System Tables do Databricks
# MAGIC
# MAGIC O **System Catalog** (`system`) é um catálogo especial do Unity Catalog que fornece visibilidade completa sobre:
# MAGIC - 💰 **Custos e Billing**
# MAGIC - 🔍 **Auditoria e Compliance**
# MAGIC - ⚡ **Performance e Query Optimization**
# MAGIC - 🖥️ **Recursos Computacionais**
# MAGIC - 🤖 **Machine Learning e AI**
# MAGIC - 🔄 **Pipelines e Jobs**
# MAGIC - 📊 **Linhagem de Dados**
# MAGIC
# MAGIC Este guia cobre **todos os 11 schemas** disponíveis com exemplos práticos de uso!
# MAGIC
# MAGIC ---

# COMMAND ----------

# DBTITLE 1,1️⃣ SYSTEM.BILLING - Gestão de Custos
# MAGIC %md
# MAGIC ## 1️⃣ SYSTEM.BILLING - Gestão de Custos 💰
# MAGIC
# MAGIC ### Tabelas Disponíveis:
# MAGIC * `system.billing.usage` - Consumo detalhado de DBUs
# MAGIC * `system.billing.list_prices` - Preços oficiais por SKU
# MAGIC * `system.billing.account_prices` - Preços específicos da sua conta
# MAGIC
# MAGIC ### 📋 Significado:
# MAGIC Monitore e otimize custos do Databricks com dados granulares de consumo por workspace, cluster, usuário, SKU e tipo de workload.
# MAGIC
# MAGIC ### ✅ Casos de Uso:
# MAGIC 1. **Análise de custo por departamento/projeto**
# MAGIC 2. **Identificar recursos mais caros**
# MAGIC 3. **Criar alertas de budget**
# MAGIC 4. **Chargeback interno**
# MAGIC 5. **Projeção de custos futuros**

# COMMAND ----------

# DBTITLE 1,Exemplo: Top 10 workloads mais caros (últimos 30 dias)
# MAGIC %sql
# MAGIC -- Análise de custo dos últimos 30 dias
# MAGIC SELECT 
# MAGIC   u.workspace_id,
# MAGIC   u.usage_metadata.cluster_id,
# MAGIC   u.sku_name,
# MAGIC   ROUND(SUM(u.usage_quantity), 2) as total_dbus
# MAGIC FROM 
# MAGIC   system.billing.usage u
# MAGIC WHERE 
# MAGIC   u.usage_date >= CURRENT_DATE() - INTERVAL 30 DAYS
# MAGIC GROUP BY 1, 2, 3
# MAGIC ORDER BY total_dbus DESC
# MAGIC LIMIT 10;

# COMMAND ----------

# DBTITLE 1,2️⃣ SYSTEM.ACCESS - Auditoria e Governança
# MAGIC %md
# MAGIC ## 2️⃣ SYSTEM.ACCESS - Auditoria e Governança 🔐
# MAGIC
# MAGIC ### Tabelas Disponíveis:
# MAGIC * `system.access.audit` - Log completo de todas as ações no workspace
# MAGIC * `system.access.table_lineage` - Linhagem de tabelas (origem → destino)
# MAGIC * `system.access.column_lineage` - Linhagem em nível de coluna
# MAGIC * `system.access.assistant_events` - Interações com AI Assistant
# MAGIC * `system.access.clean_room_events` - Eventos de Clean Rooms
# MAGIC * `system.access.outbound_network` - Conexões externas do workspace
# MAGIC
# MAGIC ### 📋 Significado:
# MAGIC Rastreie **TUDO** que acontece no workspace: quem acessou, criou, modificou ou deletou dados, tabelas, notebooks, jobs, etc.
# MAGIC
# MAGIC ### ✅ Casos de Uso:
# MAGIC 1. **Compliance e LGPD/GDPR**
# MAGIC 2. **Investigar incidentes de segurança**
# MAGIC 3. **Auditoria de acessos a dados sensíveis**
# MAGIC 4. **Rastreamento de linhagem completa (data lineage)**
# MAGIC 5. **Identificar tabelas órfãs ou não utilizadas**

# COMMAND ----------

# DBTITLE 1,Exemplo: Quem acessou tabelas com dados sensíveis (últimos 7 dias)
# MAGIC %sql
# MAGIC -- Auditoria de acesso a tabelas sensíveis
# MAGIC SELECT 
# MAGIC   event_date,
# MAGIC   user_identity.email as usuario,
# MAGIC   action_name,
# MAGIC   request_params.full_name_arg as tabela_acessada,
# MAGIC   request_params.operation as tipo_operacao
# MAGIC FROM 
# MAGIC   system.access.audit
# MAGIC WHERE 
# MAGIC   event_date >= CURRENT_DATE() - INTERVAL 7 DAYS
# MAGIC   AND action_name IN ('getTable', 'readTable', 'createTable', 'deleteTable')
# MAGIC   AND request_params.full_name_arg LIKE '%pii%' -- tabelas com dados sensíveis
# MAGIC ORDER BY event_date DESC
# MAGIC LIMIT 100;

# COMMAND ----------

# DBTITLE 1,Exemplo: Mapeamento de linhagem de dados
# MAGIC %sql
# MAGIC -- Descobrir origem e destino de uma tabela específica
# MAGIC SELECT 
# MAGIC   source_table_full_name as tabela_origem,
# MAGIC   target_table_full_name as tabela_destino,
# MAGIC   source_type,
# MAGIC   target_type,
# MAGIC   event_time
# MAGIC FROM 
# MAGIC   system.access.table_lineage
# MAGIC WHERE 
# MAGIC   target_table_full_name = 'catalog.schema.minha_tabela'
# MAGIC ORDER BY event_time DESC
# MAGIC LIMIT 50;

# COMMAND ----------

# DBTITLE 1,3️⃣ SYSTEM.QUERY - Histórico e Performance de Queries
# MAGIC %md
# MAGIC ## 3️⃣ SYSTEM.QUERY - Histórico e Performance 🚀
# MAGIC
# MAGIC ### Tabelas Disponíveis:
# MAGIC * `system.query.history` - Histórico completo de todas as queries executadas
# MAGIC
# MAGIC ### 📋 Significado:
# MAGIC Como você já viu neste notebook, esta tabela registra **TODAS** as queries executadas (SQL, notebooks, dashboards, jobs) com métricas detalhadas de performance.
# MAGIC
# MAGIC ### ✅ Casos de Uso:
# MAGIC 1. **Identificar queries lentas (bottlenecks)**
# MAGIC 2. **Análise de uso do cache**
# MAGIC 3. **Otimização de performance**
# MAGIC 4. **Troubleshooting de falhas**
# MAGIC 5. **Monitoramento de SLAs**

# COMMAND ----------

# DBTITLE 1,Exemplo: Queries com pior performance (últimos 7 dias)
# MAGIC %sql
# MAGIC -- Top 20 queries mais lentas com detalhes de otimização
# MAGIC SELECT 
# MAGIC   statement_id,
# MAGIC   executed_by,
# MAGIC   SUBSTRING(statement_text, 1, 100) as query_preview,
# MAGIC   ROUND(total_duration_ms / 1000, 2) as tempo_segundos,
# MAGIC   ROUND(read_bytes / 1024 / 1024, 2) as mb_lidos,
# MAGIC   produced_rows,
# MAGIC   from_result_cache,
# MAGIC   execution_status,
# MAGIC   error_message,
# MAGIC   start_time
# MAGIC FROM 
# MAGIC   system.query.history
# MAGIC WHERE 
# MAGIC   start_time >= CURRENT_DATE() - INTERVAL 7 DAYS
# MAGIC   AND execution_status = 'FINISHED'
# MAGIC   AND total_duration_ms > 10000 -- queries > 10 segundos
# MAGIC ORDER BY total_duration_ms DESC
# MAGIC LIMIT 20;

# COMMAND ----------

# DBTITLE 1,4️⃣ SYSTEM.COMPUTE - Recursos Computacionais
# MAGIC %md
# MAGIC ## 4️⃣ SYSTEM.COMPUTE - Recursos Computacionais 🖥️
# MAGIC
# MAGIC ### Tabelas Disponíveis:
# MAGIC * `system.compute.clusters` - Informações de todos os clusters
# MAGIC * `system.compute.warehouses` - SQL Warehouses configurados
# MAGIC * `system.compute.warehouse_events` - Eventos de warehouse (start, stop, scale)
# MAGIC * `system.compute.node_timeline` - Timeline de utilização de nós
# MAGIC * `system.compute.node_types` - Tipos de instâncias disponíveis
# MAGIC
# MAGIC ### 📋 Significado:
# MAGIC Monitore clusters, SQL warehouses e recursos computacionais: configuração, estado, eventos de lifecycle e custos associados.
# MAGIC
# MAGIC ### ✅ Casos de Uso:
# MAGIC 1. **Otimizar tamanho de clusters**
# MAGIC 2. **Identificar clusters ociosos**
# MAGIC 3. **Monitorar autoscaling**
# MAGIC 4. **Análise de uptime vs downtime**
# MAGIC 5. **Planejamento de capacidade**

# COMMAND ----------

# DBTITLE 1,Exemplo: Clusters ativos e seu custo estimado
# MAGIC %sql
# MAGIC -- Análise de clusters e custos
# MAGIC SELECT 
# MAGIC   cluster_id,
# MAGIC   cluster_name,
# MAGIC   driver_node_type,
# MAGIC   worker_node_type,
# MAGIC   worker_count,
# MAGIC   min_autoscale_workers,
# MAGIC   max_autoscale_workers,
# MAGIC   owned_by,
# MAGIC   create_time,
# MAGIC   DATEDIFF(hour, create_time, CURRENT_TIMESTAMP()) as horas_uptime
# MAGIC FROM 
# MAGIC   system.compute.clusters
# MAGIC WHERE 
# MAGIC   delete_time IS NULL
# MAGIC ORDER BY create_time DESC;

# COMMAND ----------

# DBTITLE 1,Exemplo: Análise de eventos de SQL Warehouse
# MAGIC %sql
# MAGIC -- Monitorar starts/stops de SQL Warehouse
# MAGIC SELECT 
# MAGIC   warehouse_id,
# MAGIC   event_type,
# MAGIC   event_time,
# MAGIC   cluster_count
# MAGIC FROM 
# MAGIC   system.compute.warehouse_events
# MAGIC WHERE 
# MAGIC   event_time >= CURRENT_DATE() - INTERVAL 7 DAYS
# MAGIC ORDER BY event_time DESC
# MAGIC LIMIT 100;

# COMMAND ----------

# DBTITLE 1,5️⃣ SYSTEM.LAKEFLOW - Jobs e Pipelines
# MAGIC %md
# MAGIC ## 5️⃣ SYSTEM.LAKEFLOW - Jobs e Pipelines 🔄
# MAGIC
# MAGIC ### Tabelas Disponíveis:
# MAGIC * `system.lakeflow.jobs` - Configuração de todos os jobs
# MAGIC * `system.lakeflow.job_run_timeline` - Histórico de execuções de jobs
# MAGIC * `system.lakeflow.job_tasks` - Tasks individuais dos jobs
# MAGIC * `system.lakeflow.job_task_run_timeline` - Timeline de tasks
# MAGIC * `system.lakeflow.pipelines` - Pipelines (Spark Declarative)
# MAGIC
# MAGIC ### 📋 Significado:
# MAGIC Monitore orquestração de workflows: jobs, tasks, pipelines e seus históricos de execução, falhas e durações.
# MAGIC
# MAGIC ### ✅ Casos de Uso:
# MAGIC 1. **Monitorar SLA de jobs críticos**
# MAGIC 2. **Identificar jobs com falhas recorrentes**
# MAGIC 3. **Análise de duração de tasks**
# MAGIC 4. **Otimização de pipelines ETL**
# MAGIC 5. **Alertas de falha em produção**

# COMMAND ----------

# DBTITLE 1,Exemplo: Jobs com falhas nos últimos 7 dias
# MAGIC %sql
# MAGIC SELECT 
# MAGIC   j.job_id,
# MAGIC   j.name as job_name,
# MAGIC   j.creator_user_name as created_by,
# MAGIC   jrt.run_id,
# MAGIC   jrt.result_state,
# MAGIC   jrt.termination_code as state_message,
# MAGIC   jrt.error_message,
# MAGIC   jrt.period_start_time as start_time,
# MAGIC   jrt.period_end_time as end_time,
# MAGIC   ROUND((unix_timestamp(jrt.period_end_time) - unix_timestamp(jrt.period_start_time)) / 60, 2) as duracao_minutos
# MAGIC FROM 
# MAGIC   system.lakeflow.jobs j
# MAGIC   INNER JOIN system.lakeflow.job_run_timeline jrt 
# MAGIC     ON j.job_id = jrt.job_id 
# MAGIC     AND j.workspace_id = jrt.workspace_id
# MAGIC WHERE 
# MAGIC   jrt.period_start_time >= CURRENT_DATE() - INTERVAL 7 DAYS
# MAGIC   AND jrt.result_state IN ('FAILED', 'TIMED_OUT', 'CANCELED')
# MAGIC ORDER BY jrt.period_start_time DESC
# MAGIC LIMIT 50

# COMMAND ----------

# DBTITLE 1,6️⃣ SYSTEM.MLFLOW - Machine Learning
# MAGIC %md
# MAGIC ## 6️⃣ SYSTEM.MLFLOW - Machine Learning 🤖
# MAGIC
# MAGIC ### Tabelas Disponíveis:
# MAGIC * `system.mlflow.experiments_latest` - Experimentos de ML
# MAGIC * `system.mlflow.runs_latest` - Runs (execuções) de treinamento
# MAGIC * `system.mlflow.run_metrics_history` - Métricas ao longo do tempo
# MAGIC
# MAGIC ### 📋 Significado:
# MAGIC Rastreie experimentos de Machine Learning: modelos treinados, métricas (accuracy, loss, etc.), parâmetros e artifacts.
# MAGIC
# MAGIC ### ✅ Casos de Uso:
# MAGIC 1. **Comparar performance de modelos**
# MAGIC 2. **Rastrear evolução de métricas**
# MAGIC 3. **Governança de modelos em produção**
# MAGIC 4. **Auditoria de treinamentos**
# MAGIC 5. **Identificar melhores hiperparâmetros**

# COMMAND ----------

# DBTITLE 1,Exemplo: Top 10 modelos por accuracy
# MAGIC %sql
# MAGIC -- Melhores modelos por accuracy
# MAGIC SELECT 
# MAGIC   r.experiment_id,
# MAGIC   e.name as experiment_name,
# MAGIC   r.run_id,
# MAGIC   r.run_name,
# MAGIC   r.created_by as user_id,
# MAGIC   m.metric_name as metrica,
# MAGIC   m.metric_value as valor_metrica,
# MAGIC   r.start_time,
# MAGIC   r.status
# MAGIC FROM 
# MAGIC   system.mlflow.runs_latest r
# MAGIC   INNER JOIN system.mlflow.experiments_latest e ON r.experiment_id = e.experiment_id
# MAGIC   INNER JOIN system.mlflow.run_metrics_history m ON r.run_id = m.run_id
# MAGIC WHERE 
# MAGIC   m.metric_name = 'accuracy'
# MAGIC   AND r.status = 'FINISHED'
# MAGIC ORDER BY m.metric_value DESC
# MAGIC LIMIT 10;

# COMMAND ----------

# DBTITLE 1,7️⃣ SYSTEM.SERVING - Model Serving
# MAGIC %md
# MAGIC ## 7️⃣ SYSTEM.SERVING - Model Serving 🌐
# MAGIC
# MAGIC ### Tabelas Disponíveis:
# MAGIC * `system.serving.endpoint_usage` - Uso de endpoints de modelos
# MAGIC * `system.serving.served_entities` - Modelos servidos em produção
# MAGIC
# MAGIC ### 📋 Significado:
# MAGIC Monitore endpoints de modelos em produção: requisições, latência, throughput e versões deployadas.
# MAGIC
# MAGIC ### ✅ Casos de Uso:
# MAGIC 1. **Monitorar latência de inferência**
# MAGIC 2. **Análise de volume de requisições**
# MAGIC 3. **Identificar modelos subutilizados**
# MAGIC 4. **Alertas de degradação de performance**
# MAGIC 5. **Planejamento de scaling**

# COMMAND ----------

# DBTITLE 1,Exemplo: Análise de uso de endpoints
-- Uso de endpoints nos últimos 7 dias
SELECT 
  se.endpoint_id,
  se.endpoint_name,
  DATE(eu.request_time) as data,
  COUNT(*) as total_requisicoes,
  ROUND(AVG(eu.usage_context['latency_ms']), 2) as latencia_media_ms,
  ROUND(MAX(eu.usage_context['latency_ms']), 2) as latencia_maxima_ms,
  SUM(CASE WHEN eu.status_code >= 400 THEN 1 ELSE 0 END) as erros
FROM 
  system.serving.endpoint_usage eu
  LEFT JOIN system.serving.served_entities se
    ON eu.served_entity_id = se.served_entity_id
WHERE 
  eu.request_time >= CURRENT_DATE() - INTERVAL 7 DAYS
GROUP BY 1, 2, 3
ORDER BY 3 DESC, 4 DESC;

# COMMAND ----------

# DBTITLE 1,8️⃣ SYSTEM.AI_GATEWAY - GenAI & LLMs
# MAGIC %md
# MAGIC ## 8️⃣ SYSTEM.AI_GATEWAY - GenAI & LLMs 🧠
# MAGIC
# MAGIC ### Tabelas Disponíveis:
# MAGIC * `system.ai_gateway.usage` - Uso de AI Gateway (LLMs externos)
# MAGIC
# MAGIC ### 📋 Significado:
# MAGIC Rastreie chamadas a modelos de linguagem (OpenAI, Anthropic, etc.) através do AI Gateway: tokens consumidos, custos, latência.
# MAGIC
# MAGIC ### ✅ Casos de Uso:
# MAGIC 1. **Controlar custos de APIs de LLM**
# MAGIC 2. **Monitorar consumo de tokens**
# MAGIC 3. **Análise de latência de inferência**
# MAGIC 4. **Auditoria de uso por usuário/app**
# MAGIC 5. **Otimizar prompts (reduzir tokens)**

# COMMAND ----------

# DBTITLE 1,Exemplo: Consumo de tokens por modelo
# MAGIC %sql
# MAGIC -- Análise de uso de LLMs
# MAGIC SELECT 
# MAGIC   DATE(event_time) as data,
# MAGIC   endpoint_name,
# MAGIC   destination_model,
# MAGIC   COUNT(*) as total_requests,
# MAGIC   SUM(input_tokens) as tokens_input,
# MAGIC   SUM(output_tokens) as tokens_output,
# MAGIC   SUM(total_tokens) as tokens_totais,
# MAGIC   ROUND(AVG(latency_ms), 2) as latencia_media_ms
# MAGIC FROM 
# MAGIC   system.ai_gateway.usage
# MAGIC WHERE 
# MAGIC   event_time >= CURRENT_DATE() - INTERVAL 30 DAYS
# MAGIC GROUP BY 1, 2, 3
# MAGIC ORDER BY 1 DESC, tokens_totais DESC;

# COMMAND ----------

# DBTITLE 1,9️⃣ SYSTEM.STORAGE - Otimização de Armazenamento
# MAGIC %md
# MAGIC ## 9️⃣ SYSTEM.STORAGE - Otimização de Armazenamento 💾
# MAGIC
# MAGIC ### Tabelas Disponíveis:
# MAGIC * `system.storage.predictive_optimization_operations_history` - Histórico de otimizações automáticas
# MAGIC
# MAGIC ### 📋 Significado:
# MAGIC Rastreie operações de Predictive Optimization (auto-compaction, auto-clustering, etc.) que o Databricks executa automaticamente nas suas tabelas.
# MAGIC
# MAGIC ### ✅ Casos de Uso:
# MAGIC 1. **Verificar otimizações automáticas**
# MAGIC 2. **Monitorar redução de arquivos pequenos**
# MAGIC 3. **Avaliar impacto de clustering**
# MAGIC 4. **Troubleshoot problemas de performance**
# MAGIC 5. **Entender overhead de manutenção**

# COMMAND ----------

# DBTITLE 1,Exemplo: Otimizações executadas nos últimos 7 dias
# MAGIC %sql
# MAGIC -- Histórico de Predictive Optimization
# MAGIC SELECT 
# MAGIC   catalog_name as table_catalog,
# MAGIC   schema_name as table_schema,
# MAGIC   table_name,
# MAGIC   operation_type,
# MAGIC   operation_status,
# MAGIC   start_time,
# MAGIC   end_time,
# MAGIC   operation_metrics['num_files_added'] as files_added,
# MAGIC   operation_metrics['num_files_removed'] as files_removed,
# MAGIC   ROUND((unix_timestamp(end_time) - unix_timestamp(start_time)) / 60, 2) as duracao_minutos
# MAGIC FROM 
# MAGIC   system.storage.predictive_optimization_operations_history
# MAGIC WHERE 
# MAGIC   start_time >= CURRENT_DATE() - INTERVAL 7 DAYS
# MAGIC ORDER BY start_time DESC
# MAGIC LIMIT 50;

# COMMAND ----------

# DBTITLE 1,🔟 SYSTEM.AI - AI Assistant
# MAGIC %md
# MAGIC ## 🔟 SYSTEM.AI - AI Assistant (Schema vazio no momento)
# MAGIC
# MAGIC ### Tabelas Disponíveis:
# MAGIC Atualmente não há tabelas públicas neste schema.
# MAGIC
# MAGIC ### 📋 Significado:
# MAGIC Reservado para funcionalidades futuras relacionadas ao AI Assistant do Databricks.
# MAGIC
# MAGIC ---

# COMMAND ----------

# DBTITLE 1,1️⃣1️⃣ SYSTEM.INFORMATION_SCHEMA - Metadados do Unity Catalog
# MAGIC %md
# MAGIC ## 1️⃣1️⃣ SYSTEM.INFORMATION_SCHEMA - Metadados do Unity Catalog 📋
# MAGIC
# MAGIC ### Significado:
# MAGIC Segue o padrão ANSI SQL para metadados. Contém informações sobre:
# MAGIC * Catálogos, schemas e tabelas
# MAGIC * Colunas e tipos de dados
# MAGIC * Views e funções
# MAGIC * Permissões e grants
# MAGIC
# MAGIC ### ✅ Casos de Uso:
# MAGIC 1. **Descoberta de dados (data discovery)**
# MAGIC 2. **Documentação automática de schemas**
# MAGIC 3. **Auditoria de permissões**
# MAGIC 4. **Governança de metadados**
# MAGIC 5. **Inventário de objetos do Unity Catalog**

# COMMAND ----------

# DBTITLE 1,Exemplo: Inventário de tabelas em um catálogo
# MAGIC %sql
# MAGIC -- Listar todas as tabelas de um catálogo específico
# MAGIC SELECT 
# MAGIC   table_catalog,
# MAGIC   table_schema,
# MAGIC   table_name,
# MAGIC   table_type,
# MAGIC   comment
# MAGIC FROM 
# MAGIC   system.information_schema.tables
# MAGIC WHERE 
# MAGIC   table_catalog = 'curso_databricks'
# MAGIC ORDER BY table_schema, table_name;

# COMMAND ----------

# DBTITLE 1,📊 Resumo: Quando Usar Cada Schema
# MAGIC %md
# MAGIC ## 📊 Resumo: Quando Usar Cada Schema
# MAGIC
# MAGIC | Schema | Use quando precisar... |
# MAGIC |--------|------------------------|
# MAGIC | **billing** | 💰 Analisar custos, DBUs consumidos, chargeback |
# MAGIC | **access** | 🔐 Auditoria, compliance, linhagem de dados, segurança |
# MAGIC | **query** | 🚀 Otimizar performance, identificar queries lentas |
# MAGIC | **compute** | 🖥️ Monitorar clusters, warehouses, recursos computacionais |
# MAGIC | **lakeflow** | 🔄 Acompanhar jobs, pipelines, orquestração de workflows |
# MAGIC | **mlflow** | 🤖 Rastrear experimentos de ML, comparar modelos |
# MAGIC | **serving** | 🌐 Monitorar endpoints de modelos em produção |
# MAGIC | **ai_gateway** | 🧠 Controlar custos de LLMs, tokens consumidos |
# MAGIC | **storage** | 💾 Verificar otimizações automáticas de tabelas |
# MAGIC | **information_schema** | 📋 Descoberta de metadados, inventário do Unity Catalog |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🎯 Dica Final:
# MAGIC Combine múltiplos schemas em uma única análise!
# MAGIC
# MAGIC **Exemplo:** Cruzar `system.query.history` (performance) com `system.billing.usage` (custos) para identificar queries caras e lentas.

# COMMAND ----------

# DBTITLE 1,BÔNUS: Query cross-schema (Performance + Custo)
# MAGIC %sql
# MAGIC -- Combinar dados de query history + billing para análise completa
# MAGIC WITH queries_lentas AS (
# MAGIC   SELECT 
# MAGIC     statement_id,
# MAGIC     executed_by,
# MAGIC     compute.warehouse_id as warehouse_id,
# MAGIC     total_duration_ms,
# MAGIC     read_bytes,
# MAGIC     DATE(start_time) as data_execucao
# MAGIC   FROM system.query.history
# MAGIC   WHERE 
# MAGIC     start_time >= CURRENT_DATE() - INTERVAL 7 DAYS
# MAGIC     AND total_duration_ms > 30000 -- > 30 segundos
# MAGIC ),
# MAGIC custos AS (
# MAGIC   SELECT 
# MAGIC     usage_date,
# MAGIC     usage_metadata.warehouse_id as warehouse_id,
# MAGIC     SUM(usage_quantity) as dbus_consumidos
# MAGIC   FROM system.billing.usage
# MAGIC   WHERE usage_date >= CURRENT_DATE() - INTERVAL 7 DAYS
# MAGIC     AND usage_metadata.warehouse_id IS NOT NULL
# MAGIC     AND usage_unit = 'DBU'
# MAGIC   GROUP BY 1, 2
# MAGIC )
# MAGIC SELECT 
# MAGIC   q.statement_id,
# MAGIC   q.executed_by,
# MAGIC   q.warehouse_id,
# MAGIC   ROUND(q.total_duration_ms / 1000, 2) as tempo_segundos,
# MAGIC   ROUND(q.read_bytes / 1024 / 1024, 2) as mb_lidos,
# MAGIC   c.dbus_consumidos,
# MAGIC   q.data_execucao
# MAGIC FROM queries_lentas q
# MAGIC LEFT JOIN custos c 
# MAGIC   ON q.data_execucao = c.usage_date 
# MAGIC   AND q.warehouse_id = c.warehouse_id
# MAGIC ORDER BY q.total_duration_ms DESC
# MAGIC LIMIT 20;