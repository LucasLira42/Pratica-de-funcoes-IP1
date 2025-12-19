def main():

 #Narrativa: Vamos otimizar o processo de cálculo de média, lendo as notas do usuário e calculando a média em uma única linha de comando.
 #Tarefa: Crie uma função calcular_media(n1, n2) que retorna a média de dois números. Em seguida, chame essa função em uma única linha, usando o retorno de int(input()) diretamente como argumentos: media_final = calcular_media(int(input("Nota 1: ")), int(input("Nota 2: "))). Imprima o resultado

 def calcuclar_media(n1,n2):
    media = (n1 + n2)/2
    print(f"a média é {media}")
    return media 
 
 media_final = calcuclar_media(int(input("nota 1:")),int(input("nota 2:")))
  

    

if __name__ == "__main__":
    main()
