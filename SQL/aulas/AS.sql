--	Comando AS: Renomeando colunas(aliasing

-- Selecione as 3 colunas da tabela dimProduct: ProductName, BrandName, ColorName
SELECT
	ProductName AS Produto,
	BrandName AS Marca,
	ColorName AS Cor
FROM
	DimProduct