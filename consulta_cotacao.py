from httpx import get
from tratando_requisicao import verificando_status_erro_requisicao


def consulta_cotacao_moeda(link_consulta):
    USD = 'USD'
    BRL = 'BRL'
    PARES = f'{USD}-{BRL}'
    PARES_JSON = f'{USD}{BRL}'

    requisicao = get(f'{link_consulta}/{PARES}', timeout=None)

    if verificando_status_erro_requisicao(requisicao):
        verificando_status_erro_requisicao(requisicao)
    else:
        saida_em_json = requisicao.json()[f'{PARES_JSON}']
        valor_cotado = saida_em_json['ask']
        maxima_do_dia = saida_em_json['high']
        minima_do_dia = saida_em_json['low']
        variacao = saida_em_json['varBid']

        output = f'\n COTAÇÃO DO DÓLAR AMERICANO \n' \
                 f'\nUSD 1 = R$ {valor_cotado}\n' \
                 f'Valor cotado: {valor_cotado}\n' \
                 f'Maxima do dia: {maxima_do_dia}\n' \
                 f'Mínima do dia: {minima_do_dia}\n' \
                 f'Variação: {variacao}'

        return output
