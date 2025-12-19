def main():

 historico_aluno = ["Cálculo I", "Lógica"]

 def registrar_disciplina_cursada(historico,disciplina):
    historico.append(disciplina)

 registrar_disciplina_cursada("Programação 1 ")
 print(historico_aluno)


if __name__ == "__main__":
    main()
