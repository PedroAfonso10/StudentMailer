import openpyxl 

def carregar_alunos():
    planilha = openpyxl.load_workbook('Students/Students.xlsx')
    dados = planilha.active
    for linha in dados.iter_rows(min_row=2, values_only=True):
        if linha:
            nome = linha[1]
            email = linha[2]
            situacao = linha[7]
            yield nome, email, situacao

