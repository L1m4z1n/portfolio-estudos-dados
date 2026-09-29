-- LEFT, RIGHT E FULL ANTI JOIN

SELECT * FROM produtos
SELECT * FROM subcategoria

SELECT
 id_produto,
 nome_produto,
 produtos.id_subcategoria,
 subcategoria.nome_subcategoria
FROM
	produtos
LEFT JOIN subcategoria
ON produtos.id_subcategoria = subcategoria.id_subcategoria
WHERE nome_subcategoria IS NULL

SELECT
 id_produto,
 nome_produto,
 produtos.id_subcategoria,
 subcategoria.nome_subcategoria
FROM
	produtos
RIGHT JOIN subcategoria
ON produtos.id_subcategoria = subcategoria.id_subcategoria
WHERE id_produto IS NULL

SELECT
 id_produto,
 nome_produto,
 produtos.id_subcategoria,
 subcategoria.nome_subcategoria
FROM
	produtos
FULL JOIN subcategoria
ON produtos.id_subcategoria = subcategoria.id_subcategoria
WHERE id_produto IS NULL OR nome_subcategoria IS NULL