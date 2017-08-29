import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('alunos.ifpb.xls')

newData = df[df.columns[[3, 4, 6]]]

afastado = newData[newData.Situação == 'Afastado']
aguardandoColacao = newData[newData.Situação == 'Aguardando Colação de Grau']
aguardandoENADE = newData[newData.Situação == 'Aguardando ENADE']
cancelado = newData[newData.Situação == 'Cancelado']
cancelamentoCompulsorio = newData[newData.Situação == 'Cancelamento']
concludente = newData[newData.Situação == 'Concludente']
concluido = newData[newData.Situação == 'Concluído']
egresso = newData[newData.Situação == 'Egresso']
estagiarioConcludente = newData[newData.Situação == 'Estagiario (Concludente)']
evasao = newData[newData.Situação == 'Evasão']
falecido = newData[newData.Situação == 'Falecido']
formado = newData[newData.Situação == 'Formado']
intercambio = newData[newData.Situação == 'Intercâmbio']
matriculado = newData[newData.Situação == 'Matriculado']
trancado = newData[newData.Situação == 'Trancado']
trancadoVoluntariamente = newData[newData.Situação == 'Trancado Voluntariamente']
transferidoExterno = newData[newData.Situação == 'Transferido Externo']

situacao = pd.crosstab(index=newData["Situação"], columns="Quantidade")

porcentagem = situacao/situacao.sum()
print(porcentagem, "\n")

# print(porcentagem[porcentagem.columns[0]].ix[0])

# a = situacao.rownames
# print(a)

sizes = []
for indice in range(17):
    sizes.append(porcentagem[porcentagem.columns[0]].ix[indice])

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
explode = (0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.1, 0.5, 0.5, 0.5)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()