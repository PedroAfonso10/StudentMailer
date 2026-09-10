from email.message import EmailMessage
from Emails.message import messagemAprovado
from Emails.message import messagemReprovado
from Emails.message import carregarImagem

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
        msg.set_content(messagemReprovado(nome), subtype='html')
    elif situacao == 'aprovado':
        msg.set_content(messagemAprovado(nome), subtype='html')
    else:
        raise ValueError(f'VALOR INVÁLIDO: nome={nome!r}, situacao={situacao!r}')

    carregarImagem(msg)
    return msg