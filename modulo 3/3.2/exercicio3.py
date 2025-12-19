def main():

#Narrativa: Uma função pode ser responsável por buscar e formatar os dados de uma tropa, e seu resultado pode ser passado diretamente para a função print().

#Tarefa: Crie uma função obter_status_tropa(nome_tropa, nivel) que retorna uma string formatada como "[nome_tropa] (Nível [nivel])". Chame a função print() passando como argumento uma chamada à sua função: print(obter_status_tropa("Cavaleiro", 9)).

 def obter_status_tropa (nome_tropa,nivel):
    Nivel = str(nivel)

    return  "[{nome_tropa}] ( Nivel [{Nivel}])"
 
 print(obter_status_tropa("Cavaleiro", 9))




if __name__ == "__main__":
    main()    