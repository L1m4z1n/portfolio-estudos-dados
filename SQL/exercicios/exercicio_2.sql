-- 1)
SELECT 
	TOP(100) * 
FROM 
	FactSales
ORDER BY SalesQuantity DESC

-- 2)
SELECT DISTINCT TOP(10)  * FROM DimProduct
ORDER BY UnitPrice DESC, Weight DESC,AvailableForSaleDate ASC

-- 3) 
-- a,b,c)
SELECT ProductName AS 'Nome do Produto', Weight AS 'Peso' FROM DimProduct
WHERE Weight >= 100
ORDER BY Weight DESC

-- 4) a)
SELECT * FROM DimStore

SELECT StoreName AS 'Nome da Loja', OpenDate AS 'Data de Abertura',EmployeeCount AS 'QTD FUNCIONARIOS' FROM DimStore
WHERE Status = 'ON'

-- 5)
SELECT * FROM DimProduct
WHERE BrandName = 'Litware' AND ProductName LIKE 'Litware Home%' AND AvailableForSaleDate = '2009-15-03'

-- 6)
SELECT * FROM DimStore
WHERE CloseReason IS NOT Null

-- 7)
SELECT * FROM DimStore
WHERE EmployeeCount BETWEEN 1 AND 20

-- 8)
SELECT ProductKey AS 'ID', ProductName AS 'Nome', UnitPrice AS 'Preço' FROM DimProduct
WHERE ProductDescription LIKE '%LCD%'

-- 9)
SELECT * FROM DimProduct
WHERE BrandName IN ('Contoso','Litware','Fabrikam') AND ColorName IN ('Green','Orange','Black','Silver','Pink')

-- 10)
SELECT * FROM DimProduct
WHERE BrandName = 'Contoso' AND ColorName = 'Silver' AND UnitPrice BETWEEN 10 AND 30
ORDER BY UnitPrice DESC