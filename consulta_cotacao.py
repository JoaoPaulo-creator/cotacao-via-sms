from httpx import get


def consulta_cotacao_moeda(link_consulta):
    requisicao = get(link_consulta, timeout=None)
    saida_em_json = requisicao.json()['USDBRL']

    um_dolar_em_real = saida_em_json['ask']
    valor_cotado = saida_em_json['ask']
    maxima_do_dia = saida_em_json['high']
    minima_do_dia = saida_em_json['low']
    variacao = saida_em_json['varBid']

    output = f'\n COTAÇÃO DO DÓLAR AMERICANO \n' \
             f'\nUSD 1 = R$ {um_dolar_em_real}\n' \
             f'Valor cotado: {valor_cotado}\n' \
             f'Maxima do dia: {maxima_do_dia}\n' \
             f'Mínima do dia: {minima_do_dia}\n' \
             f'Variação: {variacao}'

    return output
