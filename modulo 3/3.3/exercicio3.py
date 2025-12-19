def main():
 import time

#Narrativa: O Mago Elétrico atinge um alvo e seu raio salta para um segundo alvo. Podemos simular esse dano em cadeia com recursão.
#Tarefa: Crie uma função dano_em_cadeia(dano, numero_de_saltos). Se numero_de_saltos for 0, a função termina. Caso contrário, ela imprime "Causando [dano] de dano a um alvo..." e chama a si mesma com o dano reduzido (ex: dano * 0.8) e numero_de_saltos - 1. Simule um ataque inicial de 100 de dano com 2 saltos.

 def dano_em_cadeia(dano, numero_de_saltos):
     
     while numero_de_saltos > 0 :
        print(f"causando {dano} de dano a um alvo...")
        dano = dano * 0.8
        numero_de_saltos = numero_de_saltos - 1
        time.sleep(0.5)

 dano_em_cadeia(100,100)


if __name__ == "__main__":
    main()