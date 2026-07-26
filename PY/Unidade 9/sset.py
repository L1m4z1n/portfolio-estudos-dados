'''
Set

Estrutura:

meu_set = {valor,valor,valor,...}

Obs:.
- Não pode ter valores duplicados
- Não tem ordem fixa

'''

set_produtos = {'arroz','feijão','macarrão','atum'}
print(set_produtos)

'''
- Aplicação bem útil:
1. quantos clientes tivemos na loja?

'''

cpf_clientes = ['762.196.080-97','263.027.380-67','827.363.930-40','925.413.640-91']
set_cpf_clientes = set(cpf_clientes)
cpf_clientes_unicos = list(set_cpf_clientes)

print(cpf_clientes_unicos)
print(len(set_cpf_clientes))