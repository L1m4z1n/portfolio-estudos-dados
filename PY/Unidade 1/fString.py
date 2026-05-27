# F-string
faturamento = 1000
custo = 400

lucro = faturamento - custo

# Com format
print("O faturamento foi de {} e o lucro de {}".format(faturamento,lucro))

# Com F-string
print(f"O faturamento foi de {faturamento} e o lucro foi de {lucro}")

#Mudança de tipo de variável
faturamento = int(input("Insira o faturamento:"))
custo = int(input("Insira o custo:"))

lucro = faturamento - custo
print(lucro)

# str -> muda para string
# int -> muda para inteiro
# float -> muda para float