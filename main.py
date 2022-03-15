import constants as const
from consulta_cotacao import consulta_cotacao_moeda
from envio_mensagem_whatsapp import message_whats
from envio_sms import message_sms
from datetime import datetime


def main():
    corpo_mensagem = consulta_cotacao_moeda(const.LINK_COTACAO_MOEDAS)

    numero_destino_whats = const.DESTINATION_WHATSAPP_NUMBER
    message_whats(corpo_mensagem, numero_destino_whats)

    numero_destino_sms = const.DESTINATION_NUMBER
    message_sms(corpo_mensagem, numero_destino_sms)


if __name__ == '__main__':
    main()

    # Experimental
    while True:
        hora = datetime.today().strftime('%H%M')
        hora_convertida_int = eval(hora)

        match hora_convertida_int:
            case True:
                if hora_convertida_int > 1000:
                    main()
            case 1800:
                break
