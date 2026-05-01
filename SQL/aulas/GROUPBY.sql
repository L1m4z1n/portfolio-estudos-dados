-- GROUP BY
SELECT * FROM DimProduct

SELECT
BrandName AS 'Nome da Marca',
COUNT(*) AS 'QTD. Total'
FROM DimProduct
GROUP BY BrandName

-- WHERE + GROUP BY
SELECT
	ColorName AS 'Cor do Produto',
	COUNT(*) AS 'Total de Produtos'
FROM
	DimProduct
WHERE BrandName = 'Contoso'
GROUP BY ColorName

--GROUP BY + HAVING
SELECT
BrandName AS 'Nome da Marca',
COUNT(*) AS 'QTD. Total'
FROM DimProduct
GROUP BY BrandName
HAVING COUNT(BrandName) >= 200

-- WHERE VS HAVING
SELECT
BrandName AS 'Nome da Marca',
COUNT(*) AS 'QTD. Total'
FROM DimProduct
WHERE ClassName = 'Economy' -- Filtra a tabela original, antes do agrupamento
GROUP BY BrandName
HAVING COUNT(BrandName) >= 200 -- Filtra a tabela depois de agrupada

