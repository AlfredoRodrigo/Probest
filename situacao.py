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