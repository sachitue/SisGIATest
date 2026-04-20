#!/usr/bin/env python
import os
import sys
import django
import pandas as pd

# Configuração do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'college_management_system.settings')
django.setup()

from RH.models import Funcionario, CategoriaFuncionario

def verificar_estado_categorias():
    """Verifica o estado atual das categorias."""
    print("🔍 VERIFICANDO ESTADO ATUAL DAS CATEGORIAS")
    print("="*70)
    
    # Verificar categorias existentes
    categorias = CategoriaFuncionario.objects.all()
    print(f"📊 Categorias cadastradas: {categorias.count()}")
    
    for cat in categorias:
        funcionarios_count = Funcionario.objects.filter(categoria=cat).count()
        print(f"   • {cat.codigo} - {cat.descricao}: {funcionarios_count} funcionários")
    
    # Verificar funcionários sem categoria
    sem_categoria = Funcionario.objects.filter(categoria__isnull=True).count()
    com_categoria = Funcionario.objects.exclude(categoria__isnull=True).count()
    total = Funcionario.objects.count()
    
    print(f"\n📋 ESTADO DOS FUNCIONÁRIOS:")
    print(f"   • Total de funcionários: {total}")
    print(f"   • Com categoria: {com_categoria}")
    print(f"   • Sem categoria: {sem_categoria}")
    print(f"   • Percentual preenchido: {(com_categoria/total)*100:.1f}%")
    
    return sem_categoria, total

def criar_categorias_padrao():
    """Cria as categorias padrão baseadas no Excel."""
    print("\n🔧 CRIANDO CATEGORIAS PADRÃO")
    print("="*70)
    
    categorias_padrao = [
        ("ASSISTENTE", "Assistente"),
        ("ASSISTENTE_ESTAGIARIO", "Assistente Estagiário"),
        ("PROFESSOR_AUXILIAR", "Professor Auxiliar"),
        ("ASSISTENTE_INVESTIGACAO", "Assistente de Investigação"),
        ("AUXILIAR_INVESTIGACAO", "Auxiliar de Investigação"),
        ("ASSISTENTE_PRINCIPAL", "Assistente Principal"),
        ("PROFESSOR_ASSOCIADO", "Professor Associado"),
        ("PROFESSOR_CATEDRATICO", "Professor Catedrático"),
        ("TECNICO_SUPERIOR", "Técnico Superior"),
        ("TECNICO_MEDIO", "Técnico Médio"),
        ("ASSISTENTE_TECNICO", "Assistente Técnico"),
        ("AUXILIAR_SERVICOS", "Auxiliar de Serviços"),
        ("COORDENADOR", "Coordenador"),
        ("CHEFE_DEI", "Chefe de DEI"),
        ("DIRETOR", "Diretor"),
        ("SUBDIRETOR", "Subdiretor"),
        ("SECRETARIO", "Secretário"),
        ("MOTORISTA", "Motorista"),
        ("VIGILANTE", "Vigilante"),
        ("LIMPEZA", "Pessoal de Limpeza"),
    ]
    
    criadas = 0
    existentes = 0
    
    for codigo, descricao in categorias_padrao:
        categoria, created = CategoriaFuncionario.objects.get_or_create(
            codigo=codigo,
            defaults={'descricao': descricao}
        )
        
        if created:
            print(f"   ✅ Criada: {codigo} - {descricao}")
            criadas += 1
        else:
            print(f"   📋 Existe: {codigo} - {descricao}")
            existentes += 1
    
    print(f"\n📊 Resultado: {criadas} criadas, {existentes} já existentes")
    return criadas

def mapear_categoria_do_excel():
    """Mapeia categorias do Excel para os funcionários."""
    print("\n🔄 MAPEANDO CATEGORIAS DO EXCEL")
    print("="*70)
    
    # Ler dados do Excel para obter as categorias originais
    arquivo_excel = 'PLANILHAS funcionários-2025- IP.xlsx'
    
    if not os.path.exists(arquivo_excel):
        print(f"❌ Arquivo Excel não encontrado: {arquivo_excel}")
        return 0
    
    # Mapeamento de categorias do Excel para códigos do sistema
    mapeamento_categorias = {
        'assistente': 'ASSISTENTE',
        'assistente estagiário': 'ASSISTENTE_ESTAGIARIO',
        'assistente estagiario': 'ASSISTENTE_ESTAGIARIO',
        'professor auxiliar': 'PROFESSOR_AUXILIAR',
        'assistente de investigação': 'ASSISTENTE_INVESTIGACAO',
        'assistente de investigacao': 'ASSISTENTE_INVESTIGACAO',
        'auxiliar de investigação': 'AUXILIAR_INVESTIGACAO',
        'auxiliar de investigacao': 'AUXILIAR_INVESTIGACAO',
        'assistente principal': 'ASSISTENTE_PRINCIPAL',
        'professor associado': 'PROFESSOR_ASSOCIADO',
        'professor catedrático': 'PROFESSOR_CATEDRATICO',
        'professor catedratico': 'PROFESSOR_CATEDRATICO',
        'técnico superior': 'TECNICO_SUPERIOR',
        'tecnico superior': 'TECNICO_SUPERIOR',
        'técnico médio': 'TECNICO_MEDIO',
        'tecnico medio': 'TECNICO_MEDIO',
        'assistente técnico': 'ASSISTENTE_TECNICO',
        'assistente tecnico': 'ASSISTENTE_TECNICO',
        'auxiliar de serviços': 'AUXILIAR_SERVICOS',
        'auxiliar de servicos': 'AUXILIAR_SERVICOS',
        'coordenador': 'COORDENADOR',
        'chefe': 'CHEFE_DEI',
        'diretor': 'DIRETOR',
        'subdiretor': 'SUBDIRETOR',
        'secretário': 'SECRETARIO',
        'secretario': 'SECRETARIO',
        'motorista': 'MOTORISTA',
        'vigilante': 'VIGILANTE',
        'limpeza': 'LIMPEZA',
    }
    
    funcionarios_atualizados = 0
    erros = []
    
    try:
        # Processar cada aba do Excel
        abas = ['Docentes', 'Administrativo', 'Docentes e Adm Contratados', 
                'Aposentados', 'Docen Expatriados', 'DocentesFormação']
        
        for aba in abas:
            try:
                print(f"\n📋 Processando aba: {aba}")
                df = pd.read_excel(arquivo_excel, sheet_name=aba, header=9)
                df = df.dropna(subset=['Nome completo'])
                
                for _, row in df.iterrows():
                    nome_completo = str(row['Nome completo']).strip()
                    if not nome_completo or nome_completo == 'nan':
                        continue
                    
                    # Separar nome e apelido
                    partes = nome_completo.split()
                    if len(partes) >= 2:
                        nome = " ".join(partes[:-1])
                        apelido = partes[-1]
                    else:
                        nome = partes[0]
                        apelido = ""
                    
                    # Procurar funcionário no banco
                    funcionario = Funcionario.objects.filter(
                        nome=nome, 
                        apelido=apelido
                    ).first()
                    
                    if funcionario and not funcionario.categoria:
                        # Extrair categoria do Excel
                        categoria_excel = None
                        for col in df.columns:
                            if 'categoria' in str(col).lower():
                                categoria_excel = row.get(col)
                                break
                        
                        if pd.notna(categoria_excel):
                            categoria_str = str(categoria_excel).strip().lower()
                            
                            # Buscar código da categoria
                            codigo_categoria = mapeamento_categorias.get(categoria_str)
                            
                            if codigo_categoria:
                                try:
                                    categoria_obj = CategoriaFuncionario.objects.get(codigo=codigo_categoria)
                                    funcionario.categoria = categoria_obj
                                    funcionario.save()
                                    funcionarios_atualizados += 1
                                    print(f"   ✅ {nome} {apelido} → {categoria_obj.descricao}")
                                except CategoriaFuncionario.DoesNotExist:
                                    print(f"   ⚠️ Categoria não encontrada: {codigo_categoria}")
                            else:
                                # Categoria não mapeada, criar uma genérica
                                categoria_generica, created = CategoriaFuncionario.objects.get_or_create(
                                    codigo=categoria_str.upper().replace(' ', '_'),
                                    defaults={'descricao': categoria_excel}
                                )
                                funcionario.categoria = categoria_generica
                                funcionario.save()
                                funcionarios_atualizados += 1
                                print(f"   🆕 {nome} {apelido} → {categoria_generica.descricao} (nova)")
            
            except Exception as e:
                erro = f"Erro na aba {aba}: {str(e)}"
                erros.append(erro)
                print(f"   ❌ {erro}")
    
    except Exception as e:
        print(f"❌ Erro geral: {e}")
    
    if erros:
        print(f"\n⚠️ Erros encontrados:")
        for erro in erros[:5]:
            print(f"   - {erro}")
    
    print(f"\n📊 Funcionários atualizados com categoria: {funcionarios_atualizados}")
    return funcionarios_atualizados

def atribuir_categorias_por_cargo():
    """Atribui categorias baseadas no campo cargo para funcionários sem categoria."""
    print("\n🎯 ATRIBUINDO CATEGORIAS POR CARGO")
    print("="*70)
    
    # Mapeamento de cargos para categorias
    mapeamento_cargo_categoria = {
        'coordenador': 'COORDENADOR',
        'chefe': 'CHEFE_DEI',
        'diretor': 'DIRETOR',
        'subdiretor': 'SUBDIRETOR',
        'secretário': 'SECRETARIO',
        'secretario': 'SECRETARIO',
        'professor': 'PROFESSOR_AUXILIAR',
        'docente': 'ASSISTENTE',
        'técnico': 'TECNICO_SUPERIOR',
        'tecnico': 'TECNICO_SUPERIOR',
        'assistente': 'ASSISTENTE',
        'auxiliar': 'AUXILIAR_SERVICOS',
        'motorista': 'MOTORISTA',
        'vigilante': 'VIGILANTE',
        'limpeza': 'LIMPEZA',
    }
    
    funcionarios_sem_categoria = Funcionario.objects.filter(categoria__isnull=True)
    atualizados_por_cargo = 0
    
    for funcionario in funcionarios_sem_categoria:
        if funcionario.cargo:
            cargo_lower = funcionario.cargo.lower()
            
            for palavra_chave, codigo_categoria in mapeamento_cargo_categoria.items():
                if palavra_chave in cargo_lower:
                    try:
                        categoria = CategoriaFuncionario.objects.get(codigo=codigo_categoria)
                        funcionario.categoria = categoria
                        funcionario.save()
                        atualizados_por_cargo += 1
                        print(f"   ✅ {funcionario.nome} {funcionario.apelido} → {categoria.descricao} (por cargo: {funcionario.cargo})")
                        break
                    except CategoriaFuncionario.DoesNotExist:
                        continue
    
    print(f"\n📊 Funcionários atualizados por cargo: {atualizados_por_cargo}")
    return atualizados_por_cargo

def atribuir_categoria_padrao():
    """Atribui categoria padrão para funcionários ainda sem categoria."""
    print("\n📋 ATRIBUINDO CATEGORIA PADRÃO")
    print("="*70)
    
    funcionarios_sem_categoria = Funcionario.objects.filter(categoria__isnull=True)
    
    if funcionarios_sem_categoria.count() == 0:
        print("   ✅ Todos os funcionários já possuem categoria!")
        return 0
    
    # Usar categoria padrão "ASSISTENTE" para funcionários sem categoria
    try:
        categoria_padrao = CategoriaFuncionario.objects.get(codigo='ASSISTENTE')
    except CategoriaFuncionario.DoesNotExist:
        categoria_padrao = CategoriaFuncionario.objects.create(
            codigo='ASSISTENTE',
            descricao='Assistente'
        )
    
    atualizados = 0
    for funcionario in funcionarios_sem_categoria:
        funcionario.categoria = categoria_padrao
        funcionario.save()
        atualizados += 1
        print(f"   📋 {funcionario.nome} {funcionario.apelido} → {categoria_padrao.descricao} (padrão)")
    
    print(f"\n📊 Funcionários com categoria padrão: {atualizados}")
    return atualizados

def verificacao_final_categorias():
    """Verificação final das categorias preenchidas."""
    print("\n✅ VERIFICAÇÃO FINAL DAS CATEGORIAS")
    print("="*70)
    
    total = Funcionario.objects.count()
    com_categoria = Funcionario.objects.exclude(categoria__isnull=True).count()
    sem_categoria = total - com_categoria
    
    print(f"📊 RESULTADOS FINAIS:")
    print(f"   • Total de funcionários: {total}")
    print(f"   • Com categoria: {com_categoria}")
    print(f"   • Sem categoria: {sem_categoria}")
    print(f"   • Percentual preenchido: {(com_categoria/total)*100:.1f}%")
    
    # Estatísticas por categoria
    print(f"\n📋 DISTRIBUIÇÃO POR CATEGORIA:")
    categorias_usadas = CategoriaFuncionario.objects.filter(funcionarios__isnull=False).distinct()
    
    for categoria in categorias_usadas:
        count = Funcionario.objects.filter(categoria=categoria).count()
        print(f"   • {categoria.descricao}: {count} funcionários")
    
    if sem_categoria == 0:
        print(f"\n🎉 SUCESSO! Todos os funcionários possuem categoria!")
        return True
    else:
        print(f"\n⚠️ Ainda restam {sem_categoria} funcionários sem categoria")
        return False

def executar_preenchimento_categorias():
    """Executa todo o processo de preenchimento de categorias."""
    print("🚀 INICIANDO PREENCHIMENTO DE CATEGORIAS")
    print("="*70)
    
    # 1. Verificar estado atual
    sem_categoria_inicial, total = verificar_estado_categorias()
    
    if sem_categoria_inicial == 0:
        print("\n🎉 Todos os funcionários já possuem categoria!")
        return True
    
    # 2. Criar categorias padrão
    categorias_criadas = criar_categorias_padrao()
    
    # 3. Mapear categorias do Excel
    mapeados_excel = mapear_categoria_do_excel()
    
    # 4. Atribuir por cargo
    mapeados_cargo = atribuir_categorias_por_cargo()
    
    # 5. Atribuir categoria padrão para restantes
    padrao_atribuidos = atribuir_categoria_padrao()
    
    # 6. Verificação final
    sucesso = verificacao_final_categorias()
    
    # 7. Relatório final
    print(f"\n" + "="*70)
    print(f"📋 RELATÓRIO FINAL DO PREENCHIMENTO")
    print("="*70)
    print(f"   • Categorias criadas: {categorias_criadas}")
    print(f"   • Mapeados do Excel: {mapeados_excel}")
    print(f"   • Mapeados por cargo: {mapeados_cargo}")
    print(f"   • Categoria padrão: {padrao_atribuidos}")
    print(f"   • Total processado: {mapeados_excel + mapeados_cargo + padrao_atribuidos}")
    
    if sucesso:
        print(f"   • Status: ✅ SUCESSO TOTAL!")
    else:
        print(f"   • Status: ⚠️ PARCIALMENTE CONCLUÍDO")
    
    print("="*70)
    return sucesso

if __name__ == "__main__":
    executar_preenchimento_categorias()