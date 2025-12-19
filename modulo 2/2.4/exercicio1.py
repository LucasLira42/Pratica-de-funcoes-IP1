
def main():

 dano_golem = 300
 def simular_efeito_furia(dano_tropa):
    dano_tropa = dano_tropa * 1.4
    print(f"{dano_tropa} ")

 simular_efeito_furia(dano_golem)
 print(dano_golem)


if __name__ == "__main__":
    main()

#Narrativa: O feitiço de Fúria no Clash Royale aumenta o dano de uma tropa temporariamente. Precisamos de uma função que simule esse efeito sem alterar o dano base permanente da tropa.
#Tarefa: Crie uma variável dano_golem = 300. Crie uma função simular_efeito_furia(dano_tropa). Dentro da função, reatribua o valor do parâmetro: dano_tropa = dano_tropa * 1.4. Imprima o valor de dano_tropa dentro da função. Depois de chamar simular_efeito_furia(dano_golem), imprima a variável original dano_golem e veja que seu valor não mudou.