meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]

for vendedor in vendas:
    if vendedor[1] >= meta:
        print(f"{vendedor[0]} bateu a meta com {vendedor[1]} em vendas!")