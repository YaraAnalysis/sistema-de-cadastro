# Este programa faz o cadastro de alunos e cursos do aluno

alunos = []
telefones = []
emails = []
cursos = []
curso_aluno = []
i = 0

cadastrar = 'S'
while cadastrar == 'S':
    nome = input('Digite o nome do aluno: ')
    alunos.append(nome)
    tel = input('Digite o telefone do aluno: ')
    telefones.append(tel)
    email = input('Digite o email do aluno: ')
    emails.append(email)
    curso = input('Digite o curso do aluno: ')
    curso_aluno.append(curso)
    print('Cursos do(a) aluno(a) {} cadastrados até agora: {}.'.format(nome, curso_aluno))
    outro_curso = input('Deseja cadastrar outro curso para o mesmo aluno? (S/N) ')
    while outro_curso == 'S':
        curso = input('Digite o curso do aluno: ')
        curso_aluno.append(curso)
        print('curso aluno: ', curso_aluno)
        outro_curso = input('Deseja cadastrar outro curso para o mesmo aluno? (S/N) ')
    i += 1
    cursos.insert(i, curso_aluno[:])
    curso_aluno.clear()
    cadastrar = input('Deseja cadastrar outro aluno? (S/N) ')

qtd_alunos = len(alunos)
print('\nLista de alunos:')
for i in range(qtd_alunos):
    print('\nAluno: {} | Telefone: {} | E-mail: {} | Cursos: {}.'.format(alunos[i], telefones[i], emails[i], cursos[i]))
print('\nFim do relatório')