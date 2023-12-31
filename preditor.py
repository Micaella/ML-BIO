import pandas as pd
import numpy as np
import re
import pickle
import os
import sys

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

path_atual = os.path.dirname(os.path.realpath(__file__))
arq_entrada = path_atual+'/base-de-dados/modelo_treinado_resultados_aminoacido.csv.pickle'

with open(arq_entrada, 'rb') as handle:
    modelo = pickle.load(handle)

#Buscando o valor de bootstrap
with open(path_atual+'/RAxML_v_008_002_012_executar.sh', 'r') as f:
    conteudo = f.read()
valor = re.search(r'RAXML_BOOTSTRAP=(\w+)', conteudo)

if valor:
    try:
        bootstrap = float(valor.group(1))
    except ValueError:
        print("Erro: o valor encontrado não é numérico.")
        sys.exit(1)  # Encerra a execução com um código de erro
else:
    print("Valor não encontrado.")
    sys.exit(1) # Encerra a execução com um código de erro

nodes = preditor_temp(modelo, bootstrap, 24, 1)

# Abrir o arquivo em modo de leitura e substituir o numero de nos (nodes)
with open(path_atual+'/RAxML_v_008_002_012_pre.script', 'r+') as fd:
    txt = fd.read()
    txt = re.sub(r'nodes=\w+', "nodes=" + str(nodes), txt)
    txt = re.sub(r'ntasks=\w+', "ntasks=" + str(nodes), txt) # Como está sendo usado 1 processo MPI, ntasks fica igual ao núemro de nos
    fd.seek(0)
    fd.write(txt)
