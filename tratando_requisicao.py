

def verificando_status_erro_requisicao(requisicao):

    for nao_econtrado in range(400, 500):
        lista_nao_encontrado = [nao_econtrado]
        if requisicao.status_code in lista_nao_encontrado:
            return 'Cotação não encontrada'

    for erro_servidor in range(500, 600):
        lista_erro_servidor = [erro_servidor]
        if requisicao.status_code in lista_erro_servidor:
            return 'Não foi possível consultar cotação devido a um erro interno'

    return
