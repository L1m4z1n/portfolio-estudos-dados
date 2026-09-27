# Arquitetura do Projeto

Este documento apresenta a arquitetura adotada no projeto **Dashboard de Viagens Corporativas**, desenvolvido em Power BI com dados exclusivamente fictícios.

O objetivo da arquitetura é separar de forma clara:

- origem dos dados;
- transformação;
- consolidação;
- modelagem;
- métricas;
- segurança;
- visualização.

---

## 1. Visão Geral da Arquitetura

O fluxo principal do projeto é:

```text
viagens_ficticias.xlsx
        ↓
Power Query
        ↓
Tratamento e padronização
        ↓
Tabelas de estágio / Raw
        ↓
Base_Geral + fatos operacionais
        ↓
Dimensões
        ↓
Modelo de dados
        ↓
Medidas DAX
        ↓
RLS Dinâmico
        ↓
Dashboard Power BI
```

---

## 2. Fonte de Dados

A origem principal utilizada no projeto é:

```text
data/viagens_ficticias.xlsx
```

O arquivo contém dados fictícios relacionados a:

- passagens aéreas;
- hospedagens;
- transporte urbano;
- diárias;
- cancelamentos;
- passagens não utilizadas.

Nenhuma fonte corporativa real é utilizada no projeto publicado.

---

## 3. Camada de Entrada

Os dados do arquivo Excel são carregados inicialmente em queries específicas.

As principais queries utilizadas são:

```text
Passagem_Raw
Uber_Raw
Hospedagem_Raw
Diarias_Raw
Cancelados_Raw
Nao_Voados_Raw
```

Cada query representa um conjunto específico de informações operacionais.

---

## 4. Transformação dos Dados

As transformações são realizadas no Power Query.

Entre as principais etapas estão:

- definição dos tipos de dados;
- padronização dos nomes das colunas;
- tratamento de datas;
- padronização de valores;
- padronização de centros de custo;
- padronização de diretorias;
- criação do tipo de despesa;
- classificação de períodos;
- preparação das tabelas para consolidação.

O detalhamento das transformações está disponível em:

```text
power-query/transformacoes.md
```

---

## 5. Base Consolidada

A principal tabela analítica do projeto é:

```text
Base_Geral
```

Ela consolida os principais registros utilizados nas análises financeiras e operacionais do dashboard.

A `Base_Geral` é formada a partir da combinação das seguintes fontes:

```text
Passagem_Raw
Uber_Raw
Hospedagem_Raw
Diarias_Raw
```

O processo de consolidação permite analisar diferentes tipos de despesas utilizando uma estrutura comum.

Entre os principais campos utilizados estão:

```text
Viajante
Data
Diretoria
Centro_Custo
Tipo_Despesa
Valor_Total
Trimestre
```

---

## 6. Tabelas Operacionais Específicas

Algumas tabelas permanecem separadas da `Base_Geral`, pois representam processos específicos.

### Cancelados_Raw

Armazena informações sobre solicitações canceladas.

É utilizada principalmente para:

- quantidade de cancelamentos;
- valor cancelado;
- análise por diretoria;
- análise por centro de custo.

---

### Nao_Voados_Raw

Armazena informações sobre passagens emitidas e não utilizadas.

É utilizada para:

- quantidade de passagens não utilizadas;
- valor associado;
- análise por diretoria;
- análise por centro de custo;
- análise por viajante.

---

### Diarias_Raw

A tabela de diárias também pode ser utilizada diretamente em medidas específicas, mesmo com seus dados consolidados na estrutura analítica.

Ela permite calcular:

- valor total de diárias;
- quantidade de registros;
- distribuição por diretoria;
- distribuição por trimestre.

---

## 7. Dimensões

O modelo utiliza dimensões para centralizar os principais filtros do relatório.

### Dim_Trimestre

Responsável pela organização temporal das análises.

Foi criada com quatro períodos:

```text
Primeiro Trimestre
Segundo Trimestre
Terceiro Trimestre
Quarto Trimestre
```

A dimensão também possui a coluna:

```text
Ordem
```

utilizada para garantir a ordenação correta nos gráficos:

```text
T1 → T2 → T3 → T4
```

Estrutura:

```text
Dim_Trimestre
├── Trimestre
└── Ordem
```

---

### Dim_Centro_Custo

Responsável pela estrutura organizacional utilizada no relatório.

Contém principalmente:

```text
Diretoria
Centro_Custo
```

Essa dimensão possui dois papéis importantes:

1. centralizar os filtros organizacionais;
2. atuar como ponto de aplicação do RLS dinâmico.

Estrutura conceitual:

```text
Diretoria
    ↓
Centro de Custo
```

---

## 8. Modelo de Dados

O modelo segue uma estrutura dimensional simplificada.

As dimensões filtram as tabelas fato através de relacionamentos do tipo:

```text
1 : *
```

com direção de filtro da dimensão para as tabelas fato.

### Relacionamentos por trimestre

```text
Dim_Trimestre
      │
      ├──→ Base_Geral
      ├──→ Diarias_Raw
      ├──→ Cancelados_Raw
      └──→ Nao_Voados_Raw
```

---

### Relacionamentos por estrutura organizacional

```text
Dim_Centro_Custo
      │
      ├──→ Base_Geral
      ├──→ Diarias_Raw
      ├──→ Cancelados_Raw
      └──→ Nao_Voados_Raw
```

A utilização das dimensões evita que cada visual utilize diretamente atributos repetidos nas tabelas fato.

---

## 9. Camada de Medidas

As métricas do relatório são criadas utilizando DAX.

Entre os principais grupos de medidas estão:

### Indicadores financeiros

```text
Soma Valor Total
Valor Aereo
Valor Hospedagem
Valor Uber
Valor Total Diarias
Valor Cancelado
Valor Nao Voado
```

### Indicadores de volume

```text
Qtd_Total
Qtd Aereo
Qtd Hospedagem
Qtd Uber
Qtd Diarias
Quantidade Cancelados
Quantidade Nao Voados
```

### Indicadores temporais

```text
Valor Total T1
Valor Total T2
Valor Total T3
Valor Total T4
Variacao T1 T4 %
Ranking Variacao
```

### Segurança

```text
Usuario Logado
Perfil Usuario
Diretoria Permitida
Status RLS
Qtd Diretorias Visiveis
Qtd Centros Visiveis
Descricao Acesso
```

A documentação das medidas está disponível em:

```text
dax/medidas.md
```

---

## 10. Row-Level Security

O projeto utiliza **Row-Level Security dinâmico**.

O objetivo é permitir que o mesmo relatório apresente diferentes conjuntos de dados dependendo do usuário autenticado.

O fluxo utilizado é:

```text
USERPRINCIPALNAME()
        ↓
Acesso_Usuarios
        ↓
Identificação do perfil
        ↓
Identificação da diretoria permitida
        ↓
Dim_Centro_Custo
        ↓
Tabelas fato
```

---

## 11. Tabela de Acesso

A tabela:

```text
Acesso_Usuarios
```

contém dados fictícios de acesso.

Sua estrutura principal é:

```text
Email
Diretoria
Perfil
```

Exemplo conceitual:

```text
ana.tecnologia@empresa.com
DIR_TECNOLOGIA
Usuario
```

Os perfis utilizados são:

```text
Usuario
Gestor
Auditor
```

---

## 12. Perfis de Segurança

### Usuário

Possui acesso somente aos dados relacionados à diretoria associada ao seu cadastro.

Exemplo:

```text
ana.tecnologia@empresa.com
        ↓
DIR_TECNOLOGIA
        ↓
GER_DADOS
GER_SISTEMAS
```

---

### Gestor

Possui acesso às diretorias previstas pela regra de acesso total.

---

### Auditor

Possui acesso completo para fins de análise e validação.

---

## 13. Aplicação do RLS

O RLS é aplicado sobre:

```text
Dim_Centro_Custo
```

e não diretamente sobre todas as tabelas fato.

Isso permite que o filtro de segurança seja propagado pelo modelo.

Fluxo:

```text
Usuário
   ↓
Acesso_Usuarios
   ↓
Dim_Centro_Custo
   ↓
Base_Geral
Diarias_Raw
Cancelados_Raw
Nao_Voados_Raw
```

Essa abordagem centraliza a lógica de segurança e reduz duplicações.

---

## 14. Camada de Apresentação

O relatório foi desenvolvido utilizando:

- visuais nativos do Power BI;
- cards;
- gráficos de barras;
- gráficos de linha;
- gráficos de rosca;
- tabelas;
- slicers;
- botões de navegação;
- medidas DAX com HTML.

---

## 15. Visuais HTML

Alguns elementos foram criados utilizando medidas DAX que retornam HTML.

Essa abordagem foi utilizada para criar componentes personalizados, como:

- cards;
- rankings;
- indicadores;
- elementos de segurança;
- fluxo visual do RLS.

Exemplos:

```text
HTML Ranking Variacao Diretorias
HTML Card Usuario
HTML Card Perfil
HTML Card Diretoria
HTML Card Status RLS
HTML Banner RLS
HTML Destaque RLS
HTML Perfis Acesso
HTML Fluxo Seguranca
HTML Aviso Acesso
HTML Tabela Validacao RLS
```

Esses elementos fazem parte da camada de apresentação e utilizam as mesmas medidas analíticas do modelo.

---

## 16. Páginas do Dashboard

### Visão Geral

Apresenta os principais indicadores do relatório, incluindo:

- valor total;
- quantidade total;
- gastos por tipo de despesa;
- distribuição por diretoria;
- alertas operacionais.

---

### Por Diretoria

Apresenta uma visão comparativa das diretorias.

As diretorias fictícias utilizadas são:

```text
DIR_TECNOLOGIA
DIR_ADMINISTRATIVA
DIR_COMERCIAL
DIR_OPERACOES
DIR_FINANCEIRA
```

---

### Páginas de Detalhe

Foram criadas páginas específicas para detalhar cada diretoria e seus respectivos centros de custo.

---

### Prazos

Apresenta análises relacionadas ao tempo entre solicitação e viagem e à classificação dos prazos.

---

### Cancelados e Não Voados

Apresenta indicadores relacionados a:

- solicitações canceladas;
- passagens não utilizadas;
- valores;
- diretorias;
- centros de custo;
- viajantes.

---

### Evolução Trimestral

Permite comparar o comportamento dos gastos entre:

```text
T1
T2
T3
T4
```

Inclui:

- valores por trimestre;
- evolução temporal;
- variação entre T1 e T4;
- ranking de diretorias por variação.

---

### Segurança / RLS

Página técnica criada para validar o funcionamento do controle de acesso.

Apresenta:

- usuário autenticado;
- perfil;
- diretoria permitida;
- status do RLS;
- fluxo de segurança;
- perfis de acesso;
- dados visíveis para o usuário.

Essa página permanece fora da navegação analítica principal e pode ser acessada através de um botão específico.

---

## 17. Navegação

A navegação principal do relatório direciona o usuário para as páginas de análise.

Estrutura conceitual:

```text
Visão Geral
    ↓
Por Diretoria
    ↓
Prazos
    ↓
Cancelados e Não Voados
```

A página de evolução trimestral pode ser acessada através de navegação complementar.

A página de segurança é tratada como uma área técnica do relatório.

---

## 18. Separação entre Segurança e Navegação

A navegação das páginas é um recurso de experiência do usuário.

Ela não é considerada um mecanismo de segurança.

A proteção dos dados é realizada através do:

```text
Row-Level Security
```

Portanto:

```text
Navegação = experiência do usuário
RLS = segurança dos dados
```

Essa separação é importante para garantir que o controle de acesso não dependa de páginas ou botões ocultos.

---

## 19. Estrutura do Repositório

A organização prevista para o projeto é:

```text
powerbi-viagens-corporativas/
│
├── data/
│   └── viagens_ficticias.xlsx
│
├── powerbi/
│   └── dashboard_viagens.pbix
│
├── dax/
│   └── medidas.md
│
├── power-query/
│   └── transformacoes.md
│
├── docs/
│   ├── arquitetura.md
│   └── seguranca-e-governanca.md
│
├── images/
│   ├── visao-geral.png
│   ├── por-diretoria.png
│   ├── cancelados-nao-voados.png
│   ├── evolucao-trimestral.png
│   ├── seguranca-rls.png
│   icones/
│       ├── icon_areas.png
│       ├── icon_cancelados.png
│       ├── icon_comparativo.png
│       ├── icon_prazos.png
│       ├── icon_visao_geral.png
│       └── img_fundo_bi
└── README.md
```

---

## 20. Resumo da Arquitetura

A solução pode ser resumida em quatro camadas principais.

### Dados

```text
Excel fictício
```

### Transformação

```text
Power Query
```

### Modelo

```text
Base_Geral
Tabelas operacionais
Dim_Trimestre
Dim_Centro_Custo
DAX
RLS
```

### Visualização

```text
Power BI
Dashboards
HTML personalizado
Navegação
```

O resultado final é um projeto de Business Intelligence que contempla não apenas visualização de dados, mas também:

- tratamento;
- modelagem;
- análise;
- segurança;
- governança;
- documentação.