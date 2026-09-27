# Transformações no Power Query

Este documento descreve as principais transformações aplicadas às fontes utilizadas no projeto **Dashboard de Viagens Corporativas**.

A origem utilizada no projeto publicado é exclusivamente fictícia:

`data/viagens_ficticias.xlsx`

O objetivo das transformações foi padronizar diferentes tipos de dados operacionais para permitir sua análise em um modelo único no Power BI.

---

## 1. Visão Geral do Processo

O fluxo de transformação pode ser resumido da seguinte forma:

```text
viagens_ficticias.xlsx
        ↓
Importação no Power Query
        ↓
Tratamento individual das fontes
        ↓
Padronização das colunas
        ↓
Criação de campos analíticos
        ↓
Base_Geral
        ↓
Modelo de dados
```

As principais queries utilizadas são:

```text
Passagem_Raw
Uber_Raw
Hospedagem_Raw
Diarias_Raw
Cancelados_Raw
Nao_Voados_Raw
Base_Geral
```

---

## 2. Passagem_Raw

A query `Passagem_Raw` representa os registros fictícios relacionados a passagens aéreas.

### Principais transformações

- definição dos tipos de dados;
- padronização dos nomes das colunas;
- tratamento de campos de data;
- padronização do centro de custo;
- padronização da diretoria;
- padronização do campo de valor;
- criação do tipo de despesa;
- cálculo do intervalo entre solicitação e viagem;
- classificação do prazo;
- criação do trimestre;
- preparação para consolidação na `Base_Geral`.

### Tipo de despesa

Foi adicionada a classificação:

```text
Tipo_Despesa = Aereo
```

Essa coluna permite diferenciar os registros dentro da tabela consolidada.

---

## 3. Cálculo de Prazo

Nos registros de passagem foi calculada a diferença entre:

```text
Data da solicitação
        ↓
Data da viagem
```

O resultado é utilizado na página de análise de prazos.

A lógica permite identificar solicitações realizadas com maior ou menor antecedência.

Essa informação é posteriormente utilizada para classificação dos registros conforme o prazo.

---

## 4. Classificação de Prazo

Após o cálculo da diferença entre as datas, foi criada uma classificação para facilitar a análise operacional.

Essa classificação é utilizada para:

- análise de volume;
- comparação entre diretorias;
- identificação de solicitações fora do prazo;
- construção da página `Prazos`.

A regra detalhada implementada permanece no arquivo `.pbix`.

---

## 5. Uber_Raw

A query `Uber_Raw` contém registros fictícios relacionados ao transporte urbano.

### Principais transformações

- definição dos tipos de dados;
- padronização dos nomes das colunas;
- padronização do centro de custo;
- padronização da diretoria;
- tratamento do campo de valor;
- tratamento de datas;
- criação do trimestre;
- definição do tipo de despesa;
- preparação para inclusão na `Base_Geral`.

### Tipo de despesa

```text
Tipo_Despesa = Uber
```

---

## 6. Hospedagem_Raw

A query `Hospedagem_Raw` contém os registros fictícios relacionados a hospedagens.

### Principais transformações

- definição dos tipos de dados;
- padronização das colunas;
- tratamento de datas;
- padronização do centro de custo;
- padronização da diretoria;
- padronização do campo de valor;
- criação do trimestre;
- definição do tipo de despesa;
- preparação para inclusão na `Base_Geral`.

### Tipo de despesa

```text
Tipo_Despesa = Hospedagem
```

---

## 7. Diarias_Raw

A query `Diarias_Raw` representa os registros fictícios de diárias.

### Principais transformações

- definição dos tipos de dados;
- padronização dos nomes das colunas;
- tratamento das datas;
- padronização da diretoria;
- padronização do centro de custo;
- padronização do campo de valor;
- criação do trimestre;
- criação ou padronização da classificação de despesa;
- preparação para análises específicas;
- preparação para consolidação analítica.

A tabela também permanece disponível separadamente no modelo para cálculo de indicadores específicos de diárias.

---

## 8. Cancelados_Raw

A query `Cancelados_Raw` contém os registros fictícios relacionados a solicitações canceladas.

Essa tabela permanece separada da `Base_Geral`, pois representa um evento operacional específico.

### Principais transformações

- definição dos tipos de dados;
- padronização dos nomes das colunas;
- padronização de diretoria;
- padronização de centro de custo;
- tratamento de datas;
- tratamento do valor cancelado;
- padronização das informações do viajante;
- criação do trimestre;
- preparação para relacionamentos com as dimensões.

### Uso no modelo

A tabela é utilizada para calcular:

- quantidade de cancelamentos;
- valor cancelado;
- distribuição por diretoria;
- distribuição por centro de custo;
- comportamento ao longo dos períodos.

---

## 9. Nao_Voados_Raw

A query `Nao_Voados_Raw` contém registros fictícios de passagens emitidas que não foram utilizadas.

Assim como `Cancelados_Raw`, ela permanece separada da `Base_Geral`.

### Principais transformações

- definição dos tipos de dados;
- padronização das colunas;
- tratamento de datas;
- padronização de diretoria;
- padronização de centro de custo;
- tratamento do campo de valor;
- padronização dos dados de viajante;
- criação do trimestre;
- preparação para relacionamentos com as dimensões.

### Uso no modelo

A tabela permite analisar:

- quantidade de passagens não utilizadas;
- valor associado;
- diretoria;
- centro de custo;
- viajante;
- evolução por período.

---

## 10. Padronização das Colunas

Antes da consolidação das fontes, as queries foram adaptadas para possuir uma estrutura compatível.

Entre os campos padronizados estão:

```text
Viajante
Data
Diretoria
Centro_Custo
Tipo_Despesa
Valor_Total
Trimestre
```

Nem todas as fontes possuem originalmente os mesmos campos.

Quando necessário, as colunas foram:

- renomeadas;
- convertidas;
- preenchidas;
- criadas;
- reorganizadas.

Essa padronização permite que registros de diferentes origens sejam analisados conjuntamente.

---

## 11. Padronização Organizacional

Os campos organizacionais foram estruturados utilizando:

```text
Diretoria
Centro_Custo
```

Exemplos de diretorias fictícias utilizadas no projeto:

```text
DIR_TECNOLOGIA
DIR_ADMINISTRATIVA
DIR_COMERCIAL
DIR_OPERACOES
DIR_FINANCEIRA
```

Exemplos de centros de custo:

```text
GER_DADOS
GER_SISTEMAS
GER_COMPRAS
GER_PESSOAS
GER_SUPRIMENTOS
GER_RELACIONAMENTO
GER_VENDAS
GER_LOGISTICA
GER_OPERACOES
GER_CONTROLADORIA
GER_FINANCAS
```

Essa padronização é importante para:

- filtros;
- relacionamentos;
- análises por área;
- aplicação do RLS.

---

## 12. Criação do Trimestre

Os registros foram preparados para análise temporal utilizando o campo:

```text
Trimestre
```

Os valores utilizados são:

```text
Primeiro Trimestre
Segundo Trimestre
Terceiro Trimestre
Quarto Trimestre
```

No modelo, esses valores são relacionados à dimensão:

```text
Dim_Trimestre
```

A dimensão possui uma coluna de ordenação para garantir a sequência cronológica correta nos gráficos.

---

## 13. Base_Geral

A query `Base_Geral` é a principal tabela consolidada utilizada no dashboard.

Ela reúne os principais registros de despesas utilizados nas análises gerais.

A consolidação utiliza:

```text
Passagem_Raw
Uber_Raw
Hospedagem_Raw
Diarias_Raw
```

O processo utiliza uma operação de append para reunir registros com estruturas padronizadas.

Fluxo:

```text
Passagem_Raw ───────┐
                    │
Uber_Raw ───────────┤
                    ├──→ Base_Geral
Hospedagem_Raw ─────┤
                    │
Diarias_Raw ────────┘
```

---

## 14. Estrutura Analítica da Base_Geral

Entre os principais campos utilizados na tabela consolidada estão:

```text
Viajante
Data
Diretoria
Centro_Custo
Tipo_Despesa
Valor_Total
Trimestre
```

Esses campos permitem realizar análises como:

- gastos totais;
- distribuição por tipo de despesa;
- distribuição por diretoria;
- distribuição por centro de custo;
- evolução trimestral;
- volume de registros.

---

## 15. Tabelas Mantidas Separadamente

Nem todas as queries foram incorporadas à `Base_Geral`.

As seguintes permanecem como tabelas operacionais independentes:

```text
Cancelados_Raw
Nao_Voados_Raw
```

Essa decisão permite manter separadas informações que representam eventos diferentes das despesas efetivamente consolidadas.

`Diarias_Raw` também permanece disponível individualmente para medidas específicas.

---

## 16. Integração com as Dimensões

Após o carregamento no modelo, as tabelas são relacionadas às dimensões analíticas.

### Dim_Trimestre

Utilizada para filtros temporais.

```text
Dim_Trimestre
        ↓
Base_Geral
Diarias_Raw
Cancelados_Raw
Nao_Voados_Raw
```

### Dim_Centro_Custo

Utilizada para filtros organizacionais.

```text
Dim_Centro_Custo
        ↓
Base_Geral
Diarias_Raw
Cancelados_Raw
Nao_Voados_Raw
```

A centralização dos filtros nas dimensões reduz duplicações e melhora a consistência do modelo.

---

## 17. Relação com o RLS

A padronização de:

```text
Diretoria
Centro_Custo
```

também permite a implementação de Row-Level Security.

O RLS é aplicado sobre:

```text
Dim_Centro_Custo
```

e o filtro é propagado para as tabelas fato.

Fluxo:

```text
Acesso_Usuarios
        ↓
Dim_Centro_Custo
        ↓
Base_Geral
Diarias_Raw
Cancelados_Raw
Nao_Voados_Raw
```

Assim, a lógica de segurança não precisa ser repetida em cada tabela operacional.

---

## 18. Tipos de Dados

Os tipos de dados foram revisados durante a etapa de transformação.

Exemplos:

```text
Datas          → Date / DateTime
Valores        → Decimal Number
Textos         → Text
Quantidades    → Whole Number
```

Essa etapa é importante para garantir o funcionamento correto de:

- cálculos;
- relacionamentos;
- filtros;
- medidas DAX;
- análises temporais.

---

## 19. Tratamento de Dados Fictícios

Todas as fontes utilizadas na versão publicada são fictícias.

As transformações foram desenvolvidas sobre essas fontes para reproduzir um cenário semelhante a um processo corporativo de viagens, sem expor:

- dados reais;
- nomes reais;
- identificadores corporativos;
- URLs internas;
- credenciais;
- documentos privados.

---

## 20. Resultado do Processo de Transformação

Após as etapas de Power Query, o fluxo final pode ser representado como:

```text
Excel fictício
      ↓
Queries Raw
      ↓
Padronização
      ↓
Tratamentos
      ↓
Base_Geral
      +
Tabelas operacionais
      ↓
Dimensões
      ↓
Modelo Power BI
      ↓
DAX
      ↓
Dashboard
```

As transformações permitem que fontes originalmente diferentes sejam utilizadas em um único modelo analítico, preservando tabelas específicas quando necessário.

---

## 21. Resumo

As principais atividades realizadas no Power Query foram:

- importação das fontes fictícias;
- definição dos tipos de dados;
- padronização das colunas;
- tratamento de datas;
- padronização dos valores;
- padronização da estrutura organizacional;
- criação do tipo de despesa;
- preparação dos períodos;
- classificação de prazos;
- consolidação das despesas;
- preparação das tabelas para o modelo dimensional.

O resultado é uma camada de dados preparada para suportar as análises, medidas DAX e regras de segurança utilizadas no dashboard.