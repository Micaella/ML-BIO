# ML-BIO

A ferramenta denominada ML-Bio é baseada em aprendizado de máquina e foi desenvolvida para inferir a combinação de parâmetros que resultam em um bom desempenho das aplicações do BioinfoPortal, usando como caso de estudo a aplicação RAxML. Essa ferramenta visa melhorar o desempenho do BioinfoPortal, personalizando a configuração de acordo com as necessidades de cada aplicação. Tendo em vista a implementação da ferramenta com as adaptações necessárias para todas as aplicações do portal e sua integração à arquitetura do BioinfoPortal, é possível melhorar o desempenho e a eficiência, tanto do BioinfoPortal quanto do SDumont. A ferramenta ML-BIO foi desenvolvida para auxiliar na escolha das configurações de parâmetros para execuções do RAxML no BioinfoPortal, utilizando aprendizado supervisionado regressão. O principal objetivo da ferramenta é determinar a quantidade ideal de nós para cada execução, baseando-se em dados históricos. Para desenvolver a ferramenta, foi necessário criar uma base de dados com informações sobre as execuções da aplicação RAxML, que serviram para treinar o modelo preditivo Extra Trees Regressor.

## 🚀 Começando
### 📋 Pré-requisitos

Para utilizar a ferramenta são necessários o Python 3.8.10 e as bibliotecas: pandas, numpy e scikit-learn.
Uma base de dados. Temos uma base de dados que foi utilizada no nosso estudo e pode ser usada como teste e se encontra no diretório "base-de-dados" desse projeto.

### 📋 Modo de utilização

#### Pré-processamento de dados e Treinamento do Modelo

A base de dados requer um pré-processamento antes do treinamento dos modelos, onde são realizada diversas operações, como a remoção de espaços em branco, conversão de tempos, divisão de colunas, entre outras.

O modelo é treinado utilizando o algoritmo ExtraTreesRegressor, e uma vez treinado, o modelo é salvo em um arquivo serializado e pode ser utilizado para realizar a predição sem a necessidade de re-treinamento. 

Tanto o Pré-pocessamento dos dados quanto o treinamento do modelo, são feito com o código "treinamento.py"

Para executá-lo via linha de comando:
```
python3 treinamento.py
```

#### Inferir o número de nós
Atráves do código "preditor.py" é possível predizer a quantidade de nós ideal baseado nos dados de treinamento. Para executá-lo via linha de comando:

```
python3 preditor.py
```
