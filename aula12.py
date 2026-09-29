import pandas as pd #importar pandas com apelido pd

#criar um dicionario (os dados)
dicionario = {"nome":["joão", "maria", "pedro"],"idade":[12,10,11],"nota":[7.0, 5.6, 9.0]}


#importar o dicionario (dados) para uma dataframe
df = pd.DataFrame(dicionario)

#mostrar o dataframe no terminal
print(df)

#Visualização de dados

#visualizar as 3 primeiras linhas do dataframe:
print(df.head(3)) 
df_tres_primeiras_linhas = df.head(3)
print(df_tres_primeiras_linhas)

#visualizar as 3 ultimas linhas do dataframe:

print(df.tail(3)) 
df_tres_primeiras_linhas = df.tail(3)
print(df_tres_primeiras_linhas)

#FILTRAGEM DE DADOS:

print(df[df["nota"] >= 7])

df_alunos_nota_maior_7 = df[df["nota"] >= 7]

print(df_alunos_nota_maior_7)

print(df[df["idade"] < 10])

df_alunos_idade_menor_10 = df[df["idade"] < 10]

print(df_alunos_idade_menor_10)

