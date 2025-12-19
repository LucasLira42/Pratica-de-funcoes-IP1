#Narrativa: Um professor quer usar uma função para simular como a nota de um aluno ficaria com um ponto extra. A média da turma, usada na simulação, é um dado temporário.
#Tarefa: Crie uma variável nota_aluno = 7.0. Defina uma função simular_nota_com_bonus(nota). Dentro dela, crie uma variável media_turma = 8.0 e imprima a nota e a media_turma. Chame a função passando nota_aluno. Depois da chamada, tente imprimir media_turma e veja o erro que ocorre.

def main():

 nota_aluno = 7
 def simular_nota_com_bonus(nota):
    media_turma=8 
    print(f"{nota} {media_turma}")

 simular_nota_com_bonus(nota_aluno)
 print(media_turma)

if __name__ == "__main__":
    main()