-- IN
SELECT * FROM
DimProduct
WHERE ColorName IN ('Silver','Blue','White','Red','Black')

-- LIKE
SELECT * FROM
DimProduct
WHERE ProductDescription LIKE '%MP3 Player%'

-- BETWEEN
SELECT * FROM
DimProduct
WHERE UnitPrice BETWEEN 50 AND 100

-- IS NULL | NOT IS NULL
SELECT * FROM
DimCustomer
WHERE CompanyName IS NOT NULL

SELECT * FROM
DimCustomer
WHERE CompanyName IS NULL