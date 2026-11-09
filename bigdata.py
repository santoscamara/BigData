import pandas as pd
import numpy as np

df = pd.read_excel("Planilha final.xlsx")

df['Data'] = pd.to_datetime(df['Data'], errors='coerce')
df['Ano'] = df['Data'].dt.year
df['Data'] = df['Data'].dt.strftime("%d/%m/%Y")

# Tratamento das colunas de texto para uniformização (Tudo maiúsculo e sem espaços em branco).
for col in ['Produto', 'Material', 'Pureza', 'Categoria', 'Forma_de_Pagamento']:
    df[col] = df[col].astype(str).str.strip().str.upper()


df['Valor_Bruto'] = df['Quantidade'] * df['Valor_Unitario']
df['Valor_Lucro'] = df['Valor_Bruto'] * df['Percentual_Lucro']
df['Valor_Venda'] = df['Valor_Bruto'] + df['Valor_Lucro']

#Aplicação da taxa de 5% nas vendas onde a forma de pagamento é cartão. 
df['Taxa_Cartao'] = np.where(df['Forma_de_Pagamento'].str.contains('CARTA|CARTÃ'), 0.05, 0.00)

# Calcula o valor que efetivamente entra no caixa e o lucro real do negócio
df['Valor_Venda_Liquido'] = df['Valor_Venda'] * (1 - df['Taxa_Cartao'])
df['Lucro_Liquido_Real'] = df['Valor_Venda_Liquido'] - df['Valor_Bruto']

# Tratamento das colunas de valores para apresentar apenas duas casas decimais.
colunas_valores = ['Valor_Bruto', 'Valor_Lucro', 'Valor_Venda', 'Valor_Venda_Liquido', 'Lucro_Liquido_Real']
df[colunas_valores] = df[colunas_valores].round(2)


# Agrupa tanto a venda bruta quanto a líquida simulada por Ano
faturamento_por_ano = df.groupby('Ano')[['Valor_Venda', 'Valor_Venda_Liquido']].sum().reset_index()
faturamento_por_ano.columns = ['Ano', 'Total_Vendas', 'Total_Vendas_Liquido']

meta_faturamento = faturamento_por_ano.copy()
meta_faturamento['Vendas_Ano_Anterior'] = meta_faturamento['Total_Vendas'].shift(1)
meta_faturamento['Meta_Ano'] = meta_faturamento['Vendas_Ano_Anterior'] * 1.30

# Compara o atingimento da meta usando o valor bruto (ilusão) vs o valor líquido (realidade)
meta_faturamento['Porcentagem_Bruta'] = round((meta_faturamento['Total_Vendas'] / meta_faturamento['Meta_Ano']) * 100, 2)
meta_faturamento['Porcentagem_Liquida'] = round((meta_faturamento['Total_Vendas_Liquido'] / meta_faturamento['Meta_Ano']) * 100, 2)


df = df.drop(columns=['Taxa_Cartao', 'Valor_Total', 'Valor_UnitarioXQtd'], errors='ignore')
df = pd.merge(df, meta_faturamento[['Ano', 'Meta_Ano', 'Porcentagem_Bruta', 'Porcentagem_Liquida']], on='Ano', how='left')

# ORGANIZAÇÃO E EXPORTAÇÃO FINAL
nova_ordem = [
    'Produto', 'Material', 'Pureza', 'Categoria', 'Data', 'Forma_de_Pagamento', 
    'Vendedor', 'Valor_Unitario', 'Quantidade', 'Valor_Bruto', 'Percentual_Lucro', 
    'Valor_Lucro', 'Valor_Venda', 'Valor_Venda_Liquido', 'Lucro_Liquido_Real', 
    'Meta_Ano', 'Porcentagem_Bruta', 'Porcentagem_Liquida', 'Link'
]
df = df[nova_ordem]

# Elimina a coluna temporária usada apenas para o cálculo
df = df.drop(columns=['Taxa_Cartao', 'Valor_Total', 'Valor_UnitarioXQtd'], errors='ignore')
#Exportação dos dados tratados para uma nova planilha
df.to_excel("Projeto_Big_Data.xlsx", index=False)


#Tratamento dos dados para simulação do Split Payment em 2027. 
df_projecao = pd.read_excel('Projeto_Big_Data.xlsx')
df_projecao['Data'] = pd.to_datetime(df_projecao['Data'], dayfirst=True)
df_projecao['Mes'] = df_projecao['Data'].dt.to_period('M').dt.to_timestamp()

receita = df_projecao.groupby('Mes')['Valor_Venda'].sum()
lucro = df_projecao.groupby('Mes')['Lucro_Liquido_Real'].sum()

corte = pd.Timestamp('2026-08-31')
ref = df_projecao[(df_projecao['Data'] >= '2025-01-01') & (df_projecao['Data'] <= corte)]
margem = ref['Lucro_Liquido_Real'].sum() / ref['Valor_Venda'].sum()

ano26 = df[(df_projecao['Data'] >= '2026-01-01') & (df_projecao['Data'] <= corte)]['Valor_Venda'].sum()
ano25 = df[(df_projecao['Data'] >= '2025-01-01') & (df_projecao['Data'] <= '2025-08-31')]['Valor_Venda'].sum()
cresc_2026 = ano26 / ano25 - 1
cresc_2027 = 0.05
aliquota = 0.28

linhas = []
valores = {}
for m in pd.date_range('2025-01-01', '2027-12-01', freq='MS'):
    if m <= corte:
        tipo = 'Realizado'
        r = receita.get(m, 0)
        l = lucro.get(m, 0)
    else:
        tipo = 'Projetado'
        g = cresc_2026 if m.year == 2026 else cresc_2027
        r = valores[m - pd.DateOffset(years=1)] * (1 + g)
        l = r * margem
    valores[m] = r
    a = aliquota if m >= pd.Timestamp('2027-01-01') else 0
    imposto = r * a
    linhas.append([m, tipo, round(r, 2), a, round(imposto, 2), round(l, 2), round(l - imposto, 2)])

proj = pd.DataFrame(linhas, columns=['Mês', 'Tipo', 'Receita bruta', 'Alíquota',
                                     'Imposto split payment', 'Lucro antes do imposto',
                                     'Lucro após imposto'])


proj.to_excel('Projecao.xlsx', sheet_name='Projeção', index=False)

