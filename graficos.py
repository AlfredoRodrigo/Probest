# ARQUIVO DE GRÁFICOS
# UTILIZADO COMO PACOTE PARA AS FUNÇÕES

import matplotlib.pyplot as plt
import numpy as np
import situacao as st
import labels as lb

# QUANTIDADE DE ALUNOS POR SITUAÇÃO E SUA PORCENTAGEM (COM E SEM MATRICULADOS)
situacaoComMatriculados = st.pd.crosstab(index=st.newData["Situação"], columns="Quantidade")
pctSituacaoComMatriculados = situacaoComMatriculados/situacaoComMatriculados.sum()
situacaoSemMatriculados = situacaoComMatriculados.drop("Matriculado")
pctSituacaoSemMatriculados = situacaoSemMatriculados/situacaoSemMatriculados.sum()

# curso = st.pd.crosstab(index=st.newData["Curso"], columns="Quantidade")
# periodo = st.pd.crosstab(index=st.newData["Ano/Periodo Letivo"], columns="Quantidade")

# MATRICULADOS POR CURSO E SUA PORCENTAGEM
matriculadosPorCurso = st.pd.crosstab(index=st.matriculado["Curso"], columns="Quantidade de matriculados")
pctMatriculadosPorCurso = matriculadosPorCurso/matriculadosPorCurso.sum()

# EVADIDOS POR CURSO E SUA PORCENTAGEM
evadidosPorCurso = st.pd.crosstab(index=st.evasao["Curso"], columns="Quantidade de evadidos")
pctEvadidosPorCurso = evadidosPorCurso/evadidosPorCurso.sum()


def qtd_situacao_com_matriculados():

    # GRÁFICO DE BARRAS COM A QUANTIDADE DE ALUNOS POR SITUAÇÃO (COM MATRICULADOS)

    x_axis = []
    for indice in range(17):
        x_axis.append(situacaoComMatriculados[situacaoComMatriculados.columns[0]].ix[indice])

    fig, ax = plt.subplots()

    y_pos = np.arange(len(lb.APSCM))

    ax.barh(y_pos, x_axis, align='center', color='green', ecolor='black')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(lb.APSCM)
    ax.invert_yaxis()
    ax.set_xlabel('Quantidade')
    ax.set_title('Alunos por situação')

    plt.grid()
    plt.tight_layout()
    plt.show()


def pct_situacao_com_matriculados():

    # GRÁFICO DE PIZZA COM A PORCENTAGEM DE ALUNOS POR SITUAÇÃO (COM MATRICULADOS)

    sizes = []
    for indice in range(17):
        sizes.append(pctSituacaoComMatriculados[pctSituacaoComMatriculados.columns[0]].ix[indice])

    fig1, ax1 = plt.subplots()
    explode = (1.3, 1.2, 1.1, 1, .9, .8, .7, .8, .5, .4, .3, .4, .5, .1, .2, .3, .4)
    ax1.pie(sizes, labels=lb.APSCM, autopct='%1.2f%%', shadow=False, startangle=90, explode=explode)
    ax1.axis('equal')
    ax1.set_title('Porcentagem de alunos por situação')

    plt.tight_layout()
    plt.show()


def qtd_situacao_sem_matriculados():

    # GRÁFICO DE BARRAS COM A QUANTIDADE DE ALUNOS POR SITUAÇÃO (SEM MATRICULADOS)

    x_axis = []
    for indice in range(16):
        x_axis.append(situacaoSemMatriculados[situacaoSemMatriculados.columns[0]].ix[indice])

    fig, ax = plt.subplots()

    y_pos = np.arange(len(lb.APSSM))

    ax.barh(y_pos, x_axis, align='center', color='green', ecolor='black')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(lb.APSSM)
    ax.invert_yaxis()
    ax.set_xlabel('Quantidade')
    ax.set_title('Alunos por situação (sem matriculados)')

    plt.grid()
    plt.tight_layout()
    plt.show()


def pct_situacao_sem_matriculados():

    # GRÁFICO DE PIZZA COM A PORCENTAGEM DE ALUNOS POR SITUAÇÃO (SEM MATRICULADOS)

    sizes = []
    for indice in range(16):
        sizes.append(pctSituacaoSemMatriculados[pctSituacaoSemMatriculados.columns[0]].ix[indice])

    fig1, ax1 = plt.subplots()
    explode = (.5, .4, .3, 0, .3, .1, 0, .1, .3, 0, .05, .1, .15, .2, .25, .3)
    ax1.pie(sizes, labels=lb.APSSM, autopct='%1.2f%%', shadow=False, startangle=90, explode=explode)
    ax1.axis('equal')
    ax1.set_title('Porcentagem de alunos por situação (sem matriculados)')

    plt.tight_layout()
    plt.show()


def qtd_matriculados_por_curso():

    # GRÁFICO DE BARRAS COM A QUANTIDADE DE MATRICULADOS POR CURSO

    x_axis = []
    for indice in range(19):
        x_axis.append(matriculadosPorCurso[matriculadosPorCurso.columns[0]].ix[indice])

    fig, ax = plt.subplots()

    y_pos = np.arange(len(lb.MPC))

    ax.barh(y_pos, x_axis, align='center', color='green', ecolor='black')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(lb.MPC)
    ax.invert_yaxis()
    ax.set_xlabel('Quantidade')
    ax.set_title('Alunos matriculados por curso')

    plt.grid()
    plt.tight_layout()
    plt.show()


def pct_matriculados_por_curso():

    # GRÁFICO DE PIZZA COM A PORCENTAGEM DE MATRICULADOS POR CURSO

    sizes = []
    for indice in range(19):
        sizes.append(pctMatriculadosPorCurso[pctMatriculadosPorCurso.columns[0]].ix[indice])

    fig1, ax1 = plt.subplots()
    explode = (0, 0, 0, 0, .1, .2, 0, 0, 0, 0, 0, 0, 0, .1, .2, .3, .4, .5, .6)
    ax1.pie(sizes, labels=lb.MPC, autopct='%1.1f%%', shadow=False, startangle=90, explode=explode)
    ax1.axis('equal')
    ax1.set_title('Porcentagem de alunos matriculados por curso')

    plt.tight_layout()
    plt.show()


def quantidade_evadidos_por_curso():

    # GRÁFICO DE BARRAS COM A QUANTIDADE DE EVADIDOS POR CURSO

    x_axis = []
    for indice in range(12):
        x_axis.append(evadidosPorCurso[evadidosPorCurso.columns[0]].ix[indice])

    fig, ax = plt.subplots()

    y_pos = np.arange(len(lb.EPC))

    ax.barh(y_pos, x_axis, align='center', color='green', ecolor='black')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(lb.EPC)
    ax.invert_yaxis()
    ax.set_xlabel('Quantidade')
    ax.set_title('Alunos evadidos por curso')

    plt.grid()
    plt.tight_layout()
    plt.show()


def porcentagem_evadidos_por_curso():

    # GRÁFICO DE PIZZA COM A PORCENTAGEM DE EVADIDOS POR CURSO

    sizes = []
    for indice in range(12):
        sizes.append(pctEvadidosPorCurso[pctEvadidosPorCurso.columns[0]].ix[indice])

    fig1, ax1 = plt.subplots()
    explode = (0, 0, 0, 0, 0, 0, 0, .1, 0, 0, 0, .1)
    ax1.pie(sizes, labels=lb.EPC, autopct='%1.1f%%', shadow=False, startangle=90, explode=explode)
    ax1.axis('equal')
    ax1.set_title('Porcentagem de alunos evadidos por curso')

    plt.tight_layout()
    plt.show()
