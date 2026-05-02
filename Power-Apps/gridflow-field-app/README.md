# GridFlow Field App

O **GridFlow Field App** é um projeto desenvolvido em Microsoft Power Apps para simular uma solução de registro de atendimentos técnicos em campo.

A ideia principal do app é resolver um problema comum em operações externas: o profissional precisa preencher informações durante o atendimento, mas nem sempre está em um local com conexão estável com a internet.

Pensando nisso, o app permite preencher o formulário pelo celular, salvar os dados localmente quando estiver offline e enviar os registros depois, quando a conexão for restabelecida.

## Objetivo do projeto

O objetivo foi criar um protótipo funcional que demonstrasse como o Power Apps pode ser usado para digitalizar um processo de campo, reduzindo a dependência de formulários online e evitando perda de informações em locais sem internet.

O projeto também serviu como prática de integração entre Power Apps e SharePoint, além de trabalhar conceitos de armazenamento local, navegação entre telas e organização de formulários em etapas.

## Funcionalidades

- Tela inicial com identificação do status de conexão.
- Formulário dividido em etapas.
- Registro de dados gerais do atendimento.
- Seleção de técnicos responsáveis.
- Registro de código da ordem de serviço.
- Registro de unidade atendida.
- Registro de região e endereço.
- Registro de data do atendimento.
- Registro do tipo de medição.
- Registro das informações do medidor retirado.
- Registro das informações do medidor instalado.
- Upload de imagens.
- Campo para descrição da situação encontrada em campo.
- Envio online diretamente para uma lista do SharePoint.
- Salvamento local quando o usuário está sem conexão.
- Tela para visualizar registros salvos.
- Envio posterior dos dados pendentes quando a internet volta.

## Tecnologias utilizadas

- Microsoft Power Apps
- SharePoint Lists
- Power Platform
- Excel
- Armazenamento local no aplicativo
- Conectores do Power Apps

## Fluxo da aplicação

O funcionamento do app foi pensado em dois cenários principais.

### Cenário online

Quando o usuário está com conexão ativa, ele preenche o formulário normalmente e os dados são enviados direto para uma lista do SharePoint.

### Cenário offline

Quando o usuário está sem conexão, o app salva as informações localmente. Depois, quando a conexão é restabelecida, o usuário pode acessar a tela de registros salvos e enviar os dados pendentes para o SharePoint.

## Estrutura do projeto

```txt
gridflow-field-app/
├── README.md
├── prints/
│   ├── 01-tela-inicial-online.jpeg
│   ├── 02-formulario-dados-gerais.jpeg
│   ├── 03-tela-carregamento-gridflow.jpeg
│   ├── 04-formulario-tipo-medicao.jpeg
│   ├── 05-formulario-medidor-retirado.jpeg
│   ├── 06-formulario-medidor-instalado.jpeg
│   ├── 07-formulario-foto-e-envio.jpeg
│   └── 08-registros-salvos-offline.jpeg
└── docs/
    └── fluxo-da-aplicacao.md

## Demonstração

A demonstração em vídeo do funcionamento do app está disponível no LinkedIn:

[Ver demonstração no LinkedIn](https://www.linkedin.com/posts/gabrielimalmeida_powerapps-powerplataform-sharepoint-ugcPost-7456357059081453568-XHUB)    