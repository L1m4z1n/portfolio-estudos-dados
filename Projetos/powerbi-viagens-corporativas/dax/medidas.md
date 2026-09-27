# Medidas DAX

Este documento reúne as principais medidas DAX utilizadas no projeto **Dashboard de Viagens Corporativas**.

As medidas são calculadas de acordo com o contexto de filtro aplicado no Power BI, principalmente por meio das dimensões:

- `Dim_Trimestre`
- `Dim_Centro_Custo`

O projeto também utiliza medidas específicas para análise trimestral, indicadores operacionais e implementação de Row-Level Security (RLS).

---

## 1. Indicadores Gerais

### Soma Valor Total

Calcula o valor total das despesas consolidadas na tabela `Base_Geral`.

```DAX
Soma Valor Total =
SUM(Base_Geral[Valor_Total])
```

#### Uso no dashboard

- Card de valor total
- Gráficos por diretoria
- Gráficos por tipo de despesa
- Evolução trimestral
- Validação de acesso via RLS

---

### Quantidade Total

Conta a quantidade de registros presentes na tabela consolidada.

```DAX
Qtd_Total =
COUNTROWS(Base_Geral)
```

#### Uso no dashboard

- Card de quantidade de solicitações
- Comparações entre diretorias
- Comparações por período
- Validação do volume de dados visíveis

---

## 2. Indicadores por Tipo de Despesa

### Valor Aéreo

Calcula o valor total das despesas classificadas como transporte aéreo.

```DAX
Valor Aereo =
CALCULATE(
    [Soma Valor Total],
    Base_Geral[Tipo_Despesa] = "Aereo"
)
```

---

### Quantidade Aéreo

Conta os registros classificados como transporte aéreo.

```DAX
Qtd Aereo =
CALCULATE(
    [Qtd_Total],
    Base_Geral[Tipo_Despesa] = "Aereo"
)
```

---

### Valor Hospedagem

Calcula o valor total gasto com hospedagem.

```DAX
Valor Hospedagem =
CALCULATE(
    [Soma Valor Total],
    Base_Geral[Tipo_Despesa] = "Hospedagem"
)
```

---

### Quantidade Hospedagem

Conta os registros classificados como hospedagem.

```DAX
Qtd Hospedagem =
CALCULATE(
    [Qtd_Total],
    Base_Geral[Tipo_Despesa] = "Hospedagem"
)
```

---

### Valor Uber

Calcula o valor total gasto com transporte urbano.

```DAX
Valor Uber =
CALCULATE(
    [Soma Valor Total],
    Base_Geral[Tipo_Despesa] = "Uber"
)
```

---

### Quantidade Uber

Conta os registros classificados como Uber.

```DAX
Qtd Uber =
CALCULATE(
    [Qtd_Total],
    Base_Geral[Tipo_Despesa] = "Uber"
)
```

---

## 3. Diárias

As diárias permanecem disponíveis em uma tabela específica do modelo.

### Valor Total Diárias

```DAX
Valor Total Diarias =
SUM(Diarias_Raw[Valor_Total])
```

---

### Quantidade de Diárias

```DAX
Qtd Diarias =
COUNTROWS(Diarias_Raw)
```

#### Uso no dashboard

- Card de valor de diárias
- Card de quantidade de registros
- Análises trimestrais
- Análises por diretoria

---

## 4. Cancelamentos

### Quantidade de Cancelados

Conta a quantidade de solicitações canceladas.

```DAX
Quantidade Cancelados =
COUNTROWS(Cancelados_Raw)
```

---

### Valor Cancelado

Calcula o valor total associado às solicitações canceladas.

```DAX
Valor Cancelado =
SUM(Cancelados_Raw[Valor_Total])
```

#### Uso no dashboard

- Página de Cancelados e Não Voados
- Ranking por diretoria
- Indicadores operacionais

---

## 5. Passagens Não Utilizadas

### Quantidade de Não Voados

Conta a quantidade de registros de passagens emitidas e não utilizadas.

```DAX
Quantidade Nao Voados =
COUNTROWS(Nao_Voados_Raw)
```

---

### Valor Não Voado

Calcula o valor total associado às passagens não utilizadas.

```DAX
Valor Nao Voado =
SUM(Nao_Voados_Raw[Valor_Total])
```

#### Uso no dashboard

- Alertas da Visão Geral
- Página de Cancelados e Não Voados
- Análise por centro de custo
- Análise por viajante

---

## 6. Comparativo Trimestral

As medidas trimestrais removem o filtro atual de trimestre e aplicam explicitamente o período desejado.

Isso permite comparar os períodos independentemente do contexto atual do visual.

### Valor Total T1

```DAX
Valor Total T1 =
CALCULATE(
    [Soma Valor Total],
    REMOVEFILTERS(Dim_Trimestre),
    Dim_Trimestre[Trimestre] = "Primeiro Trimestre"
)
```

---

### Valor Total T2

```DAX
Valor Total T2 =
CALCULATE(
    [Soma Valor Total],
    REMOVEFILTERS(Dim_Trimestre),
    Dim_Trimestre[Trimestre] = "Segundo Trimestre"
)
```

---

### Valor Total T3

```DAX
Valor Total T3 =
CALCULATE(
    [Soma Valor Total],
    REMOVEFILTERS(Dim_Trimestre),
    Dim_Trimestre[Trimestre] = "Terceiro Trimestre"
)
```

---

### Valor Total T4

```DAX
Valor Total T4 =
CALCULATE(
    [Soma Valor Total],
    REMOVEFILTERS(Dim_Trimestre),
    Dim_Trimestre[Trimestre] = "Quarto Trimestre"
)
```

---

### Variação T1 x T4

Calcula a variação percentual entre o primeiro e o quarto trimestre.

```DAX
Variacao T1 T4 % =
VAR ValorInicial =
    [Valor Total T1]

VAR ValorFinal =
    [Valor Total T4]

RETURN
    DIVIDE(
        ValorFinal - ValorInicial,
        ValorInicial
    )
```

#### Interpretação

- Valor positivo: crescimento entre T1 e T4
- Valor negativo: redução entre T1 e T4
- Valor igual a zero: estabilidade

---

### Ranking de Variação

Classifica as diretorias pela variação entre o primeiro e o quarto trimestre.

```DAX
Ranking Variacao =
RANKX(
    ALLSELECTED(Dim_Centro_Custo[Diretoria]),
    [Variacao T1 T4 %],
    ,
    DESC,
    DENSE
)
```

#### Uso no dashboard

Utilizada na página **Evolução Trimestral** para destacar as diretorias com maiores variações no período.

---

## 7. Segurança e Row-Level Security

O projeto utiliza Row-Level Security (RLS) dinâmico para restringir os dados visualizados de acordo com o usuário autenticado.

A identificação do usuário é realizada através da função:

`USERPRINCIPALNAME()`.

---

### Usuário Logado

Retorna a identificação do usuário autenticado no Power BI.

```DAX
Usuario Logado =
USERPRINCIPALNAME()
```

---

### Perfil do Usuário

Consulta a tabela `Acesso_Usuarios` para identificar o perfil associado ao usuário autenticado.

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

Os perfis utilizados no projeto são:

- `Usuario`
- `Gestor`
- `Auditor`

---

### Diretoria Permitida

Identifica a diretoria que o usuário possui permissão para visualizar.

Gestores e auditores possuem acesso às diretorias previstas pela regra de segurança.

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

---

### Status do RLS

Retorna o status utilizado na página técnica de segurança.

```DAX
Status RLS =
IF(
    [Perfil Usuario] = "Sem acesso",
    "Sem acesso",
    "Dinâmico Ativo"
)
```

---

### Quantidade de Diretorias Visíveis

Conta quantas diretorias estão disponíveis no contexto atual de segurança.

```DAX
Qtd Diretorias Visiveis =
DISTINCTCOUNT(
    Dim_Centro_Custo[Diretoria]
)
```

Para um usuário comum, o resultado esperado é uma única diretoria.

Para perfis com acesso total, o resultado corresponde ao total de diretorias disponíveis no modelo.

---

### Quantidade de Centros de Custo Visíveis

Conta os centros de custo disponíveis após a aplicação dos filtros e do RLS.

```DAX
Qtd Centros Visiveis =
DISTINCTCOUNT(
    Dim_Centro_Custo[Centro_Custo]
)
```

---

### Descrição do Acesso

Gera uma descrição dinâmica de acordo com o perfil autenticado.

```DAX
Descricao Acesso =
VAR PerfilAtual =
    [Perfil Usuario]

VAR DiretoriaAtual =
    [Diretoria Permitida]

RETURN
    SWITCH(
        TRUE(),

        PerfilAtual = "Usuario",
            "Exibindo somente os dados da diretoria "
                & DiretoriaAtual
                & " permitidos para este usuário.",

        PerfilAtual = "Gestor",
            "Perfil Gestor: acesso liberado para todas as diretorias.",

        PerfilAtual = "Auditor",
            "Perfil Auditor: acesso completo aos dados para análise.",

        "Usuário sem permissão cadastrada."
    )
```

Essa medida é utilizada na página **Segurança / RLS**.

---

## 8. Regra do RLS Dinâmico

A função `RLS_Dinamico` é aplicada sobre a tabela `Dim_Centro_Custo`.

A regra utilizada é:

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

### Fluxo da segurança

```text
USERPRINCIPALNAME()
        ↓
Acesso_Usuarios
        ↓
Dim_Centro_Custo
        ↓
Tabelas fato
```

O filtro aplicado em `Dim_Centro_Custo` é propagado para as tabelas relacionadas através dos relacionamentos do modelo.

---

## 9. Dimensão de Trimestre

A dimensão utilizada para controlar os períodos foi criada da seguinte forma:

```DAX
Dim_Trimestre =
DATATABLE(
    "Trimestre", STRING,
    "Ordem", INTEGER,
    {
        {"Primeiro Trimestre", 1},
        {"Segundo Trimestre", 2},
        {"Terceiro Trimestre", 3},
        {"Quarto Trimestre", 4}
    }
)
```

A coluna `Trimestre` é ordenada pela coluna `Ordem`.

Isso garante a sequência:

```text
T1 → T2 → T3 → T4
```

nos gráficos temporais.

---

## 10. Visuais HTML

Alguns elementos do dashboard foram desenvolvidos utilizando medidas DAX que retornam conteúdo HTML.

Essas medidas são utilizadas principalmente para:

- cards personalizados;
- ranking de variação por diretoria;
- página de segurança e RLS;
- indicadores de perfil e acesso;
- fluxo visual da arquitetura de segurança;
- tabela de validação do RLS.

Os visuais HTML são utilizados como camada de apresentação e consomem as mesmas medidas analíticas descritas anteriormente.

Entre as principais medidas HTML utilizadas estão:

- `HTML Ranking Variacao Diretorias`
- `HTML Card Usuario`
- `HTML Card Perfil`
- `HTML Card Diretoria`
- `HTML Card Status RLS`
- `HTML Banner RLS`
- `HTML Destaque RLS`
- `HTML Perfis Acesso`
- `HTML Fluxo Seguranca`
- `HTML Aviso Acesso`
- `HTML Tabela Validacao RLS`

Os códigos HTML completos permanecem implementados diretamente no arquivo Power BI para evitar que este documento se torne excessivamente extenso.

---

## 11. Observações sobre o Modelo

- `Base_Geral` concentra as principais despesas utilizadas no dashboard.
- `Cancelados_Raw` permanece como tabela operacional específica.
- `Nao_Voados_Raw` permanece como tabela operacional específica.
- `Diarias_Raw` também pode ser utilizada diretamente em indicadores específicos.
- Os filtros de trimestre utilizam `Dim_Trimestre`.
- Os filtros organizacionais utilizam `Dim_Centro_Custo`.
- Os relacionamentos utilizam as dimensões para propagação do contexto de filtro.
- As medidas respondem automaticamente aos filtros aplicados pelo relatório.
- O RLS utiliza `Dim_Centro_Custo` como ponto de propagação da segurança para as tabelas fato.

---

## 12. Resumo

As medidas DAX do projeto suportam quatro principais grupos de análise:

1. **Indicadores financeiros**
   - valores;
   - volumes;
   - tipos de despesa.

2. **Indicadores operacionais**
   - cancelamentos;
   - não voados;
   - diárias.

3. **Análise temporal**
   - valores por trimestre;
   - evolução;
   - variação entre períodos;
   - ranking por diretoria.

4. **Segurança e governança**
   - identificação do usuário;
   - perfil de acesso;
   - diretoria permitida;
   - RLS dinâmico;
   - validação do escopo de dados visível.