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
    tel = input('Digite o telefone do aluno: ')
    telefones.append(tel)
    email = input('Digite o email do aluno: ')
    emails.append(email)
    curso = input('Digite o curso do aluno: ')
    curso_aluno.append(curso)
    outro_curso = input('Deseja cadastrar outro curso para o mesmo aluno? (S/N) ')
    while outro_curso == 'S':
        i = 1
        curso = input('Digite o curso do aluno: ')
        curso_aluno.append(curso)
        outro_curso = input('Deseja cadastrar outro curso para o mesmo aluno? (S/N) ')
        i = i + 1
    cursos.append(curso_aluno)
    curso_aluno.clear
    cadastrar = input('Deseja cadastrar outro aluno? (S/N) ')

print(alunos)
print(telefones)
print(emails)
print(cursos)