# Node.js com serverless framework

> Este é o projeto de exemplo para o curso [Node.js com serverless framework](tbd) na Alura.

Este projeto tem como objetivo guiar seu aprendizado durante o curso, e para isso, ele está dividido em branches, cada um com um objetivo diferente. Cada branch representa um passo do curso, e você pode navegar entre elas para ver o código de cada etapa.

## Pré-requisitos

- Banco de dados mongodb - ex: atlas;
- Conta na AWS configurada com o aws configure;
- Conta no Serverless, conectada com a AWS via IAM.

## Executando localmente

Para executar o projeto localmente, será necesario startar o mongodb, execute: 

```bash
docker compose up -d
```

Com o mongodb rodando em background, você pode executar o comando que inicia o serverless localmente:

```bash
sls offline
```

Depois de executar o projeto, você pode acessar a aplicação em `http://localhost:3000`.

## Deploy

O deploy, como toda a gestão do serverless, pode ser feito via cli com o seguinte comando:

```bash
sls deploy --stage=prod
```

O deploy cria uma pasta chamada ".serverless" com as configurações do Serverless console(onde deve ser criado as variáveis) e com o respectivo stage. Automaticamente é gerado um **bucket(s3)** para o código da Lambda e uma "application" com o respectivo stage da **Lambda**.