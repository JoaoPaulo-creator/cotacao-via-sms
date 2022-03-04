import pytest
from httpx import get
import constants as const


def test_consulta_cotacao_moeda():
    requisicao = get(const.LINK_COTACAO_MOEDAS, timeout=None)
    saida_em_json = requisicao.json()['USDBRL']

    um_dolar_em_real = saida_em_json['ask']
    valor_cotado = saida_em_json['ask']
    maxima_do_dia = saida_em_json['high']
    minima_do_dia = saida_em_json['low']
    variacao = saida_em_json['varBid']

    output = f'\n' \
             f'\nUSD 1 = R$ {um_dolar_em_real}\n' \
             f'Valor cotado: {valor_cotado}\n' \
             f'Maxima do dia: {maxima_do_dia}\n' \
             f'Mínima do dia: {minima_do_dia}\n' \
             f'Variação: {variacao}'

    saida = {'\nMaxima do dia: ': eval(maxima_do_dia), '\nMinimma do dia: ': minima_do_dia}
    # TODO: realizar um teste, onde os valores atribuidos as variáveis saiam na impressão, conforme está organizado
    #  no dicionário "saida"#

    a = f'{maxima_do_dia, minima_do_dia}'.join(saida)
    print(output)
