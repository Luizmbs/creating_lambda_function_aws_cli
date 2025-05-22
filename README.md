# creating_lambda_function_aws_cli
## Visão Geral
A função implementada é bem simples, faz apenas a conversão de moeda. O foco do reposítório é o estudo de como utilizar uma AWS Lambda Function através do AWS CLI.

## Como criar uma lambda function com o AWS CLI
### Pré-requisitos
Antes de tudo você precisa ter o AWS CLI instalado no seu computador. <br>
[Tutorial de instalação](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)<br>
Também é necessário ter as permissões para conta da AWS configuradas<br>

### Criando a lambda
A criação do lambda function é feita através do método create-function, que tem como parâmetro obrigatórios --function-name (nome da função) e --role (o ARN da role de execução da função), e tem também parâmetros opcionais, como: --runtime (linguagem do código) e --zipefile (arquivo zip contendo a função e suas dependências)
#### Exemplo
`aws lambda create-function --function-name nome_lambda --zip-file fileb://lambda_function.zip --runtime python3.12 --role...`

### Alterando a função 
Também é possível fazer o deploy de mudanças no código da lambda utilizando o comando update-function-code, que tem como parâmetro obrigatório apenas o --function-name, e diversos outros parâmetros opcionais, como: --zifile (envio do código alterado), --output (fomato do arquivo de saída) e --debug (retorno um log de debug).
#### Exemplo
`aws lambda update-function-code --function-name nome_lambda --zip-file fileb://lambda_function.zip`

### Alterando configuração
Além do código, também é possível fazer a alteração das configurações da lambda, para isso utilizamos o comando update-function-configuration, que tem como parâmetro obrigatório o --function-name e outros parâmetros opcionais, como: --role, --handler e --region, que alteram esses campos na configuração da função.

#### Exemplo
`aws lambda update-function-configuration --function-name nome_lambda --runtime python3.9`

### Invocando a lambda
Também é possível invocar a lambda através do AWS CLI, para isso utilizamos o comando invoke, que tem como parâmetros obrigatórios o --function-name e o caminho para um arquivo de saída. O comando conta também com parâmetros opcionais, como o payload que é a entrada da função

#### Exemplo
`aws lambda invoke --function-name nome_lambda --payload {"chave":"valor"} output.json`

### A documentação completa dos comando citados e muitos outros pode ser encontrada [aqui](https://docs.aws.amazon.com/cli/latest/reference/lambda/)

