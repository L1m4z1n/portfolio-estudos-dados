'''
Range
Estrutura:

- range(tamanho)

ou

- range(inicio,fim)

ou

- range(inicio, fim, passo)
'''

#uso comum no for
produtos = ['arroz','feijao','macarrao','atum','azeite']
estoque = [50,100,20,5,80]

for i in range(5):
    i+=1
    print(i)


# range com inicio e fim
print(range(1,10))

#vamos olhar no for para entender

'''
Exemplo: Modelo Jack Welch da G&E

1. Classe A: 10% melhor
2. Classe B: 80% mantém/busca melhorar
3. Classe C: 10% pior demitido

Quem são os funcionário classe B?
'''
funcionarios = ['Maria','José','Gabriel','Lucas','Leticia','Joana']
vendas = [2750,1900,1500,1200,1100,999]


print('Funcionários classe B')
for i in range(1,5):
    i+=1
    print(f'{funcionarios[i]}: fez {vendas[i]} vendas')