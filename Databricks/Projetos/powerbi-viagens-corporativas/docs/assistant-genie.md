# Assistente + Databricks Genie

## Fluxo

```text
Power BI
↓
Power Apps
↓
Power Automate
↓
Databricks Genie API
↓
Gold
```

## Continuidade

O `conversation_id` permite manter o contexto entre perguntas.

```text
Quanto foi gasto com passagens?
→ R$ 64.664,95

E por diretoria?
→ continua a análise anterior
```

## Filtros

O contexto atual do Power BI é adicionado à pergunta antes de chamar o Genie.

## Segurança

Nunca versionar tokens, PATs, secrets ou credenciais.
