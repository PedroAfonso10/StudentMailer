from dotenv import load_dotenv
import os
import smtplib 
from Emails.sender import enviar_email

if __name__ == '__main__':
    load_dotenv()
    EMAIL_REMETENTE = os.getenv('EMAIL_REMETENTE')
    SENHA_APP = os.getenv('SENHA_APP')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as email:
        email.login(EMAIL_REMETENTE, SENHA_APP)
        for msg in enviar_email(EMAIL_REMETENTE):
            email.send_message(msg)