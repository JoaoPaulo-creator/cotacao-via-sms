from datetime import datetime
from time import sleep

import constants as const
from consulta_cotacao import consulta_cotacao_moeda
from envio_sms import message_sms


def main():
    corpo_mensagem = consulta_cotacao_moeda(const.LINK_COTACAO_MOEDAS)

    numero_destino_sms = const.DESTINATION_NUMBER
    message_sms(corpo_mensagem, numero_destino_sms)


if __name__ == '__main__':

    while True:
        hora = datetime.today().strftime("%H%M")
        hora_convertida_int = eval(hora)

        match hora_convertida_int:
            case 1936:
                main()
                sleep(20)
            case 1937:
                break

