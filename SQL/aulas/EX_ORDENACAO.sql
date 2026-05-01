-- 1)
SELECT * FROM DimEmployee
WHERE Gender = 'F' AND DepartmentName = 'Finance'

-- 2)
SELECT * FROM DimProduct
WHERE BrandName = 'Contoso' AND ColorName = 'Red' AND UnitPrice >= 100

-- 3)
SELECT * FROM DimProduct
WHERE BrandName = 'Litware' OR BrandName = 'Fabrikam' OR ColorName = 'Black'

-- 4)
SELECT * FROM DimSalesTerritory
WHERE SalesTerritoryGroup = 'Europe' AND SalesTerritoryCountry != 'Italy'