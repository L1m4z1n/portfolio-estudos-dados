-- CROSSJOIN

SELECT * FROM marcas
SELECT * FROM subcategoria

-- OBS:. Não adicionei a tabela de marcas na base contoso

SELECT 
	marca,
	nome_subcategoria
FROM
	marcas
CROSS JOIN subcategoria