def main():
 
 from logica_batalha import verificar_vitoria

 print(verificar_vitoria(0)) 

if __name__ == "__main__":
    main()

#Narrativa: A lógica para determinar se uma batalha foi vencida (destruindo pelo menos uma torre) é uma regra de negócio que pode ser reutilizada em várias partes do jogo.
#Tarefa: Crie um arquivo chamado logica_batalha.py. Nele, defina uma função verificar_vitoria(torres_destruidas) que retorna True se torres_destruidas >= 1 e False caso contrário.
#Crie um segundo arquivo, simulador.py. Nele, importe a função do outro arquivo com a linha from logica_batalha import verificar_vitoria.
#No simulador.py, chame a função verificar_vitoria(2) e imprima o resultado.