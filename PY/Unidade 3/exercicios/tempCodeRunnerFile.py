nome = input('Digite seu nome:')
gmail = input("Digite seu gmail:")

if nome.strip() != "" and '@' in gmail and '.' in gmail:
    print('Gmail veridico')
else:
    print('Tente outro gmail')