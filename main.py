
from funcoes_vendas import ler_csv, processar_dados, calcular_vendas_categoria

def main():
    nome_arquivo = 'vendas.csv'

    dados_brutos = ler_csv(nome_arquivo)
    dados_processados = processar_dados(dados_brutos)
    vendas_categoria = calcular_vendas_categoria(dados_processados)

    for categoria, total in vendas_categoria.items():
        print(f'{categoria}: R$ {total}')


if __name__ == '__main__':
    main()
