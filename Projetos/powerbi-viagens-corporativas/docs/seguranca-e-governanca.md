# Segurança e Governança

Este documento descreve as principais decisões de **segurança, controle de acesso e governança de dados** adotadas no projeto **Dashboard de Viagens Corporativas**.

O projeto utiliza exclusivamente dados fictícios e foi desenvolvido com foco em demonstrar boas práticas de Business Intelligence, incluindo:

- controle de acesso;
- Row-Level Security (RLS);
- separação entre navegação e segurança;
- centralização de regras de acesso;
- proteção do escopo de dados visível;
- governança do modelo;
- documentação das decisões técnicas.

---

## 1. Objetivo

O objetivo da camada de segurança é garantir que diferentes usuários possam acessar o mesmo relatório, mas visualizar apenas os dados permitidos para seu perfil.

A solução foi estruturada para simular um cenário corporativo com três perfis principais:

- `Usuario`
- `Gestor`
- `Auditor`

O comportamento esperado é:

```text
Usuario
    ↓
Visualiza somente sua diretoria

Gestor
    ↓
Visualiza todas as diretorias

Auditor
    ↓
Visualiza todas as diretorias
```

---

## 2. Dados Utilizados

Todos os dados presentes no projeto são fictícios.

O repositório público não deve conter:

- dados pessoais reais;
- nomes reais de colaboradores;
- e-mails corporativos reais;
- URLs internas;
- credenciais;
- tokens;
- identificadores corporativos;
- documentos privados;
- informações operacionais reais.

A base utilizada no projeto está localizada em:

```text
data/viagens_ficticias.xlsx
```

---

## 3. Row-Level Security

O projeto utiliza **Row-Level Security (RLS) dinâmico**.

O RLS permite controlar quais linhas do modelo cada usuário pode visualizar.

A lógica utiliza a identificação do usuário autenticado através de:

```DAX
USERPRINCIPALNAME()
```

O usuário identificado é comparado com os registros da tabela:

```text
Acesso_Usuarios
```

---

## 4. Tabela de Acesso

A tabela `Acesso_Usuarios` centraliza as permissões utilizadas pelo RLS.

Sua estrutura principal é:

```text
Email
Diretoria
Perfil
```

Exemplo fictício:

```text
ana.tecnologia@empresa.com | DIR_TECNOLOGIA | Usuario
bruno.financeiro@empresa.com | DIR_FINANCEIRA | Usuario
carla.comercial@empresa.com | DIR_COMERCIAL | Usuario
diego.operacoes@empresa.com | DIR_OPERACOES | Usuario
elisa.adm@empresa.com | DIR_ADMINISTRATIVA | Usuario
gestor@empresa.com | TODAS | Gestor
auditor@empresa.com | TODAS | Auditor
```

Essa tabela utiliza exclusivamente identidades fictícias.

---

## 5. Perfis de Acesso

### Usuario

O perfil `Usuario` possui acesso somente aos dados relacionados à diretoria associada ao seu cadastro.

Exemplo:

```text
ana.tecnologia@empresa.com
        ↓
DIR_TECNOLOGIA
        ↓
GER_DADOS
GER_SISTEMAS
```

O usuário não deve visualizar dados de outras diretorias.

### Gestor

O perfil `Gestor` possui acesso total às diretorias do modelo.

Esse perfil simula um usuário com necessidade de visão consolidada.

### Auditor

O perfil `Auditor` também possui acesso total às diretorias.

Esse perfil representa um cenário de análise, validação e auditoria dos dados.

---

## 6. Fluxo de Segurança

O fluxo utilizado no projeto pode ser representado da seguinte forma:

```text
USERPRINCIPALNAME()
        ↓
Acesso_Usuarios
        ↓
Perfil + Diretoria Permitida
        ↓
Dim_Centro_Custo
        ↓
Base_Geral
Diarias_Raw
Cancelados_Raw
Nao_Voados_Raw
```

A regra de segurança é centralizada na dimensão:

```text
Dim_Centro_Custo
```

---

## 7. Motivo para Aplicar o RLS na Dimensão

O RLS não foi duplicado em cada tabela fato.

Em vez disso, a regra é aplicada em:

```text
Dim_Centro_Custo
```

Essa dimensão está relacionada às principais tabelas utilizadas no relatório.

O filtro aplicado pela segurança é propagado para:

```text
Base_Geral
Diarias_Raw
Cancelados_Raw
Nao_Voados_Raw
```

Essa abordagem reduz duplicações e centraliza a regra organizacional.

---

## 8. Regra do RLS Dinâmico

A regra implementada utiliza a identificação do usuário e consulta sua permissão na tabela `Acesso_Usuarios`.

```DAX
VAR UsuarioAtual =
    USERPRINCIPALNAME()

VAR PerfilAtual =
    CALCULATE(
        MAX(Acesso_Usuarios[Perfil]),
        FILTER(
            ALL(Acesso_Usuarios),
            Acesso_Usuarios[Email] = UsuarioAtual
        )
    )

VAR DiretoriasPermitidas =
    CALCULATETABLE(
        VALUES(Acesso_Usuarios[Diretoria]),
        FILTER(
            ALL(Acesso_Usuarios),
            Acesso_Usuarios[Email] = UsuarioAtual
        )
    )

VAR AcessoTotal =
    PerfilAtual = "Gestor"
        || PerfilAtual = "Auditor"

RETURN
    AcessoTotal
        || Dim_Centro_Custo[Diretoria] IN DiretoriasPermitidas
```

---

## 9. Comportamento Esperado

### Usuário comum

Para:

```text
ana.tecnologia@empresa.com
```

o resultado esperado é:

```text
Perfil: Usuario
Diretoria Permitida: DIR_TECNOLOGIA
```

O usuário deve visualizar somente:

```text
DIR_TECNOLOGIA
GER_DADOS
GER_SISTEMAS
```

### Gestor

Para:

```text
gestor@empresa.com
```

o resultado esperado é:

```text
Perfil: Gestor
Diretoria Permitida: TODAS
```

O usuário deve visualizar todas as diretorias.

### Auditor

Para:

```text
auditor@empresa.com
```

o resultado esperado é:

```text
Perfil: Auditor
Diretoria Permitida: TODAS
```

O usuário também deve visualizar todas as diretorias.

### Usuário não cadastrado

Para um usuário que não existe em `Acesso_Usuarios`, o comportamento esperado é:

```text
Perfil: Sem acesso
Diretoria Permitida: SEM ACESSO
```

O modelo deve impedir a visualização dos dados protegidos.

---

## 10. Medidas de Validação

Algumas medidas foram criadas especificamente para validar o funcionamento do RLS.

### Usuário Logado

```DAX
Usuario Logado =
USERPRINCIPALNAME()
```

### Perfil do Usuário

```DAX
Perfil Usuario =
VAR UsuarioAtual =
    USERPRINCIPALNAME()

VAR PerfilEncontrado =
    CALCULATE(
        MAX(Acesso_Usuarios[Perfil]),
        FILTER(
            ALL(Acesso_Usuarios),
            Acesso_Usuarios[Email] = UsuarioAtual
        )
    )

RETURN
    COALESCE(
        PerfilEncontrado,
        "Sem acesso"
    )
```

### Diretoria Permitida

```DAX
Diretoria Permitida =
VAR UsuarioAtual =
    USERPRINCIPALNAME()

VAR PerfilAtual =
    [Perfil Usuario]

VAR DiretoriasUsuario =
    CALCULATETABLE(
        VALUES(Acesso_Usuarios[Diretoria]),
        FILTER(
            ALL(Acesso_Usuarios),
            Acesso_Usuarios[Email] = UsuarioAtual
        )
    )

RETURN
    SWITCH(
        TRUE(),
        PerfilAtual = "Gestor", "TODAS",
        PerfilAtual = "Auditor", "TODAS",
        PerfilAtual = "Sem acesso", "SEM ACESSO",
        CONCATENATEX(
            DiretoriasUsuario,
            Acesso_Usuarios[Diretoria],
            ", "
        )
    )
```

### Status do RLS

```DAX
Status RLS =
IF(
    [Perfil Usuario] = "Sem acesso",
    "Sem acesso",
    "Dinâmico Ativo"
)
```

### Quantidade de Diretorias Visíveis

```DAX
Qtd Diretorias Visiveis =
DISTINCTCOUNT(
    Dim_Centro_Custo[Diretoria]
)
```

### Quantidade de Centros de Custo Visíveis

```DAX
Qtd Centros Visiveis =
DISTINCTCOUNT(
    Dim_Centro_Custo[Centro_Custo]
)
```

---

## 11. Página Técnica de Segurança

O relatório possui uma página específica para demonstrar o funcionamento do RLS.

Essa página apresenta:

- usuário autenticado;
- perfil;
- diretoria permitida;
- status do RLS;
- perfis de acesso;
- fluxo da segurança;
- tabela com os dados visíveis;
- indicadores do escopo disponível.

A página é utilizada como recurso técnico e de validação.

Ela permanece fora da navegação analítica principal e pode ser acessada por meio de um botão específico.

---

## 12. Segurança x Navegação

A navegação do relatório não é utilizada como mecanismo de segurança.

Essa separação é importante.

```text
Navegação = experiência do usuário
RLS = segurança dos dados
```

Ocultar uma página ou remover um botão não substitui o RLS.

O controle do acesso aos dados deve ocorrer no modelo.

---

## 13. Relacionamentos e Propagação do Filtro

A dimensão `Dim_Centro_Custo` possui relacionamentos com as principais tabelas do modelo.

Estrutura conceitual:

```text
Dim_Centro_Custo
      │
      ├──→ Base_Geral
      ├──→ Diarias_Raw
      ├──→ Cancelados_Raw
      └──→ Nao_Voados_Raw
```

Os relacionamentos permitem que o filtro de segurança seja propagado para as tabelas fato.

---

## 14. Princípio de Menor Acesso

O projeto segue conceitualmente o princípio de fornecer somente o acesso necessário.

Um usuário comum possui acesso apenas à sua diretoria.

Perfis com visão ampliada são definidos explicitamente.

Esse comportamento evita que o relatório dependa de filtros manuais para restringir dados.

---

## 15. Comportamento para Usuários Sem Cadastro

Usuários não cadastrados na tabela `Acesso_Usuarios` não recebem automaticamente acesso aos dados.

O comportamento esperado é:

```text
Usuário não encontrado
        ↓
Perfil = Sem acesso
        ↓
Nenhuma diretoria autorizada
```

Essa abordagem segue uma lógica de acesso restritivo por padrão.

---

## 16. Governança do Modelo

A governança do projeto foi baseada em alguns princípios.

### Centralização dos filtros

Filtros de período utilizam:

```text
Dim_Trimestre
```

Filtros organizacionais utilizam:

```text
Dim_Centro_Custo
```

### Separação entre fatos e dimensões

As tabelas operacionais armazenam os registros.

As dimensões centralizam os atributos utilizados em filtros e relacionamentos.

### Centralização da segurança

A regra do RLS é aplicada na dimensão organizacional.

Isso reduz a necessidade de repetir regras em várias tabelas.

### Padronização

Os nomes de diretoria e centro de custo foram padronizados antes da construção do modelo.

Essa padronização melhora a consistência de:

- filtros;
- relacionamentos;
- análises;
- segurança.

---

## 17. Exportação de Dados

A exportação deve respeitar o escopo de dados permitido ao usuário.

A decisão de liberar ou restringir exportação faz parte da governança da solução e deve ser revisada conforme o ambiente de publicação.

Para este projeto de portfólio, a recomendação é demonstrar apenas dados fictícios e evitar qualquer dependência de informações privadas ou externas.

---

## 18. Auditoria Antes da Publicação

Antes da publicação do projeto, devem ser verificadas referências que não pertencem à versão pública.

A auditoria deve procurar por:

```text
URLs internas
SharePoint
nomes reais
e-mails reais
identificadores reais
credenciais
tokens
siglas corporativas
arquivos privados
fontes externas não fictícias
```

Também devem ser revisados:

- Power Query;
- medidas DAX;
- colunas calculadas;
- filtros;
- bookmarks;
- páginas ocultas;
- botões;
- títulos;
- tooltips;
- visuais HTML;
- nomes de queries;
- parâmetros;
- conexões de dados.

---

## 19. Testes de Segurança

Os principais cenários de teste são:

### Cenário 1 — Usuário de Tecnologia

```text
Usuário: ana.tecnologia@empresa.com
Perfil: Usuario
Esperado: somente DIR_TECNOLOGIA
```

### Cenário 2 — Usuário Financeiro

```text
Usuário: bruno.financeiro@empresa.com
Perfil: Usuario
Esperado: somente DIR_FINANCEIRA
```

### Cenário 3 — Gestor

```text
Usuário: gestor@empresa.com
Perfil: Gestor
Esperado: todas as diretorias
```

### Cenário 4 — Auditor

```text
Usuário: auditor@empresa.com
Perfil: Auditor
Esperado: todas as diretorias
```

### Cenário 5 — Usuário não cadastrado

```text
Usuário: usuario.nao.cadastrado@empresa.com
Perfil esperado: Sem acesso
Esperado: nenhum dado protegido
```

---

## 20. Validação nas Páginas

O RLS deve ser validado em todas as páginas relevantes.

Exemplos:

```text
Visão Geral
Por Diretoria
Detalhes por Diretoria
Prazos
Cancelados e Não Voados
Evolução Trimestral
Segurança / RLS
```

A validação não deve se limitar à `Base_Geral`.

Também deve ser verificado o comportamento de:

```text
Diarias_Raw
Cancelados_Raw
Nao_Voados_Raw
```

---

## 21. Separação entre Ambiente Público e Ambiente Privado

A versão publicada no GitHub deve utilizar apenas:

```text
dados fictícios
documentação pública
screenshots do projeto fictício
arquivo PBIX sanitizado
```

Qualquer arquivo ou conexão associada a ambientes privados deve permanecer fora do repositório.

---

## 22. Boas Práticas Adotadas

Entre as principais práticas utilizadas estão:

- RLS dinâmico;
- identificação do usuário com `USERPRINCIPALNAME()`;
- tabela centralizada de permissões;
- aplicação do RLS em dimensão;
- separação entre navegação e segurança;
- bloqueio conceitual de usuários não cadastrados;
- dados exclusivamente fictícios;
- modelo dimensional;
- documentação das regras;
- validação com diferentes perfis;
- auditoria antes da publicação.

---

## 23. Limitações

O projeto é uma implementação educacional e de portfólio.

A tabela `Acesso_Usuarios` utiliza identidades fictícias e tem como objetivo demonstrar a lógica de segurança.

Em um ambiente corporativo real, a estratégia de identidade, grupos, permissões, publicação, compartilhamento e governança deve seguir as políticas e ferramentas oficiais da organização.

---

## 24. Resumo

A arquitetura de segurança do projeto pode ser resumida como:

```text
Usuário autenticado
        ↓
USERPRINCIPALNAME()
        ↓
Acesso_Usuarios
        ↓
Perfil + Diretoria
        ↓
RLS em Dim_Centro_Custo
        ↓
Propagação para as tabelas fato
        ↓
Dados permitidos no dashboard
```

O objetivo é garantir que a segurança esteja integrada ao modelo de dados, e não apenas à interface visual do relatório.
