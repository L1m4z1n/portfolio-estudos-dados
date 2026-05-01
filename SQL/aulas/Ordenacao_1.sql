--Quantas colunas têm um preço unitário maior que $1000?
SELECT
COUNT(UnitPrice) AS 'QUANTIDADE'
FROM
DimProduct
WHERE UnitPrice >= 1000

--Colunas de texto colocar N entre ''
--Colunas de data filtrar no formato de data 'YYYY/MM/DD'

--Condicionais
SELECT
	*
FROM
	DimProduct
WHERE
	BrandName = 'Fabrikam'
AND
	ColorName = 'Black'

	--OR
SELECT
	*
FROM
	DimProduct
WHERE
	BrandName = 'Contoso'
OR
	ColorName = 'White'

	--NOT
SELECT
	*
FROM
	DimEmployee
WHERE NOT
	DepartmentName = 'Marketing'
