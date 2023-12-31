# ML-BIO

A ML-BIO é uma ferramenta que utiliza técnicas de aprendizado de máquina para otimizar o desempenho de aplicações no [BioinfoPortal](https://bioinfo.lncc.br/). Este portal é uma iniciativa colaborativa entre LABINFO, CENAPAD-RJ e SINAPAD, que facilita o acesso a recursos de computação de alto desempenho disponíveis no supercomputador [Santos Dumont](https://sdumont.lncc.br/) (SDumont).

## Objetivo da Ferramenta
A ML-Bio é especialmente projetada para determinar a configuração idela de parâmetros para aplicações hospedadas no BioinfoPortal. Utilizando a aplicação RAxML como caso de estudo, esta ferramenta busca ajustar as configurações de forma personalizada, visando melhorar o desempenho e a eficiência do BioinfoPortal e do SDumont.

## Pré-requisitos

* Python 3.8.10 
* Bibliotecas: pandas, numpy e scikit-learn.
```
pip install pandas numpy scikit-learn
```
* Base de dados (disponível no diretório `base-de-dados` desse repositório)

## Modelo Preditivo
A ferramenta emprega um modelo de regressão supervisionado, implementado pelo algoritmo Extra Trees Regressor. Este modelo é treinado com dados históricos de execuções anteriores, permitindo a ML-BIO prever a quantidade ideal de nós necessários para cada execução.

## Componentes da ML-BIO
A ML-BIO consiste em duas etapas, ambos desenvolvidos em Python:

1. **Módulo de Treinamento (`treinamento.py`):**
   - Realiza o pré-processamento dos dados.
   - Executa o treinamento do modelo ExtraTreesRegressor.
   - Salva o modelo treinado para uso futuro.
   - Para iniciar o treinamento, execute no terminal:
     ```bash
     python3 treinamento.py
     ```
Esse módulo pode ser executado apenas uma vez, sem necessidade de retreinamento. Caso já possua o modelo treinado não há nessecidade do uso desse módulo.

2. **Módulo Preditor (`preditor.py`):**
   - Realiza previsões da quantidade de nós ideal.
   - Atualiza o script `RAxML_v_008_002_012_pre.script` com os valores preditos.
   - Prepara o script para submissão ao metaescalonador do BioinfoPortal.
   - Para executar a previsão, use o comando:
     ```bash
     python3 preditor.py
     ```

## Estrutura de Diretórios e Arquivos
- `base-de-dados/`: Contém amostras de arquivos de saída e de entrada usados pela ferramenta.
- `resultados_aminoacido.csv`: Exemplo de base de dados utilizada para treinar o modelo.
- `modelo_treinamento_resultados_aminoacido.csv.pickle`: O modelo treinado, pronto para uso nas previsões.


## Cite
Se você considerar a Ferramenta ML-BIO ou a base de dados úteis para sua pesquisa, recomendamos citar os seguintes artigos em seus trabalhos:

```
@inproceedings{wscad,
 author = {Micaella Coelho and Guilherme Freire and Kary Ocaña and Carla Osthoff and Marcelo Galheigo and André Carneiro and Francieli Boito and Philippe Navaux and Douglas Cardoso},
 title = {Desenvolvimento de um Framework de Aprendizado de Máquina no Apoio a Gateways Científicos Verdes, Inteligentes e Eficientes: BioinfoPortal como Caso de Estudo Brasileiro},
 booktitle = {Anais do XXIII Simpósio em Sistemas Computacionais de Alto Desempenho},
 location = {Florianópolis},
 year = {2022},
 pages = {205--216},
 publisher = {SBC},
 address = {Porto Alegre, RS, Brasil},
 doi = {10.5753/wscad.2022.226377},
 url = {https://sol.sbc.org.br/index.php/wscad/article/view/21945}
}

@inproceedings{coelho2022development,
  title={Development of a Machine Learning Framework to Support Efficient Scientific Gateways},
  author={Coelho, M. and Freire, G. and Ocaña, K. and Osthoff, C. and Galheigo, M. and Carneiro, A.R. and Boito, F. and Navaux, P. and Cardoso, D.O.},
  booktitle={Conferência Latino-Americana de Computação de Alto Desempenho (BioCARLA)},
  address={Porto Alegre, Brasil},
  year={2022}
}
```
