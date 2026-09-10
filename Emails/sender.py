from Students.planilha import carregar_alunos
from StudentMailer.Emails.email_Message import message
from Emails.message import carregarImagem

def enviar_email(EMAIL_REMETENTE):
    for nome, email, situacao in carregar_alunos():
        msg = message(nome, situacao)
        msg['To'] = email
        msg['From'] = EMAIL_REMETENTE
        msg['Subject'] = 'Resultado do processo seletivo - Trilha Tech'
        carregarImagem(msg)
        yield msg
    
