import matplotlib.pyplot as plt
from situacao import *

df = pd.read_excel('alunos.ifpb.xls')

situacao = pd.crosstab(index=newData["Situação"], columns="Quantidade")
curso = pd.crosstab(index=newData["Curso"], columns="Quantidade")
periodo = pd.crosstab(index=newData["Ano/Periodo Letivo"], columns="Quantidade")

evadidosPorCurso = pd.crosstab(index=evasao["Curso"], columns="Quantidade")

print(evadidosPorCurso)

porcentagem = evadidosPorCurso/evadidosPorCurso.sum()
print(porcentagem, "\n")

sizes = []
for indice in range(12):
    sizes.append(porcentagem[porcentagem.columns[0]].ix[indice])

labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal')

plt.show()