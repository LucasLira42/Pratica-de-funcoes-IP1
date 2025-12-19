#Narrativa: Em uma função que verifica se uma carta pode ser usada em um torneio, uma variável temporária calcula o nível efetivo da carta para aquele torneio, mas essa informação só é relevante dentro da verificação.
#Tarefa: Fora da função, crie uma variável nivel_global_arqueira = 9. Crie uma função verificar_nivel_torneio(nivel_carta). Dentro da função, crie uma variável nivel_maximo_torneio = 7. Imprima o nivel_carta e o nivel_maximo_torneio. Após chamar a função, tente imprimir a variável nivel_maximo_torneio fora da função e observe o NameError.

def main():

 nivel_global_arqueira = 9
 def verificar_nivel_torneio(nivel_carta):
    nivel_maximo_torneio = 7
    print(f"o nivel da cara é {nivel_carta} e o nivel máximo do torneiro é {nivel_maximo_torneio}")
    
 print(f"{nivel_maximo_torneio}")

if __name__ == "__main__":
    main()