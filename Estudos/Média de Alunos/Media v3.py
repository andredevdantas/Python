#Calcular Media de duas notas de N alunos

n = int(input("Informe o número de alunos: "))

medias = []
controle = 1
while controle <= n:
    n1 = float(input(f"Informe a primeira nota do aluno {controle}: "))
    n2 = float(input(f"Informe a segunda nota do aluno {controle}: "))

    media = round((n1 + n2) / 2,1)
    medias.append((controle, media)) 

    if media >= 6:
        print(f"Aluno {controle} foi aprovado com média {media}")
    else:
        print(f"Infelizmente o aluno {controle} foi reprovado com média {media}")
    
    controle += 1

print("\nMédia dos Alunos: ")
for aluno, media in medias:
    print(f"Aluno {aluno}: {media}")
