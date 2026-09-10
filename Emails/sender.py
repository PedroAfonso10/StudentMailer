from Students.planilha import carregar_alunos
from Emails.email_Message import message

def enviar_email(EMAIL_REMETENTE):
    for nome, email, situacao in carregar_alunos():
        msg = message(nome, situacao)
        msg['To'] = email
        msg['From'] = EMAIL_REMETENTE
        msg['Subject'] = 'Resultado do processo seletivo - Trilha Tech'
        yield msg
    
