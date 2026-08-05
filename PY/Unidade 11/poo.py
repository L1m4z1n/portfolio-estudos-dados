'''
# Introdução a Orientação a Objeto

### Regras Gerais:

- Tudo no Python é um objeto.
    - String é objeto
    - Lista é objeto
    - Dicionários são objetos
    ...

### Comparação Clássica

- Pense no Controle Remoto.
    - O Controle é um objeto
    - Cada botão dele é um comando, um método.
    - Cada método faz 1 ação específica
        - Por trás de cada método (dentro do controle) podem acontecer milhares de coisas quando você aperta 1 botão, mas no fundo você tá cagando pra isso, só quer que o botão faça o que você mandou quando você clicar no botão.

### Em termos práticos no Python

- Isso significa que todos eles tem métodos específicos, ou seja, já existe programado no Python várias coisas que você consegue fazer com ele.
    - Exemplo: Strings
        - Quando no Python criaram a string, eles programaram lá em algum lugar que texto[i] vai te dar o caracter na posição i do texto
        - Também criaram o método texto.upper() que torna toda a string em letra maiúscula
        - Também criaram o método texto.casefold() que coloca tudo em letra minúscula
        - E assim vai para tudo que temos no Python

- Em termos práticos, você já deve ter reparado que fazemos muito coisas do tipo variavel.método()
    - 'Produto {}: {} unidades vendidas'.format(produto, quantidade)
    - lista.append('ABC12304')
    - texto.count()
    - ...

### E para onde vamos com isso agora? Qual a grande vantagem?

- A vantagem é que agora vamos aprender a importar módulos novos
- Então tem MUITAS, mas MUITAS coisas que já estão prontas no Python que a gente não precisa programar do zero. A gente vai simplesmente importar e usar.
- E repare, quando a gente importar, o que na prática estaremos fazendo é importar 1 ou mais objetos que tem vários métodos já prontos para usarmos.

### Exemplo: E se eu quisesse pegar a data e hora atual para poder exibir uma mensagem de boas vindas para exibir uma mensagem de boas vindas com a data e hora -> Próxima Aula
'''