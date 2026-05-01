--1.
-- a)
SELECT
	COUNT(*)
FROM
	DimProduct
-- b)
SELECT
	COUNT(*)
FROM
	DimCustomer
/*
	INSIGTH
A empresa não possui 19.500 clientes na base de controle. Na realidade possui 18.869 clientes
*/

--2.
-- a)
SELECT 
	CustomerKey,
	FirstName,
	EmailAddress,
	BirthDate
FROM
	DimCustomer
-- b)
SELECT 
	CustomerKey AS 'ID',
	FirstName AS 'Primeiro Nome',
	EmailAddress AS 'Endereço',
	BirthDate AS 'Data do Nascimento'
FROM
	DimCustomer

--3.
-- a)
SELECT 
TOP(100)
	*
FROM
	DimCustomer

-- b)
SELECT 
TOP(10) 
PERCENT
	*
FROM
	DimCustomer

-- c)
SELECT TOP(100)
	FirstName,
	EmailAddress,
	BirthDate
FROM
	DimCustomer

-- d)
SELECT TOP(100)
	FirstName AS 'Primeiro Nome',
	EmailAddress AS 'E-mail',
	BirthDate AS 'Data do Aniversário'
FROM
	DimCustomer

--4.
-- a)
SELECT DISTINCT
 manufacturer AS 'Produtor'
FROM
	DimProduct

--5
SELECT DISTINCT TOP(1000) ProductKey FROM factSales