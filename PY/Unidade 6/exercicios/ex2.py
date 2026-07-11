#### 1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

while True:
    nota = float(input("Digite sua nota:"))
    if nota >= 0 and nota <=10:
        print(nota)
        break
    else:
        print('Digite uma nota entre 0 a 10!!!')
    

#### 2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    nome = input("Digite o nome do usuário:")
    senha = input("Digite sua senha:")

    if senha == nome:
        print("A senha não pode conter seu nome!!")
    else:
        print("Usuário e senha cadastrados com sucesso!!")
        break



#### 3. Faça um programa que leia e valide as seguintes informações (e para cada uma delas, continue pedindo a informação até o usuário inserir corretamente):
##### Nome: maior que 3 caracteres;
##### Idade: entre 0 e 150;
##### Salário: maior que zero;
##### Sexo: 'f' ou 'm';
##### Estado Civil: 's', 'c', 'v', 'd';

while True:
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    salario = input("Digite seu salário: ")
    sexo = input("Digite seu sexo (f/m): ").lower()
    estado_civil = input("Digite seu estado civil (s/c/v/d): ").lower()

    valido = True

    if len(nome) <= 3:
        print("O nome deve possuir mais que 3 caracteres!")
        valido = False

    try:
        idade = int(idade)
        if not (0 <= idade <= 150):
            print("Idade deve estar entre 0 e 150!")
            valido = False
    except ValueError:
        print("Digite um número válido para idade!")
        valido = False

    try:
        salario = float(salario)
        if salario <= 0:
            print("Salário deve ser maior que zero!")
            valido = False
    except ValueError:
        print("Digite um número válido para salário!")
        valido = False

    if sexo not in ['f', 'm']:
        print("Digite apenas 'f' ou 'm'!")
        valido = False

    if estado_civil not in ['s', 'c', 'v', 'd']:
        print("Digite apenas 's', 'c', 'v' ou 'd'!")
        valido = False

    if valido:
        print("\nCadastro realizado com sucesso!")
        print(f"Nome: {nome}, Idade: {idade}, Salário: {salario}, Sexo: {sexo}, Estado Civil: {estado_civil}")
        break
  

#### 4. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
pop_A = 80000
pop_B = 200000
tempo = 0
while pop_A < pop_B:
    pop_A *= 1.03
    pop_B *= 1.015
    tempo += 1

print(f"Será necessário {tempo} anos, para a população A igualar a população B")
#### 5. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
repeticao = 's'
while repeticao == 's':
    pop_A = int(input("Digite a quantidade da população A:"))
    pop_B = int(input("Digite a quantidade da população B:"))
tx_A = float(input('Informe a taxa de crescimento da população A em porcentagem (exemplo: entre 3 para 3%): '))
tx_B = float(input('Informe a taxa de crescimento da população B em porcentagem (exemplo: entre 3 para 3%): '))
while tx_A <= 0 or tx_B <= 0:
    print('As taxas precisam ser maiores que zero')
    tx_A = float(input('Informe a taxa de crescimento da população A em porcentagem (exemplo: entre 3 para 3%): '))
    tx_B = float(input('Informe a taxa de crescimento da população B em porcentagem (exemplo: entre 3 para 3%): '))
tx_A = tx_A / 100 + 1
tx_B = tx_B / 100 + 1

tempo = 0

while pop_A < pop_B:
    pop_A *= tx_A
    pop_B *= tx_B
    tempo += 1
print(f"Será necessário {tempo} anos, para a população A igualar a população B")
repeticao = input('Deseja repetir a operação? Tecle "s" para sim, qualquer outra tecla para não.')

#### 6. Faça um programa que peça para o usuário inserir o faturamento dos últimos 5 meses (individualmente) e informe o maior faturamento



#### 7. Faça um programa que peça para o usuário inserir o faturamento dos últimos 5 meses (individualmente) e informe o faturamento total (soma) e o faturamento médio por mês (média).




#### 8. Faça um programa que consiga categorizar a idade das equipes de uma empresa. Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da equipe varia entre 0 e 25 (jovem) ,26 e 60 (sênior) e maior que 60 (idosa); e então, dizer se a equipe é jovem, sênior ou idosa, conforme a média calculada.




#### 9. Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.



#### 10. Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
