# Dashboard de Viagens Corporativas

Projeto de portfólio em Business Intelligence para análise de viagens corporativas com **Power BI, Power Query e DAX**, utilizando exclusivamente dados fictícios.

> Este projeto foi reconstruído do zero para fins de estudo e portfólio, sem uso de arquivos, dados ou identificadores corporativos reais.

## Objetivo
Centralizar dados de passagens, hospedagens, transporte urbano, diárias, cancelamentos e passagens não utilizadas para apoiar análises de gastos, prazos e padrões por área.

## Arquitetura proposta

`Excel fictício -> Power Query -> Base_Geral -> Modelo de Dados -> DAX -> Dashboard Power BI`

## Estrutura
- `data/`: base fictícia de entrada
- `powerbi/`: arquivo `.pbix` criado no computador pessoal
- `power-query/`: documentação das transformações
- `dax/`: principais medidas DAX
- `images/`: prints das páginas do dashboard
- `docs/`: arquitetura, decisões e documentação complementar

## Próximos passos
1. Importar `data/viagens_ficticias.xlsx` no Power BI.
2. Tratar e padronizar as queries no Power Query.
3. Criar a `Base_Geral` com Passagem, Uber e Hospedagem.
4. Criar dimensões e relacionamentos.
5. Desenvolver as medidas DAX.
6. Criar as páginas do dashboard.
7. Salvar screenshots em `images/`.
8. Completar este README com resultados e aprendizados.
