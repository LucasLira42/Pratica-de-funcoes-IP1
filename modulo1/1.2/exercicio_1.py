#Narrativa: O sistema de áudio do Clash Royale precisa anunciar qual tropa específica foi posicionada na arena. A estrutura da mensagem é sempre a mesma, mudando apenas o nome da tropa.
#Tarefa: Primeiro, escreva o código para anunciar a entrada de um "Gigante". Cria a variável tropa = “Gigante” e imprima a mensagem deve ser: f"A tropa {tropa} entrou na batalha! Prepare sua defesa!". Em seguida, no mesmo script, escreva o código para anunciar a entrada de uma "P.E.K.K.A.", ou seja tropa = “P.E.K.K.A.”, com a mensagem: "A tropa {tropa}. entrou na batalha! Prepare sua defesa!"


def main():

    tropa1 = "Gigante"
    tropa2 = "P.E.K.K.A."

    def anunciodetropa (name):
        print(f"A tropa {name} entrou na batalha! Prepare sua defesa!\n\n")

    anunciodetropa(tropa1)
    anunciodetropa(tropa2)
    



if __name__ == "__main__":
    main()