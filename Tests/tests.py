import pytest
from httpx import get
import constants as const
from datetime import datetime



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
             f'Mínima do dia: {minima_do_dia}\n'

    valorizacao = ...
    depreciacao = eval(maxima_do_dia) - eval(valor_cotado)

    if eval(variacao) > 0:
        print(output + f'\nValorização: {valorizacao:.4f}')

    else:
        print(output + f'Depreciação: {depreciacao:.4f}')

    return


LINK_COTACAO_MOEDAS = 'https://economia.awesomeapi.com.br/last/USD-BRL'


def test_validando_requisicao():

    requisicao = get(LINK_COTACAO_MOEDAS, timeout=None)
    print(f'\n{requisicao.status_code}')

    for sucesso_consulta in range(200, 300):
        lista_sucesso_cosulta = [sucesso_consulta]
        if requisicao.status_code in lista_sucesso_cosulta:
            print('A consulta deu certo')

    for nao_econtrado in range(400, 500):
        lista_nao_encontrado = [nao_econtrado]
        if requisicao.status_code in lista_nao_encontrado:
            print('Cotação não encontrada')

    for erro_servidor in range(500, 600):
        lista_erro_servidor = [erro_servidor]
        if requisicao.status_code in lista_erro_servidor:
            print('Não foi possível consultar cotação devido a um erro interno')

    return


def test_validando_horario():
    while True:
        hora = datetime.today().strftime('%H%M')
        hora_convertida_int = eval(hora)

        match hora_convertida_int:
            case True:
                print(hora_convertida_int)
            case 1610:
                break
