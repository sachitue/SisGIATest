# Importação de Funcionários via Excel - Resumo

## Visão Geral

Este documento descreve o processo de importação de dados de funcionários a partir do arquivo "PLANILHAS funcionários-2025- IP.xlsx" para o sistema College Management.

## Arquivo de Origem

- **Nome do arquivo**: PLANILHAS funcionários-2025- IP.xlsx
- **Localização**: Diretório raiz do projeto
- **Total de funcionários identificados**: 77

## Estrutura do Arquivo Excel

O arquivo contém as seguintes colunas relevantes:
- Nome completo
- N.º B.I (Documento de identificação único)
- N.º Agente
- Data de Nascimento
- Género
- Nível Académico
- Curso de Formação
- Ano de conclusão da formação actual
- Tempo de serviço na Função Pública
- Tempo de serviço no Ensino Superior
- Ano de Ingresso na categoria Actual
- Função/Cargo
- DEI a que pertence (Departamento)
- Regime de Trabalho
- Endereço Electrónico
- Telefone

## Processo de Importação

### 1. Análise do Arquivo
- Identificação da linha de cabeçalho (linha 9)
- Remoção de linhas de cabeçalho duplicadas
- Validação de dados obrigatórios (Nome e BI)

### 2. Mapeamento de Campos
Os dados do Excel foram mapeados para os campos do modelo Funcionario:
- Nome completo → nome
- N.º B.I → bi
- Data de Nascimento → data_nascimento
- Género → genero (com conversão Masculino/Feminino para M/F)
- Nível Académico → grau_academico (com conversão para valores do sistema)
- Departamento → departamento (com mapeamento para valores do sistema)
- Regime de Trabalho → regime_trabalho (com mapeamento para valores do sistema)
- E outros campos relevantes

### 3. Execução da Importação
- Criado comando de gerenciamento Django: `import_funcionarios_excel`
- Implementado mecanismo de detecção de funcionários existentes (baseado no BI)
- Para funcionários novos: criação de novos registros
- Para funcionários existentes: atualização dos dados

## Resultados da Importação

- **Funcionários importados com sucesso**: 76
- **Funcionários atualizados**: 1
- **Erros encontrados**: 0

## Benefícios Obtidos

1. **Economia de tempo**: Em vez de cadastrar manualmente 77 funcionários, o processo foi automatizado
2. **Redução de erros**: Minimização de erros de digitação através da importação direta
3. **Consistência dos dados**: Todos os funcionários foram cadastrados com o mesmo padrão
4. **Facilidade de manutenção**: O comando pode ser reutilizado para atualizações futuras

## Como Utilizar o Comando de Importação

### Para testar sem importar (dry run):
```bash
python manage.py import_funcionarios_excel "PLANILHAS funcionários-2025- IP.xlsx" --dry-run
```

### Para importar os dados:
```bash
python manage.py import_funcionarios_excel "PLANILHAS funcionários-2025- IP.xlsx"
```

## Considerações Técnicas

1. O comando utiliza o campo "N.º B.I" como identificador único para detectar funcionários existentes
2. Datas são convertidas do formato DD.MM.YYYY para o formato de data do Django
3. Valores categóricos (Género, Nível Académico, etc.) são convertidos para os valores esperados pelo sistema
4. Campos vazios são tratados adequadamente sem causar erros

## Próximos Passos

1. Verificar os dados importados através da interface administrativa do Django
2. Validar a integridade dos dados importados
3. Realizar testes de funcionalidades relacionadas aos funcionários
4. Documentar o processo para futuras importações