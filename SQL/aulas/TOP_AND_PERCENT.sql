-- Comando SELECT... FROM: Retorna todas as linhas da tabela, independente das colunas selecionadas

-- 1. Trzer as 10 primeiras linhas
SELECT TOP(10)
	*
FROM
	DimProduct

-- 2. Trzer as 10% primeiras linhas
SELECT TOP(10) PERCENT
	*
FROM
	DimProduct



