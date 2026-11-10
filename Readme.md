<h1 align="center">
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="Python Logo" width="50">
  <br>
  BIG DATA — Análise de Vendas de Joalheria
</h1>

<p align="center">
  <strong>Tratamento, análise e projeção de vendas com Python, Excel e Power BI.</strong>
</p>

<hr>

## 🚀 Sobre o Projeto

O projeto **Big Data** analisa uma base de **571 vendas de joalheria** (2015 a 2026), aplicando tratamento de dados com **Python (pandas e numpy)** e visualização no **Power BI**.

O script padroniza os dados, calcula lucro bruto e líquido (considerando a taxa de 5% nas vendas no cartão), compara o faturamento anual com a meta de crescimento de 30% e simula o impacto do **Split Payment (alíquota de 28%)** sobre o lucro de 2027.

---

## 🛠️ Tech Stack

<p align="left">
  <img src="https://skillicons.dev/icons?i=py,pandas,numpy,powerbi,git" height="45" alt="Tech Stack" />
</p>

---

## 📂 Estrutura do Projeto

| Arquivo | Tipo | Responsabilidade |
|:--------|:-----|:-----------------|
| `bigdata.py` | Script Python | Tratamento dos dados, cálculo de metas e projeção do Split Payment |
| `Planilha final.xlsx` | Dados brutos | Base original de vendas (`TabelaVendas`) |
| `Projeto_Big_Data.xlsx` | Dados tratados | Base final com valores líquidos, meta anual e percentuais de atingimento |
| `Projecao.xlsx` | Projeção | Receita e lucro mensais (realizado e projetado) de 2025 a 2027 |
| `Projeto_Big_Data.pbix` | Dashboard | Painel no Power BI com os gráficos de análise e previsão |

---

## 🧩 Etapas do Tratamento

- **Padronização** — colunas de texto em maiúsculas e sem espaços extras
- **Cálculo de valores** — `Valor_Bruto`, `Valor_Lucro` e `Valor_Venda`
- **Taxa de cartão** — desconto de 5% para gerar `Valor_Venda_Liquido` e `Lucro_Liquido_Real`
- **Meta anual** — faturamento do ano anterior + 30%, com atingimento bruto vs. líquido
- **Projeção** — realizado até 31/08/2026 e projetado até 12/2027, com crescimento 2027 de 5%

---

## 📊 Projeção do Split Payment

A partir de **01/01/2027**, a alíquota de **28%** é aplicada sobre a receita bruta mensal. O arquivo `Projecao.xlsx` apresenta, para cada mês:

- Receita bruta
- Imposto do Split Payment
- Lucro antes do imposto
- Lucro após o imposto

---

## ▶️ Como Executar

```bash
pip install pandas numpy openpyxl
python bigdata.py
```

O script lê `Planilha final.xlsx` e gera `Projeto_Big_Data.xlsx` e `Projecao.xlsx`. O arquivo `.pbix` deve ser aberto no Power BI Desktop.

---

## 👨‍💻 Autores

<table align="center">
  <tr>
    <td align="center">
      <img src="https://github.com/iggorhenri-tech.png" width="100px;" alt="Igor H." style="border-radius: 50%; border: 2px solid #5d2f8e;"/>
      <br />
      <sub><b>Igor H.</b></sub>
      <br /><br />
      <a href="https://www.linkedin.com/in/igor-henrique-26b149218/" target="_blank">
        <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white">
      </a>
      <br />
      <a href="mailto:iggorhenri@gmail.com">
        <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white">
      </a>
    </td>
    <td align="center">
      <img src="https://github.com/santoscamara.png" width="100px;" alt="santoscamara" style="border-radius: 50%; border: 2px solid #5d2f8e;"/>
      <br />
      <sub><b>santoscamara</b></sub>
      <br /><br />
      <a href="https://github.com/santoscamara" target="_blank">
        <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white">
      </a>
    </td>
  </tr>
</table>