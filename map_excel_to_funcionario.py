import pandas as pd
from django.utils import timezone
from datetime import datetime

# Read the Excel file with the correct header row
df = pd.read_excel('PLANILHAS funcionários-2025- IP.xlsx', header=8)

# Rename columns to match the actual headers
df.columns = [
    'N/O', 'Nome completo', 'N.º Agente', 'Categoria', 'N.º B.I', 'Data de Nascimento', 
    'Género', 'Nível Académico', 'Curso de Formação', 'Ano de conclusão da formação actual', 
    'Tempo de serviço na Função Pública', 'Tempo de serviço no Ensino Superior', 
    'Ano de Ingresso na categoria Actual', 'Função/Cargo', 'DEI a que pertence', 
    'Regime de Trabalho', 'Endereço Electrónico', 'Telefone'
]

# Display the first few rows to verify
print("Columns in the Excel file:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())

# Check how many rows have data
print(f"\nTotal rows: {len(df)}")
print(f"Rows with employee names: {df['Nome completo'].notna().sum()}")

# Let's see what data we can map to the Funcionario model
print("\nSample employee data:")
for i in range(min(5, len(df))):
    if pd.notna(df.iloc[i]['Nome completo']):
        print(f"\nEmployee {i}:")
        row = df.iloc[i]
        for col in df.columns:
            if pd.notna(row[col]):
                print(f"  {col}: {row[col]}")

# Mapping to Funcionario model fields
print("\n\nMapping to Funcionario model:")
print("Excel Column -> Funcionario Field")
print("=================================")
mapping = {
    'Nome completo': 'nome',
    'N.º B.I': 'bi',
    'Data de Nascimento': 'data_nascimento',
    'Género': 'genero',
    'Nível Académico': 'grau_academico',
    'Curso de Formação': 'curso_formacao',
    'Ano de conclusão da formação actual': 'ano_conclusao_formacao',
    'Tempo de serviço na Função Pública': 'tempo_servico_fp',
    'Tempo de serviço no Ensino Superior': 'tempo_servico_es',
    'Ano de Ingresso na categoria Actual': 'ano_ingresso_categoria',
    'Função/Cargo': 'cargo',
    'DEI a que pertence': 'departamento',
    'Regime de Trabalho': 'regime_trabalho',
    'Endereço Electrónico': 'email_institucional',
    'Telefone': 'contacto_principal',
    'N.º Agente': 'numero_agente'
}

for excel_col, funcionario_field in mapping.items():
    print(f"{excel_col} -> {funcionario_field}")