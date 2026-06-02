# Elif se temos mais do que um caso de sim ou não

vendas = int(input("Quantas vendas foram feitas:"))

meta = 20000
if vendas < meta:
    print("Não ganhou bônus!")
elif vendas > (meta*2):
    bonus = 0.07 * vendas
    print(f"Ganhou {bonus} de bônus")
else:
    bonus = 0.03 * vendas
    print(f"Ganhou {bonus} de bônus!!")