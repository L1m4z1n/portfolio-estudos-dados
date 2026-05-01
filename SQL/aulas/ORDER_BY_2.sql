--EXEMPLO 1: Selecione as 10 primeiras linhas da tabela DimProduct e ordene de acordo com a UnitCost
SELECT TOP(10) 
	ProductName,
	UnitCost,
	Weight
FROM
	DimProduct
ORDER BY UnitCost DESC, Weight DESC