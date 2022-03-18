from datetime import datetime
from time import sleep

import constants as const
from consulta_cotacao import consulta_cotacao_moeda
from envio_sms import message_sms


def main():
    corpo_mensagem = consulta_cotacao_moeda(const.LINK_COTACAO_MOEDAS)

    numero_destino_sms = const.DESTINATION_NUMBER
    message_sms(corpo_mensagem, numero_destino_sms)


def numero_de_envio_sms(nro_envios):
    if nro_envios == 2:
        exit()


if __name__ == '__main__':

    hora = datetime.today().strftime("%H%M")
    hora_convertida_int = eval(hora)
    numero_envio = 0
    while True:
        sleep(2)
        numero_envio += 1
        match hora_convertida_int:
            case 1816:
                main()
                numero_de_envio_sms(numero_envio)
            case 1819:
                main()
                numero_de_envio_sms(numero_envio)
            case 1820:
                break

                
exit()
