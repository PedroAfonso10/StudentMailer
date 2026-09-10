def carregarImagem(msg):

    with open("Emails/imagem.jpeg", "rb") as arquivo:
        dados_imagem = arquivo.read()
    
    msg.add_related(
            dados_imagem,
            maintype="image",
            subtype="jpeg",
            cid="banner_trilha_tech"
        )

    return msg

def messagemReprovado(nome):
    messagem = f"""\
<html>
  <body style="font-family: Arial, sans-serif; color: #333; line-height: 1.6;">
    <p>Olá, {nome}! Tudo bem?</p>

    <p>Agradecemos seu interesse em participar do curso Trilha Tech e pela sua participação no processo seletivo.</p>

    <p>Após a análise das inscrições, informamos que, nesta edição, você não foi selecionado(a) para participar do curso.</p>

    <p>Ressaltamos que esta não é a única oportunidade: novas edições da Trilha Tech e outras iniciativas acadêmicas serão divulgadas futuramente, possibilitando que você participe de novos processos seletivos.</p>

    <p>Esperamos que você continue buscando crescimento na área de tecnologia e que possa fazer parte de uma de nossas próximas iniciativas.</p>

    <p>Agradecemos pelo seu interesse e desejamos sucesso em sua trajetória acadêmica e profissional!</p>

    <!-- BANNER / ASSINATURA -->
    <br>
    <img src="cid:banner_trilha_tech" alt="Trilha Tech" style="max-width: 100%; height: auto;">
  </body>
</html>
"""
    return messagem


def messagemAprovado(nome):
    messagem = f"""\
<html>
  <body style="font-family: Arial, sans-serif; color: #333; line-height: 1.6;">
    <p>Olá, {nome}! Tudo bem?</p>

    <p>É com satisfação que informamos que você foi aprovado(a) para participar do curso Trilha Tech.</p>

    <p>Esta será uma importante oportunidade para ampliar seus conhecimentos na área de tecnologia, desenvolver novas competências e vivenciar uma experiência voltada à sua formação acadêmica e profissional.</p>

    <p>As aulas terão início no dia <strong>11/09/2026</strong>, das <strong>10h às 11h40</strong>.</p>

    <p>Para acompanhar o curso, acesse nossa turma no Google Classroom:<br>
    🔗 Link: <a href="https://classroom.google.com/c/ODY5NTIzOTg4MTI1?cjc=3upkh545">https://classroom.google.com/c/ODY5NTIzOTg4MTI1?cjc=3upkh545</a><br>
    🔑 Código da turma: 3upkh545</p>

    <p>Ao longo do curso, esperamos contar com sua dedicação, participação e disposição para aprender, aproveitando cada encontro como uma oportunidade de desenvolvimento e construção de conhecimento.</p>

    <p>Parabéns pela aprovação, {nome}! Esperamos você no primeiro encontro da Trilha Tech.</p>

    <!-- BANNER / ASSINATURA -->
    <br>
    <img src="cid:banner_trilha_tech" alt="Trilha Tech" style="max-width: 100%; height: auto;">
  </body>
</html>
"""
    return messagem