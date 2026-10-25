# Arquitetura

## Visão geral

```mermaid
flowchart TD
    A[Arquivos das Agências] --> B[Bronze]
    B --> C[Silver]
    C --> D[Gold]
    D --> E[Power BI]
    D --> F[Databricks Genie]
    E --> G[Power Apps]
    G --> H[Power Automate]
    H --> F
```

## Bronze
Preserva os arquivos de entrada com transformação mínima.

## Silver
Centraliza padronização, limpeza, regras e enriquecimento.

## Gold
Disponibiliza fatos, dimensões e auditoria prontos para consumo.

## Princípio principal
A lógica estrutural fica no Databricks; o Power BI atua como camada analítica.
