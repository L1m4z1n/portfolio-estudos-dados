-- COMO ESCOLHER QUEM É A TABELA DA ESQUERDA E A TABELA DA DIREITA?

SELECT * FROM subcategoria

-- 1. LEFT Join para complementar informações da tabela produtos (LEFT) de acordo com a tabela de categoria (RIGHT)

SELECT 
       id_produto,
	   nome_produto,
	   produtos.id_subcategoria,
	   nome_subcategoria
FROM 
	   produtos
LEFT JOIN subcategoria
	ON produtos.id_subcategoria = subcategoria.id_subcategoria

-- 2. Obtendo o LEFT Join do caso 1 usando um RIGHT Join e invertendo as tabelas de lado

SELECT 
	   id_produto,
	   nome_produto,
	   produtos.id_subcategoria,
	   nome_subcategoria
FROM 
	   subcategoria
RIGHT JOIN produtos
	ON subcategoria.id_subcategoria = produtos.id_subcategoria