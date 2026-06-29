nome_hospede = input("Digite seu nome: ")
qtd_convidados = int(input("Quantas pessoas no quarto: "))

quarto = []

for qtd in range(qtd_convidados):
    convidado = input("Nome convidado: ")
    cpf = input("Digite o CPF: ")
    quarto.append([convidado, f"cpf: {cpf}"])
    print(quarto)