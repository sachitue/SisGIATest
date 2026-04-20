# Funcionalidade de Importação/Exportação de Funcionários via Excel

## Resumo das Alterações

Implementei a funcionalidade para substituir a listagem tradicional de funcionários por botões que permitem:
1. Importar dados de funcionários através de um arquivo Excel
2. Exportar dados de funcionários para um arquivo Excel

## Arquivos Modificados

### 1. `RH/views.py`
- Adicionei funções para exportar funcionários para Excel (`export_funcionarios_excel`)
- Adicionei funções para importar funcionários a partir de Excel (`import_funcionarios_excel`)
- Modifiquei a função `funcionarios_list` para lidar com as requisições de importação/exportação
- Adicionei as bibliotecas necessárias: `pandas`, `BytesIO`

### 2. `RH/templates/rh/funcionarios_list.html`
- Substituí a interface de listagem por seções dedicadas para importação e exportação
- Adicionei um formulário para upload de arquivos Excel
- Adicionei um botão para download dos dados em Excel
- Mantive os filtros existentes para pesquisa

### 3. `requirements.txt`
- Adicionei as dependências necessárias: `pandas`, `openpyxl`, `xlsxwriter`

## Funcionalidades Implementadas

### Importação de Funcionários (Upload Excel)
- Permite fazer upload de arquivos `.xlsx` ou `.xls`
- Processa os dados e cria novos registros de funcionários
- Atualiza registros existentes com base no número do BI
- Mostra mensagens de sucesso/erro após a importação

### Exportação de Funcionários (Download Excel)
- Gera um arquivo Excel com todos os funcionários filtrados
- Inclui informações como: ID, Nome, Apelido, BI, NIF, Email, Cargo, Categoria, Departamento, Telefone, Tipo de Funcionário, Status, Datas de Admissão e Nascimento
- O arquivo é baixado automaticamente pelo navegador

## Como Usar

1. **Para importar funcionários:**
   - Clique na seção "Importar Funcionários via Excel"
   - Selecione um arquivo Excel com os dados dos funcionários
   - Clique em "Importar Funcionários"

2. **Para exportar funcionários:**
   - Clique na seção "Exportar Funcionários para Excel"
   - Clique em "Exportar para Excel"
   - O arquivo será baixado automaticamente

## Formato do Arquivo Excel para Importação

O arquivo deve conter as seguintes colunas:
- Nome
- Apelido
- BI
- NIF
- Email
- Cargo
- Departamento
- Telefone
- Tipo Funcionário

## Benefícios

- Facilita a gestão em massa de funcionários
- Reduz o tempo necessário para cadastrar muitos funcionários
- Permite backup dos dados em formato Excel
- Mantém a funcionalidade de pesquisa e filtragem existente