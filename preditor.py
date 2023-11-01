import pandas as pd
import numpy as np
import re
import pickle

def preditor_temp(modelo_, bootstrap_, threads_, nodes_, slowdown_factor=3.3):#usando o tempo como medida
    mat = pd.DataFrame({'Bootstrap' : bootstrap_, 'Thread' : threads_, 'NNodes' : 20}, index=[0])
    #calcula o tempo usando o máximo de nós
    x = modelo_.predict(mat)
    y = x*slowdown_factor

    mat.drop(mat.loc[mat['Bootstrap'] == bootstrap_].index, inplace=True)

    #prever o tempo em numeor de nós decersente até acha um tempo aceitável de acordo com y
    for i in range(19, 0, -1):
        mat = pd.DataFrame({'Bootstrap' : bootstrap_, 'Thread' : threads_, 'NNodes' : i}, index=[0])
        tmp_pred = modelo_.predict(mat)
        if tmp_pred >= y:
            return i
        mat.drop(mat.loc[mat['Bootstrap'] == bootstrap_].index, inplace=True)
    return i

arq_entrada = '/mnt/c/Users/miica/wsl/MLBIO/ML-BIO/base-de-dados/modelo_treinado_resultados_aminoacido.csv.pickle'

with open(arq_entrada, 'rb') as handle:
    modelo = pickle.load(handle)

#Buscando o valor de bootstrap
with open('/mnt/c/Users/miica/wsl/MLBIO/ML-BIO/RAxML_v_008_002_012_executar.sh', 'r') as f:
    conteudo = f.read()
valor = re.search(r'RAXML_BOOTSTRAP=(\w+)', conteudo)

if valor:
    bootstrap = float(valor.group(1))
else:
    print("Valor não encontrado.")

nodes = preditor_temp(modelo, bootstrap, 24, 1)
