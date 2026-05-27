-- Por que precisamos do JOIN?

SELECT TOP(1000) * FROM FactSales
SELECT * FROM DimChannel

SELECT
	ChannelKey,
	SUM(SalesQuantity) AS 'QTD.Vendida'
FROM
	FactSales
GROUP BY channelKey