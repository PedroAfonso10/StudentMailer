def carregarImagem(msg):

    with open("Emails/imagem.jpeg", "rb") as arquivo:
        dados = arquivo.read()

    msg.add_attachment(
        dados,
        maintype="image",
        subtype="jpeg",
        filename="imagem.jpeg"
    )

    return msg


def messagemReprovado(nome):
    messagem = f"""
Olá, {nome}! Tudo bem?

Agradecemos seu interesse em participar do curso Trilha Tech e pela sua participação no processo seletivo.

Após a análise das inscrições, informamos que, nesta edição, você não foi selecionado(a) para participar do curso.

Ressaltamos que esta não é a única oportunidade: novas edições da Trilha Tech e outras iniciativas acadêmicas serão divulgadas futuramente, possibilitando que você participe de novos processos seletivos.

Esperamos que você continue buscando crescimento na área de tecnologia e que possa fazer parte de uma de nossas próximas iniciativas.

Agradecemos pelo seu interesse e desejamos sucesso em sua trajetória acadêmica e profissional!
 """
    
    return messagem


def messagemAprovado(nome):
    messagem = f"""
Olá, {nome}! Tudo bem?

É com satisfação que informamos que você foi aprovado(a) para participar do curso Trilha Tech.

Esta será uma importante oportunidade para ampliar seus conhecimentos na área de tecnologia, desenvolver novas competências e vivenciar uma experiência voltada à sua formação acadêmica e profissional.

As aulas terão início no dia 11/09/2026, das 10h às 11h40.

Para acompanhar o curso, acesse nossa turma no Google Classroom:
🔗 Link: https://classroom.google.com/c/ODY5NTIzOTg4MTI1?cjc=3upkh545
🔑 Código da turma: 3upkh545

Ao longo do curso, esperamos contar com sua dedicação, participação e disposição para aprender, aproveitando cada encontro como uma oportunidade de desenvolvimento e construção de conhecimento.

Parabéns pela aprovação, {nome}! Esperamos você no primeiro encontro da Trilha Tech.
"""
    return messagem