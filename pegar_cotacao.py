import requests


def pegar_cotacao_moedas(moeda_origem, moeda_destino):

    link = f'https://economia.awesomeapi.com.br/last/{moeda_origem}-{moeda_destino}'
    requisisao = requests.get(link)

    cotacao = requisisao.json()[f'{moeda_origem}{moeda_destino}']['bid']
    return cotacao