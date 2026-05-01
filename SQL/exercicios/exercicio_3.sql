--1)
SELECT COUNT(SalesQuantity), COUNT(ReturnAmount) FROM FactSales

-- 2)
SELECT AVG(YearlyIncome) FROM DimCustomer
WHERE Occupation = 'Professional'

-- 3) a, b)
SELECT MAX(EmployeeCount) AS 'QTD Funcionarios', StoreName AS 'Nome da Loja' FROM DimStore
GROUP BY EmployeeCount,StoreName
ORDER BY EmployeeCount DESC

-- c)
SELECT
	MIN(EmployeeCount) AS 'Menor QTD. Funcionarios'
FROM
	DimStore