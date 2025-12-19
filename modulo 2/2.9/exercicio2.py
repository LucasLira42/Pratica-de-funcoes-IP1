def main():

 def calcular_media_ponderada(nota1, peso1, nota2, peso2, nota3, peso3):
    return  ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / (peso1 + peso2 + peso3)

 print(calcular_media_ponderada(5,1,7,2,10,0.5))


if __name__ == "__main__":
    main()