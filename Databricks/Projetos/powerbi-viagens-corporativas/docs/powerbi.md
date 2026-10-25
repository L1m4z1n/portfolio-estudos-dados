# Power BI

## Páginas

1. Visão Geral
2. Passagens e Justificativas
3. Hospedagem
4. Uber e Diárias
5. Diretoria e Centro de Custo
6. Auditoria, Qualidade e IA

## Organização das medidas

```text
00_Medidas
01_passagens
02_Medidas_Hospedagens
03_Medidas_Uber
04_Medidas_Diarias
05_Medidas_Justificativas
06_Medidas_Diretoria_CC
07_Medidas_Auditoria_IA
```

## Boas práticas

- medidas separadas por domínio;
- dimensões compartilhadas;
- relacionamento 1:N;
- direção dimensão → fato;
- evitar relacionamento fato → fato;
- padronização visual entre páginas.

## Contexto enviado ao Power Apps

```text
Contexto Ano
Contexto Mês
Contexto Trimestre
Contexto Diretoria
Contexto Centro de Custo
Contexto Agência
```
