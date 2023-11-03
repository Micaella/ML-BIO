# ML-BIO

A ML-BIO é uma ferramenta baseada em técnicas de aprendizado de máquina, projetada para melhorar o desempenho das aplicações hospedadas no [BioinfoPortal](https://bioinfo.lncc.br/). O BioinfoPortal é fruto da colaboração entre os pesquisadores do LABINFO, CENAPAD-RJ e SINAPAD, e visa facilitar o acesso aos recursos computacionais do supercomputador [Santos Dumont](https://sdumont.lncc.br/) (SDumont).

A ferramenta ML-Bio, foi desenvolvida para inferir uma combinação de parâmetros que resultam em um bom desempenho das aplicações do BioinfoPortal. Este projeto foi testado e aprimorado tendo a aplicação RAxML como estudo de caso. O propósito da ML-Bio é aprimorar o desempenho do BioinfoPortal, ajustando as configurações de forma personalizadas para atender às exigências específicas de cada aplicação hospedada no portal.

Com a integração completa da ferramenta e as devidas adaptações em todas as aplicações do portal, também contribuímos significativamente para o desempenho tanto do BioinfoPortal quanto do SDumont. A ML-BIO utiliza o modelo preditivo de regressão supervisionado, baseado no algoritmo Extra Trees Regressor, que foi treinado com um conjunto de dados históricos.

Para a concretização desta ferramenta, foi necessário obter uma base de dados robusta, incorporando informações sobre as execuções anteriores da aplicação RAxML. Estes dados foram essenciais para o treinamento eficaz do modelo preditivo, garantindo assim a capacidade do ML-Bio em determinar de maneira precisa a quantidade ideal de nós necessária para cada execução.

## 🚀 Começando
### 📋 Pré-requisitos

* Python 3.8.10 
* Bibliotecas: pandas, numpy e scikit-learn.
```
pip install pandas numpy scikit-learn
```
* Base de dados (disponível no diretório "base-de-dados" desse repositório)

### 📋 Modo de utilização

#### Pré-processamento de dados e Treinamento do Modelo

O arquivo `treinamento.py` é responsável pelo pré-processamento da base de dados e pelo treinamento do modelo. Este processo inclui a limpeza dos dados, conversão de tipos, divisão de colunas, entre outras operações permitidas para preparar os dados para o treinamento.

O modelo é treinado utilizando o algoritmo ExtraTreesRegressor. Após o treinamento, o modelo é salvo em um arquivo para que possa ser utilizado posteriormente, sem a necessidade de retreinamento.

Para executá-lo via linha de comando:
```
python3 treinamento.py
```

#### Inferir o número de nós
O arquivo `preditor.py` é utilizado para predizer a quantidade ideal de nós com base nos dados de treinamento. Para executá-lo via linha de comando:

```
python3 preditor.py
```

Após a execução do "preditor.py", o arquivo "RAxML_v_008_002_012_pre.script" será atualizado com o valor inferido de nós. Dessa forma, ele estará pronto para ser enviado ao metaescalonador, que neste projeto é o metaescalonador do BioinfoPortal.
