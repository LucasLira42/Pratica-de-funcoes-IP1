

def main():

 from feiticos import lancar_bola_de_fogo
 from logica import calcular_dano_torre
 from tropas import posicionar_tropa


 print(posicionar_tropa("galinhapintadinha",5,18) ) 

 print(lancar_bola_de_fogo(10,7))

 print( calcular_dano_torre(4200,800))



if __name__ == "__main__":
    main()