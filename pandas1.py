#crie um dataframe que tera 3 colunas e 3 linhas: nome, cargo, salario

import pandas as pd 

dicionario = {"nome":["joão", "maria", "pedro"],"cargo":["eletricista", "advogado", "programador"],"salario":[ 3.500, 5.000, 6.000]}

df = pd.DataFrame(dicionario)

print(df)


