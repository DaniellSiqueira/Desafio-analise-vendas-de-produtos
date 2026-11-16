# Desafio: Análise de Vendas de Produtos

Projeto desenvolvido como parte dos exercícios da **Aula 07 – Funções em Python e Estrutura de Dados – Parte 1**, da Jornada de Dados.

O objetivo é praticar a criação e reutilização de funções em Python, leitura de arquivos CSV, manipulação de listas e dicionários e organização de código em módulos.

## 🎯 Sobre o desafio

O desafio proposto pela Jornada de Dados consiste em desenvolver um pequeno processo de análise de vendas a partir de um arquivo CSV contendo informações sobre produtos.

A solução deve realizar três etapas principais:

1. Ler o arquivo CSV e carregar os dados.
2. Organizar os registros em um dicionário, agrupando os produtos por categoria.
3. Calcular o total de vendas de cada categoria, considerando a quantidade vendida e o valor unitário de cada produto.

O resultado esperado é um dicionário contendo as categorias e seus respectivos totais de vendas.

**Fonte:** [Jornada de Dados – Aula 07](https://github.com/lvgalvao/data-engineering-roadmap/tree/main/03-python-avancado-para-dados/aula07)

## 🛠️ Desenvolvimento

A resolução foi desenvolvida em etapas, começando pela implementação das funções solicitadas e evoluindo posteriormente para uma estrutura mais organizada e reutilizável.

### 1. Primeira versão: implementação das funções

Inicialmente, as três funções foram desenvolvidas em um único arquivo Python, com o objetivo de resolver o problema proposto.

**`ler_csv()`**

Responsável pela leitura do arquivo CSV utilizando a biblioteca `csv` e `DictReader`, retornando os registros em uma lista de dicionários.

**`processar_dados()`**

Responsável por percorrer os registros e agrupá-los em um dicionário, utilizando a categoria como chave e uma lista de produtos como valor.

Cada produto é representado por um dicionário contendo:

- Produto
- Quantidade
- Venda

**`calcular_vendas_categoria()`**

Responsável por percorrer o dicionário processado, calcular o valor total de cada produto (quantidade × valor unitário) e acumular os resultados por categoria.

O resultado é um novo dicionário contendo o total de vendas de cada categoria.

### 2. Evolução: modularização do código

Após concluir a lógica do desafio, o código foi reorganizado para separar as funções da execução principal do programa.

Essa etapa teve como objetivo praticar a modularização e tornar as funções mais reutilizáveis.

O código foi dividido em dois arquivos:

**`funcoes_vendas.py`**

Passou a concentrar as três funções desenvolvidas no desafio.

Uma adaptação importante foi realizada na função `ler_csv()`: o caminho do arquivo passou a ser recebido como parâmetro, em vez de ficar definido diretamente no escopo global do módulo.

Com isso, a função pode ser reutilizada para ler diferentes arquivos CSV.

**`main.py`**

Foi criado para centralizar a execução do programa.

Esse arquivo importa as funções de `funcoes_vendas.py` e organiza o fluxo de processamento:

1. Define o arquivo que será utilizado.
2. Executa a leitura dos dados.
3. Encaminha os dados para processamento.
4. Calcula as vendas por categoria.
5. Exibe os resultados.

Também foi utilizado o padrão:

```python
if __name__ == '__main__':
    main()
```

Esse recurso permite que a função principal seja executada quando o arquivo `main.py` é chamado diretamente, sem executar automaticamente o programa quando o módulo é importado por outro arquivo.

## 📁 Estrutura do projeto

```text
desafio_analise_vendas_produtos/
│
├── funcoes_vendas.py
├── main.py
├── vendas.csv
└── README.md
```

| Arquivo             | Responsabilidade                                         |
| ------------------- | -------------------------------------------------------- |
| `funcoes_vendas.py` | Armazenar as funções de leitura, processamento e cálculo |
| `main.py`           | Organizar e executar o fluxo principal do programa       |
| `vendas.csv`        | Arquivo de entrada com os dados de vendas                |
| `README.md`         | Documentação do projeto                                  |

## ▶️ Como executar

**Pré-requisitos:**

- Python instalado.
- Arquivo `vendas.csv` disponível na pasta do projeto.

Não é necessária a instalação de bibliotecas externas, pois o projeto utiliza a biblioteca nativa `csv` do Python.

Com o terminal aberto na pasta do projeto, execute:

```bash
python main.py
```

## 📊 Resultado esperado

Considerando os dados presentes no arquivo `vendas.csv`, o programa retorna os seguintes totais:

```text
Electronics: R$ 23000
Apparel: R$ 900
Kitchen: R$ 300
```

## 📚 Conceitos praticados

Durante o desenvolvimento, foram trabalhados os seguintes conceitos:

- Definição e chamada de funções com `def`.
- Parâmetros, argumentos e valores de retorno com `return`.
- Type Hints para indicação dos tipos de entrada e saída.
- Leitura de arquivos CSV com `csv.DictReader`.
- Manipulação de listas e dicionários.
- Iteração com estruturas `for`.
- Utilização de acumuladores para cálculos.
- Modularização e reutilização de funções.
- Importação de funções entre arquivos Python.
- Organização do fluxo de execução com `main()`.
- Utilização de `if __name__ == '__main__'`.

## 💡 Considerações finais

O desenvolvimento começou com a resolução direta do problema proposto, priorizando a compreensão da lógica de leitura, agrupamento e cálculo dos dados.

Posteriormente, o código foi reorganizado para separar as responsabilidades em módulos, permitindo maior reutilização e uma estrutura mais próxima da organização utilizada em projetos Python.

O exercício foi uma oportunidade de consolidar os fundamentos de funções e estruturas de dados, além de dar os primeiros passos em boas práticas de organização de projetos.
