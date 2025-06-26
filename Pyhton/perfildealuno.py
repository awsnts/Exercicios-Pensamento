quantidade_total = 0
alunos_primeira = 0
alunos_segunda = 0
alunos_terceira = 0
alunos_quarta = 0
livros_lidos = 0
total_livros = 0
gosta_redacao = 0
nao_gosta_redacao = 0
resposta = ""
porcentagem = 0
serie = 0

while True:
    serie = int(input("Digite a série do aluno (1 a 4): "))
    if serie == 1:
        livros_lidos = int(input("Quantos livros você leu no último mês? "))
        gosta_redacao = int(input("Você gosta de redação? (1 para sim, 2 para não): "))
        alunos_primeira += 1
        if gosta_redacao == 1:
            resposta = "sim"
        else:   
            resposta = "não"
        print(f"Total alunos 1° serie: {alunos_primeira}")
        print(f"Aluno do 1º ano, leu {livros_lidos} livros e gosta de redação ? {resposta}.")
        
    elif serie == 2:
        livros_lidos = int(input("Quantos livros você leu no último mês? "))
        gosta_redacao = int(input("Você gosta de redação? (1 para sim, 2 para não): "))
        alunos_segunda += 1
        if gosta_redacao == 1:
            resposta = "sim"
        else:   
            resposta = "não"
        print(f"Total alunos 2° serie: {alunos_segunda}")
        print(f"Aluno do 2º ano, leu {livros_lidos} livros e gosta de redação: {resposta}.")

    elif serie == 3:
        livros_lidos = int(input("Quantos livros você leu no último mês? "))
        gosta_redacao = int(input("Você gosta de redação? (1 para sim, 2 para não): "))
        alunos_terceira += 1
        if gosta_redacao == 1:
            resposta = "sim"
        else:   
            resposta = "não"
        if gosta_redacao ==2:
            nao_gosta_redacao += 1
            porcentagem = (nao_gosta_redacao / alunos_terceira) * 100
        print(f"Porcentagem de alunos que não gostam de redação na 3° série: {porcentagem:.2f}%")
        print(f"Total de alunos que não gostam de redação: {nao_gosta_redacao}")
        print(f"Total alunos na 3° serie: {alunos_terceira}")
        print(f"Aluno do 3º ano, leu {livros_lidos} livros e gosta de redação: {resposta}.")

    elif serie == 4:
        livros_lidos = int(input("Quantos livros você leu no último mês? "))
        gosta_redacao = int(input("Você gosta de redação? (1 para sim, 2 para não): "))
        alunos_quarta += 1
        if gosta_redacao == 1:
            resposta = "sim"
        else:   
            resposta = "não"
        if total_livros < livros_lidos:
            total_livros = livros_lidos
        print(f"O maior número de livros lidos do 4°ano foi de : {total_livros} livros.")
        print(f"Total alunos na 4° serie: {alunos_quarta}")
        print(f"Aluno do 4º ano, leu {livros_lidos} livros e gosta de redação: {resposta}.")

    elif serie < 1 or serie > 4:
        print("Serie inválida. Por favor, digite um número de 1 a 4.")
        break
