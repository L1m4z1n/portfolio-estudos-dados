# 1. Faça um Programa que mostre a mensagem "Hello World!" na tela
print("Hello Word!")

# 2. Faça um Programa que peça um número e então mostre a mensagem: "O número informado foi [número]"
number = int(input("Insira um número:"))
print(f"O número informado foi {number}")

# 3. Faça um Programa que peça dois números e imprima a soma
number = int(input("Insira um número:"))
number_2 = int(input("Insira outro número:"))
soma = number+number_2
print(f"A soma dos números é igual a {soma}")

# 4. Faça um Programa que peça as 4 notas bimestrais de um aluno e mostre a média de todas as notas.
nota_matematica = int(input("Insira a nota de matemática:"))
nota_portugues = int(input("Insira a nota de português:"))
nota_ciencias = int(input("Insira a nota de ciências:"))
nota_artes = int(input("Insira a nota de artes:"))

media = (nota_matematica+nota_portugues+nota_ciencias+nota_artes)/4
print(f"A média das notas é igual a {media}")
#### 5. Faça um Programa que converta metros para centímetros. Você pode pedir o comprimento em metros para o usuário (input).

metros = int(input("Quantos metros em centimetros:"))

transformar_centimetros = metros * 100
print(f"{metros} metros é igual a {transformar_centimetros} centimetros")

#### 6. Faça um Programa que calcule a área de uma sala de um apartamento. Para isso, o seu programa precisa pedir a largura da sala, o comprimento da sala e imprimir a área em m² da sala.
largura_sala = int(input("Informe a largura da sala:"))
comprimento_sala = int(input("Informe o comprimento da sala:"))

area = largura_sala * comprimento_sala
print(f"A sala possui {area} m²")
#### 7. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
ganho = int(input("Quanto você ganha por hora:"))
horas_trabalhadas = int(input("Quantas horas trabalhadas:"))
salario = ganho * horas_trabalhadas
print(salario)
#### 8. Vamos criar um conversor de temperatura. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#$C = \frac{5}{9}(F-32)$
temp_fahrenheit = float(input("Temperatura(Fº): "))
fahrenheit = (temp_fahrenheit-32)*5/9
print(fahrenheit)
#### 9. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
#$F = \frac{9}{5}C + 32$
temp_celsius = float(input("Temperatura(Cº): "))
fahrenheit = ((9/5)*temp_celsius)+32
print(fahrenheit)
#### 10. Tendo como dados de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula:
#$P = 72,7h - 58$
#Lembrando que "algoritmo" nada mais é do que um programa, como todos os outros que você vem fazendo