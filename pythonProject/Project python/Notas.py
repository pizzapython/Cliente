totmedia = 0
for i in range(2):
    aluno = input('Digite o nome do aluno(a):')
    primeira = int(input("Digite a primeira nota"))
    segunda = int(input("Digite a segunda nota"))
    media = (primeira + segunda)/2
    print("A média do aluno é:{0:.2f}".format(media))
    totmedia = totmedia + media
mediger = totmedia/2
print("A média da turma é:{0:.2f}".format(mediger))


