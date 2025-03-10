# pip install mlxtend

from mlxtend.frequent_patterns import apriori, association_rules
import pandas as pd

# Carregar e organizar os dados
dados = pd.read_excel('TEF Sells prediction/day_snacks.xlsx')
print(dados)

# Criar uma matriz de transações por máquina e produto
transacoes = dados.groupby(['Matricula', 'Produto'])['R$ Total do Item'].count().unstack().fillna(0)
transacoes = transacoes.map(lambda x: 1 if x > 0 else 0)

# Aplicar o algoritmo Apriori
frequent_itemsets = apriori(transacoes, min_support=0.05, use_colnames=True)

# Verificar conjuntos frequentes
print(frequent_itemsets.head())

# Gerar regras de associação
regras = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

# Verificar colunas disponíveis
print("Colunas disponíveis no DataFrame de regras:", regras.columns)

# Garantir que há regras antes de tentar acessá-las
if not regras.empty:
    print(regras[['antecedants', 'consequents', 'support', 'confidence', 'lift']].head())
else:
    print("Nenhuma regra foi gerada.")

