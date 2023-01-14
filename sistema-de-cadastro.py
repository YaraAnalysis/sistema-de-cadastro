# Este programa faz o cadastro de alunos

alunos = []
telefones = []
emails = []
cursos = []
curso_aluno = []

cadastrar = input('Deseja iniciar o cadastro dos alunos? (S/N) ')
while cadastrar == 'S':
    aluno = input('Digite o nome do aluno: ')
    alunos.append(aluno)
    curso = input('Digite o curso do aluno: ')
    cursos.append(curso)
    tel = input('Digite o telefone do aluno: ')
    telefones.append(tel)
    email = input('Digite o email do aluno: ')
    emails.append(email)
    cadastrar = input('Deseja cadastrar outro aluno? (S/N) ')



print(alunos)
print(telefones)
print(emails)
print(cursos)