
#crie o dataframe a parti do dicionario e faça os seguintes filtros:
#funcionarios com salario maior que 3000.00
#funcioanarios com cargo de vendedor

import pandas as pd 

dicionario = {"nome":["genonimo", "marta", "patrick", "tiberios", "janaina", "mercedes"],
            "cargo":["gerente", "gerente","vendedor", "secretario","vendedora","vendedor"],
            "salario": [9600.56, 9600.56, 2600.90, 4500.45, 2600.90, 2600.90]}
df = pd.DataFrame (dicionario)

print (df[df["salario"] >= 3000])
print (df[df["cargo"] == "vendedor"])