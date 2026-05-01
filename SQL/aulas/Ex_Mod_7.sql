-- EXERCICIOS MODULO 7

SELECT TOP (10000) *  FROM FactSales

-- 1)
--a)
SELECT TOP (10000) 
	SUM(SalesQuantity) AS 'Quantidade Total',
	channelKey AS 'Canal de Vendas'  
FROM 
	FactSales
GROUP BY 
	channelKey

--b)
SELECT TOP (1000) 
	SUM(SalesQuantity) AS 'Quantidade Total',
	SUM(ReturnQuantity) AS 'Total Vendido',
	StoreKey AS 'Canal de Vendas'  
FROM 
	FactSales
GROUP BY 
	StoreKey

-- c)
SELECT 
	SUM(SalesAmount) AS 'Total Vendido',
	channelKey AS 'Canal de Vendas'  
FROM 
	FactSales
WHERE 
	DateKey BETWEEN '20070101' AND '20071231'
GROUP BY 
	channelKey

-- 2)
-- a)
SELECT 
	SUM(SalesAmount) AS 'Total Vendido',
	ProductKey AS 'ID Produto'  
FROM 
	FactSales
GROUP BY 
	ProductKey
HAVING SUM(SalesAmount) > 5000000
ORDER BY SUM(SalesAmount) DESC

-- b)
SELECT 
TOP(10)
	SUM(SalesAmount) AS 'Total Vendido',
	COUNT(ProductKey) AS 'ID Produto'  
FROM 
	FactSales
GROUP BY 
	 ProductKey
ORDER BY
	COUNT(SalesAmount) DESC


-- 3)
-- a) ID DO CLIENTE = 19037
SELECT TOP(100)
	CustomerKey AS 'ID',
	SUM(SalesQuantity) AS 'Vendas QTD'
FROM 
	FactOnlineSales
GROUP BY CustomerKey
ORDER BY SUM(SalesQuantity) DESC

-- b)
SELECT * FROM FactOnlineSales

SELECT TOP(3) 
	ProductKey AS 'ID',
	SUM(SalesQuantity) AS 'Total Vendido'
FROM 
	FactOnlineSales
WHERE CustomerKey = 19037
GROUP BY ProductKey
ORDER BY SUM(SalesQuantity) DESC

-- 4)
-- a)
SELECT * FROM DimProduct

SELECT
	COUNT(BrandName) AS 'QTD MARCA',
	BrandName AS 'Marca'
FROM DimProduct
GROUP BY BrandName


--b)
SELECT
	AVG(UnitPrice) AS 'Média Preço',
	ClassName AS 'Classe do Produto'
FROM DimProduct
GROUP BY ClassName

--c)
SELECT
	ColorName AS 'Cor',
	SUM(Weight)	AS 'Peso Total'
FROM
	DimProduct
GROUP BY ColorName

-- 5)
SELECT * FROM DimProduct

SELECT
	StockTypeName AS 'Tipo em Estoque',
	SUM(Weight)	AS 'Peso Total'
FROM
	DimProduct
WHERE BrandName = 'Contoso'
GROUP BY StockTypeName
ORDER BY SUM(Weight) DESC

-- 6)
SELECT DISTINCT
 BrandName AS 'Marca',
 COUNT(ColorName) AS 'QTD Cores'
FROM
	DimProduct
GROUP BY BrandName

SELECT DISTINCT
	ColorName
FROM
	DimProduct
WHERE BrandName = 'Contoso'

-- 7)
SELECT * FROM DimCustomer

SELECT 
	COUNT(FirstName) AS 'Qtd Cliente',
	Gender AS 'Sexo',
	AVG(YearlyIncome) AS 'Média Salário'
FROM 
	DimCustomer
WHERE Gender IS NOT NULL
GROUP BY GENDER

-- 8)
SELECT 
	COUNT(FirstName) AS 'Qtd Cliente',
	Education AS 'Nivel Escolar',
	AVG(YearlyIncome) AS 'Média Salário'
FROM 
	DimCustomer
WHERE Education IS NOT NULL
GROUP BY Education

-- 9)
SELECT * FROM DimEmployee

SELECT 
	COUNT(FirstName) AS 'Qtd Funcionários',
	DepartmentName AS 'Departamento'
FROM 
	DimEmployee
WHERE Status = 'Current'
GROUP BY DepartmentName

-- 10)
SELECT 
	SUM(VacationHours) AS 'Total Horas Ferias',
	Title AS 'Cargo'
FROM 
	DimEmployee
WHERE Gender = 'F' AND DepartmentName IN ('Production','Marketing','Engineering','Finance') AND HireDate BETWEEN '19990101' AND '20000101'
GROUP BY Title