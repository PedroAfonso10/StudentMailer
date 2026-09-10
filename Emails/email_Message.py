from email.message import EmailMessage
from Emails.message import messagemAprovado
from Emails.message import messagemReprovado

def message(nome, situacao):
    """
    Monta um EmailMessage pronto para envio, com base na situação
    (aprovado/reprovado) e no nome do participante.
    Retorna um novo objeto EmailMessage a cada chamada.
    """
    situacao = str(situacao).strip().lower()
    nome = str(nome).strip()

    msg = EmailMessage()

    if situacao == 'reprovado':
        msg.set_content(messagemReprovado(nome))
    elif situacao == 'aprovado':
        msg.set_content(messagemAprovado(nome))
    else:
        raise ValueError('VALOR INVÁLIDO')

    return msg