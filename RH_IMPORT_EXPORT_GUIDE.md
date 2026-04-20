# Guia de Importação e Exportação de Funcionários via Excel

## Visão Geral

Este guia explica como utilizar as novas funcionalidades de importação e exportação de dados de funcionários através de arquivos Excel na aplicação College Management System.

## Funcionalidades Disponíveis

### 1. Importação de Funcionários (Upload Excel)
Permite carregar dados de funcionários a partir de um arquivo Excel, criando novos registros ou atualizando registros existentes.

### 2. Exportação de Funcionários (Download Excel)
Permite baixar todos os dados dos funcionários em formato Excel para backup ou análise.

## Como Importar Funcionários

### Passo 1: Acessar a Página de Gestão de Funcionários
1. Faça login no sistema
2. Navegue até a seção de Recursos Humanos (RH)
3. Clique em "Gestão de Funcionários"

### Passo 2: Preparar o Arquivo Excel
1. Crie um arquivo Excel com as seguintes colunas obrigatórias:
   - **Nome** (texto)
   - **Apelido** (texto)
   - **BI** (número do bilhete de identidade - campo único)
   - **NIF** (número de identificação fiscal)
   - **Email** (endereço de email institucional)
   - **Cargo** (cargo do funcionário)
   - **Departamento** (departamento onde trabalha)
   - **Telefone** (número de contato principal)
   - **Tipo Funcionário** (NACIONAL ou EXPATRIADO)

2. Preencha os dados dos funcionários nas linhas correspondentes

### Passo 3: Realizar o Upload
1. Na seção "Importar Funcionários via Excel", clique no botão "Escolher Arquivo"
2. Selecione o arquivo Excel preparado
3. Clique no botão "Importar Funcionários"
4. Aguarde o processamento e verifique as mensagens de sucesso/erro

### Regras de Importação
- Funcionários com BI já existente serão atualizados com os novos dados
- Funcionários com BI não encontrado serão criados como novos registros
- Campos em branco serão ignorados
- O sistema mostrará mensagens de erro para linhas com problemas

## Como Exportar Funcionários

### Passo 1: Acessar a Página de Gestão de Funcionários
1. Faça login no sistema
2. Navegue até a seção de Recursos Humanos (RH)
3. Clique em "Gestão de Funcionários"

### Passo 2: Realizar a Exportação
1. Na seção "Exportar Funcionários para Excel", clique no botão "Exportar para Excel"
2. O arquivo será baixado automaticamente com o nome "funcionarios.xlsx"

### Dados Incluídos na Exportação
O arquivo Excel exportado conterá as seguintes informações:
- ID do funcionário
- Nome
- Apelido
- BI
- NIF
- Email
- Cargo
- Categoria
- Departamento
- Telefone
- Tipo de Funcionário
- Status (Ativo, Inativo, Aposentado, etc.)
- Data de Admissão
- Data de Nascimento

### Filtros na Exportação
A exportação respeita os filtros aplicados na tela:
- Filtro por nome/apelido
- Filtro por cargo
- Filtro por status
- Filtro por tipo de funcionário

## Dicas e Boas Práticas

### Para Importação
1. Sempre verifique a integridade dos dados antes de importar
2. Certifique-se de que o campo BI é único para cada funcionário
3. Use o modelo de exemplo fornecido como base
4. Faça backup dos dados antes de realizar importações em massa
5. Verifique as mensagens de erro após a importação e corrija os problemas identificados

### Para Exportação
1. Use os filtros para exportar apenas os dados necessários
2. O arquivo exportado pode ser usado para análise em outras ferramentas
3. Mantenha cópias de segurança regulares dos dados exportados

## Solução de Problemas

### Problemas Comuns na Importação
1. **"Erro ao importar o arquivo"**: Verifique se o arquivo está em formato Excel válido (.xlsx ou .xls)
2. **"Linha X: ..."**: Verifique os dados da linha indicada no arquivo
3. **Dados não atualizados**: Certifique-se de que o campo BI corresponde exatamente ao registro existente

### Problemas Comuns na Exportação
1. **Arquivo não baixado**: Verifique as configurações de bloqueio de downloads do navegador
2. **Dados incompletos**: Verifique se os filtros aplicados estão corretos

## Suporte

Para suporte adicional, entre em contato com o administrador do sistema ou consulte a documentação técnica.