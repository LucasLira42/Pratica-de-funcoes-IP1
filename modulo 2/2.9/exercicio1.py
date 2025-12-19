def main():

 def calcular_dano_liquido(dano_base,bonus,resistencia):
    return dano_base + bonus - resistencia
 
 ataque = calcular_dano_liquido(100,20,30)
 print(ataque)


if __name__ == "__main__":
    main()