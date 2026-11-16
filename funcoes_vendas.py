
import csv

caminho_arquivo = 'vendas.csv'

def ler_csv (nome_arquivo: str) -> list[dict]:

    """
    Faz a leitura do arquivo CSV
    """

    with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        return list(leitor)

def processar_dados(vendas: list[dict]) -> dict:

    """
    Processa os dados, 
    deixando eles em um formato especifico solicitado.
    """

    dados_processados = {} 

    for venda in vendas:

        categoria = venda["Categoria"]
        if categoria not in dados_processados:
            dados_processados[categoria] = []

        dados_processados[categoria].append({
            "Produto": venda["Produto"],
            "Quantidade": venda["Quantidade"],
            "Venda": venda["Venda"]
        })

    return dados_processados

def calcular_vendas_categoria(vendas: dict) -> dict:

    """
    Calcula as vendas por categoria
    """

    resultado = {}

    for categoria, lista_vendas in vendas.items():
        
        total_categoria = 0
        
        for venda in lista_vendas:
            valor_produto = int(venda["Venda"]) * int(venda["Quantidade"])
            total_categoria += valor_produto
    
        resultado[categoria] = total_categoria
        
    return resultado

