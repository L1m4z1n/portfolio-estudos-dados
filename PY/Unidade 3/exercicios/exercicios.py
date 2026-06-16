# 1º
cpf = input('Digite o seu CPF:')

if len(cpf) != 11 or not cpf.isnumeric():
    print("Digite seu CPF, corretamente e digite apenas números!!")
else:
    print(cpf)

# 2º
cpf = input('Digite o seu CPF:')

cpf_limpo =cpf.replace('.','').replace('-','')

if len(cpf_limpo) != 11 or not cpf_limpo.isnumeric():
    print("Digite seu CPF, corretamente e digite apenas números!!")
else:
    print(cpf_limpo)

# 3º
nome = input('Digite seu nome:')
gmail = input("Digite seu gmail:")

if nome.strip() != "" and '@' in gmail and '.' in gmail:
    print('Gmail veridico')
else:
    print('Tente outro gmail')