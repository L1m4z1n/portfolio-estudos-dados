# Medidas DAX

Principais medidas usadas no projeto.

- Valor Total
- Valor Aéreo
- Valor Hospedagem
- Valor Uber
- Viagens Fora do Prazo
- Quantidade Cancelados
- Quantidade Não Voados

---

## 1. Indicadores gerais

### Valor Total

Soma o valor total das despesas consolidadas na tabela `Base_Geral`.

```DAX
Valor Total =
SUM(Base_Geral[Valor])
```

#### Uso no dashboard
- Card de gasto total
- Gráficos por diretoria
- Gráficos por tipo de despesa
- Análises por trimestre

### Quantidade de Viagens

Conta a quantidade de registros presentes na base consolidada.

```DAX
Quantidade Viagens =
COUNTROWS(Base_Geral)
```

#### Uso no dashboard
- Card de volume total
- Comparações entre áreas
- Análise por período

### Ticket Médio
Calcula o valor médio por registro de despesa

```DAX
Ticket Medio =
DIVIDE(
    [Valor Total],
    [Quantidade Viagens]
)
```
#### Uso no dashboard
- Indicador de valor médio
- Comparação entre períodos e áreas

---

## 2. Medidas por tipo de despesa
### Valor Aéreo

Calcula o total de gastos classificados como despesas aéreas.

```DAX
Valor Aereo =
CALCULATE(
    [Valor Total],
    Base_Geral[Tipo_Despesa] = "Aereo"
)
```

### Valor Hospedagem

Calcula o total gasto com hospedagens.

```DAX
Valor Hospedagem =
CALCULATE(
    [Valor Total],
    Base_Geral[Tipo_Despesa] = "Hospedagem"
)
```

### Valor Uber

Calcula o total gasto com transporte urbano.
```DAX

Valor Uber =
CALCULATE(
    [Valor Total],
    Base_Geral[Tipo_Despesa] = "Uber"
)
```

## 3. Cancelamentos
## Quantidade de Cancelados

Conta a quantidade de solicitações canceladas.
```DAX
Quantidade Cancelados =
COUNTROWS(Cancelados_Raw)
```

## Valor Cancelado

Soma o valor associado às solicitações canceladas.
```DAX
Valor Cancelado =
SUM(Cancelados_Raw[Valor])
```

## 4. Não voados
## Quantidade de Não Voados

Conta a quantidade de passagens emitidas e não utilizadas.
```DAX
Quantidade Nao Voados =
COUNTROWS(Nao_Voados_Raw)
```
## Valor Não Voado

Soma o valor das passagens não utilizadas.
```DAX
Valor Nao Voado =
SUM(Nao_Voados_Raw[Valor])
```

## 5. Observações
- As medidas utilizam o contexto de filtro do Power BI.
- Os filtros de período devem utilizar Dim_Trimestre.
- Os filtros por área devem utilizar Dim_Centro_Custo.
- A tabela Base_Geral concentra as principais despesas utilizadas nas análises.