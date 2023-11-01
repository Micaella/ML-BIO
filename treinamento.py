import pandas as pd
import numpy as np
import pickle
import os
from sklearn.ensemble import ExtraTreesRegressor

def tratar_dados(resultados_, entradas_, threads_, bootstrap_):
    resultados_.columns = resultados_.columns.str.strip() #tira os espaços no incio de final de cada nome de coluna
    for i in ['AveCPU', 'CPUTime', 'Elapsed']: #alterando para segundos (float)
        resultados_[i] = (pd.to_timedelta(resultados_[i].astype(str)).dt.total_seconds())
    dados_ = resultados_.copy()

    name = []
    for en in entradas_:
        for th in threads_:
            for bs in bootstrap_:
                name.append(bs + th + en)

    for i, j in enumerate(dados_['JobName']):
        for n in name:
            if (j == n):
                aux = j
                break;
            if (j == 'raxmlHPC-HYBRID-AVX'):
                dados_.loc[i, "JobName"] = aux

    dados_[['Bootstrap', 'Thread', 'Arquivo de entrada']] = dados_['JobName'].str.split('-',expand=True)
    dados_.dropna(axis=0, inplace=True)
    dados_.drop(dados_.loc[dados_['State'] == 'FAILED'].index, inplace=True)
    dados_.drop(dados_.loc[dados_['Arquivo de entrada'] != 'aminoacido'].index, inplace=True) #retirando os dados que não se referem ao arquivo aminoacido

    for a, j in dados_.iterrows(): #retirando os caracteres das colunas bootstrap e thread
        dados_.loc[a, 'Bootstrap'] = ''.join(filter(lambda i: i.isdigit(), j.Bootstrap))
        dados_.loc[a, 'Thread'] = ''.join(filter(lambda i: i.isdigit(), j.Thread))

    dados_ = convertendo(dados_)
    return dados_

def convertendo(resultados_):
    substring = ["K", "M"]
    for c in substring:
        for a, i in resultados_.iterrows():
            r = str(i.MaxRSS).find(str(c))
            if (r != -1 and str(i.MaxRSS[r]) == 'K'):
                i.MaxRSS = ''.join(filter(lambda j: j.isdigit(), i.MaxRSS))
                resultados_.loc[a, 'MaxRSS'] = float(i.MaxRSS)/(1024*1024)
            elif (r != -1 and str(i.MaxRSS[r]) == 'M'):
                i.MaxRSS = ''.join(filter(lambda j: j.isdigit(), i.MaxRSS))
                resultados_.loc[a, 'MaxRSS'] = float(i.MaxRSS)/1024
    return resultados_

def modelo_treinamento(dados_, val_saida):
    variavel_de_entrada_treinamento = ['Bootstrap', 'Thread', 'NNodes']
    variavel_de_saida_treinamento = val_saida

    modelo = ExtraTreesRegressor()
    modelo.fit(dados_[variavel_de_entrada_treinamento], dados_[variavel_de_saida_treinamento].values.ravel())

    return modelo

path_atual = os.path.dirname(os.path.realpath(__file__))
arq_entrada = path_atual+'/base-de-dados/resultados_aminoacido.csv'
resultados = pd.read_csv(arq_entrada, sep=',')
threads = ['24th-']
entradas = ['aminoacido']
bootstrap = ['10bs-', '100bs-', '1000bs-', '2000bs-']
variavel_saida = ['Elapsed'] #'MaxRSS'

dados = tratar_dados(resultados, entradas, threads, bootstrap)
modelo = modelo_treinamento(dados, variavel_saida)
with open(path_atual+'/base-de-dados/modelo_treinado_'+arq_entrada[arq_entrada.index('resultados'):]+'.pickle', 'wb') as f:
    pickle.dump(modelo, f, pickle.HIGHEST_PROTOCOL)
