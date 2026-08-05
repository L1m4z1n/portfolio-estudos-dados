def area_a_ser_pintada():
    area = int(input('Qual é o tamanho em metros quadrados a ser pintada:'))
    return area
#Pegar quantos litros eu vou precisar de tinta
def litros_necessarios(area):
    litros = area / 6
    return litros
#Calcular quantas latas e quantos galões eu vou precisar
    #Calcular quantas latas inteiras eu vou precisar
    #Calcular quantos litros ainda faltam comprar
    #Calcular quanto custa preencher esses litros que faltam com galão
    #Calcular quanto custa preencher esses litros que faltam com latas
    #Escolher a opção mais barata

#Calcular custo total

def calcular_custo(latas,galoes):
    custo_latas = latas * 80
    custo_galoes = galoes * 25
    custo = custo_latas + custo_galoes
    return custo


area = area_a_ser_pintada()
litros_necessarios = (area)
latas = 0
galoes = 0

latas_inteiras = int(litros / 18)

litros_faltam = litros % 18

custo_extra_latas = 1 *80

galoes = litros_faltam / 3.6
if galoes > int(galoes):
    galoes = int(galoes) + 1

custo_extra_galoes = galoes *25

if custo_extra_latas < custo_extra_galoes:
    latas = latas_inteiras + 1
    galoes = 0
else:
    latas = latas_inteiras

custo = calcular_custo(latas,galoes)
print(f"Litros: {litros}")
print(f"Latas: {latas}")
print(f"Galoes: {galoes}")
print(f"Custo: {custo}")