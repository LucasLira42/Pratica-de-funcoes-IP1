
#Narrativa: O portal do aluno deve enviar lembretes sobre as próximas provas. O texto do lembrete é padronizado, alterando-se apenas o nome da disciplina. Essas notificações são geradas em momentos diferentes, sempre que um professor agenda uma avaliação.
#Tarefa: Simule o envio de dois avisos. O primeiro, para a variável disciplina = "Cálculo I", deve imprimir: f"Lembrete: A prova da disciplina {disciplina} será na próxima semana.". O segundo, para disciplina = "Algoritmos e Estrutura de Dados", deve imprimir: "Lembrete: A prova da disciplina {disciplina} será na próxima semana."


def main():

    def aviso_prova (subject):
        print( f"Lembrete: A prova da disciplina {subject} será na próxima semana.\n\n")
    
    aviso_prova(subject = "Cálculo NI")

    aviso_prova(subject="Algoritmos e Estrutura de Dados")





if __name__ =="__main__":
    main()