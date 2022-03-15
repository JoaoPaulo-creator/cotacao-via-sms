import os.path

LINK_COTACAO_MOEDAS = 'https://economia.awesomeapi.com.br/last/'

dir_root = 'C:\\Constantes\\'

dir_telefone_destino = f'{dir_root}DESTINATION_NUMBER.txt'
dir_telefone_whats_destino = f'{dir_root}DESTINATION_WHATSAPP_NUMBER.txt'

dir_twilio_account_sid = f'{dir_root}TWILIO_ACCOUNT_SID.txt'
dir_twilio_auth_token = f'{dir_root}TWILIO_AUTH_TOKEN.txt'

dir_twilio_phone_number = f'{dir_root}TWILIO_PHONE_NUMBER.txt'


file_ = os.path.exists(dir_root)

if file_:

    with open(dir_twilio_account_sid, 'r') as tas:
        TWILIO_ACCOUNT_SID = tas.read()
        tas.close()

    with open(dir_twilio_auth_token, 'r') as tat:
        TWILIO_AUTH_TOKEN = tat.read()
        tat.close()

    with open(dir_twilio_phone_number, 'r') as tpn:
        TWILIO_PHONE_NUMBER = tpn.read()
        tpn.close()

    with open(dir_telefone_destino, 'r') as dpn:
        DESTINATION_NUMBER = dpn.read()
        dpn.close()


else:
    print('Diretório inexistente')
