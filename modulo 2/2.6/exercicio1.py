def main ():

 class character:
    def __init__(self,life,attack):
       self.life = life
       self.attack = attack


 golem = character(4200,300)
 arqueiro = character(2000,600)


 def calcular_dano(attack_made,vida_alvo):
    vida_alvo = vida_alvo - attack_made 

    print(f"a vida restante é {vida_alvo}")

 calcular_dano(arqueiro.attack,golem.life)

 calcular_dano(arqueiro.attack,golem.life)
 
 calcular_dano(arqueiro.attack,golem.life)


 
if __name__ == "__main__":
    main() 