#aqui declarar as listas ou ver se dá pra linkar.

cadastrar = 'S'
while cadastrar.upper() == 'S':
    nome = input('Digite o nome do professor: ')
    alunos.append(nome)
    tel = input('Digite o telefone do professor: ')
    telefones.append(tel)
    email = input('Digite o email do professor: ')
    emails.append(email)
    curso = input('Digite o curso do professor: ')
    curso_aluno.append(curso)
    print('Cursos do(a) professor(a) {} cadastrados até agora: {}.'.format(nome, curso_aluno))
    outro_curso = input('Deseja cadastrar outro curso para o mesmo professor? (S/N) ')
    while outro_curso.upper() == 'S':
        curso = input('Digite o curso do professor: ')
        curso_aluno.append(curso)
        print('curso professor: ', curso_aluno)
        outro_curso = input('Deseja cadastrar outro curso para o mesmo professor? (S/N) ')
    i += 1
    cursos.insert(i, curso_aluno[:])
    curso_aluno.clear()
    cadastrar = input('Deseja cadastrar outro professor? (S/N) ')