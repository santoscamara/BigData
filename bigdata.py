import pandas as pd
import numpy as np


df = pd.read_excel("Planilha final 4.xlsx")
df['Data'] = pd.to_datetime(df['Data'], errors='coerce')


faturamento_por_ano = df['Valor_Venda'].groupby(df['Data'].dt.year).sum().reset_index()
faturamento_por_ano.columns = ['Ano', 'Total_Vendas']
faturamento = df['Valor_Venda'].sum()

lucro_por_ano = df['Valor_Lucro'].groupby(df['Data'].dt.year).sum().reset_index()
lucro_por_ano.columns = ['Ano', 'Lucro por Ano']
lucro = df['Valor_Lucro'].sum()

qtd_vendas_por_ano = df['Quantidade'].groupby(df['Data'].dt.year).sum().reset_index()
qtd_vendas = df['Quantidade'].sum()

v = df.groupby(df['Data'].dt.year)['Vendedor'].value_counts()



meta_faturamento = faturamento_por_ano['Total_Vendas'] + (faturamento_por_ano['Total_Vendas'] * 0.3)

print(v)











