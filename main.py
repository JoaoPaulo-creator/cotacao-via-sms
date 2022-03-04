from envio_sms import message
import constants as const
from consulta_cotacao import consulta_cotacao_moeda


def main():
    corpo_mensagem = consulta_cotacao_moeda(const.LINK_COTACAO_MOEDAS)
    numero_destino = const.DESTINATION_NUMBER

    message(corpo_mensagem, numero_destino)


if __name__ == '__main__':
    main()
