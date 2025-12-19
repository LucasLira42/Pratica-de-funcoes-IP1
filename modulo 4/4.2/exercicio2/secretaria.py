def main():
 
 from alunos import matricular_aluno
 from disciplinas import inscrever_em_disciplina
 from notas import lancar_nota_inicial
 
 matricular_aluno("Lucas")
 
 inscrever_em_disciplina( 2024001 , "calculo I")

 lancar_nota_inicial( 2024001 , "calculo I")



if __name__ == "__main__":
    main()