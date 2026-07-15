'''
Tuplas
Estrutura:

tupla = (valor,valor,valor,...)

Diferença
Parece uma lista, mas é imutável

Vantagens
-mais eficiente(em termos de performace)
-protege a base de dados(por ser imutável)
-muito usado para dados heterogêneos

Criando tuplas:
'''
vendas = ('Lira','25/08/2020','15/02/1994',2000,'Estagiário')
print(vendas)

# Acessando o valor de uma tupla

nome = vendas[0]
data_contratacao = vendas[1]
data_nascimento = vendas[2]
salario = vendas[3]
cargo = vendas[4]

nome,data_contratacao,data_nascimento,salario,cargo = vendas

# O enumerate que vinhamos usando até agora, na verdade, cria uma tupla para a gente. Vamos ver na prática:

vendas = [1000,2000,300,300,150]
funcionarios = ['João','Lira','Ana','Maria','Paula']

for i,venda in enumerate(vendas):
    print(f'{funcionarios[i]} vendeu {venda} unidades!')