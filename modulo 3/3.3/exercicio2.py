def main():
 import time
#Narrativa: Uma contagem regressiva é um exemplo clássico de recursão. A cada passo, anunciamos o dia atual e iniciamos a contagem para o dia anterior.
#Tarefa: Crie uma função contagem_regressiva(dias). Se dias for 0, ela deve imprimir "Boas férias!". Caso contrário, ela imprime o número de dias e chama a si mesma com dias - 1. Inicie a contagem a partir de 5.

 def contagem_regressiva(dias):

    while dias > 0 :
        
        print(f"{dias}")
        dias = dias - 1
        time.sleep(1)
        

    return print("boas férias")
 
 contagem_regressiva(5)

    


if __name__ == "__main__":
    main()