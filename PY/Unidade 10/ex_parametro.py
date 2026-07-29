'''
Exemplos de parâmetros

- upper() -> não tem parâmetros
- sort() -> apenas parâmetros keyword
- extend(lista) -> 1 parâmetro obrigatório
- nossa função eh_da_cate

'''

def eh_da_Categoria(bebida,cod_categoria):
    bebida = bebida.upper()
    if cod_categoria in bebida:
        return True
    else:
        return False

cod_produto = 'beb12304'
print(cod_produto.upper())

vendas_ano = [100,200,50,90,240,300,55,10,789,60]
vendas_novdez = [500,1555]

vendas_ano.extend(vendas_novdez)
print(vendas_ano)



if eh_da_Categoria(cod_produto, 'BEB'):
    print('é bebida alcoolica')