#Narrativa: Sua ferramenta de educação financeira precisa calcular o montante final de um investimento com juros simples. A fórmula é a mesma, mas o valor inicial varia.
#Tarefa: Considere uma taxa de juros de 15% ao ano (taxa = 0.15) e um período de 5 anos (tempo = 5). 
#Primeiro, calcule e imprima o montante para um valor_inicial de R$ 1000.00. 
#Em seguida, repita o bloco de cálculo e impressão para um valor_inicial de R$ 5000.00.


def main():

    def juros_simples(valor, tempo, taxa):
        resultado = valor + (valor * tempo * taxa)
        return print(f"\ncom um valor inicial de {valor} o montante final será de {resultado}\n\n")
    
    juros_simples(1000, 5, 0.15)

    juros_simples(5000, 5, 0.15)




if __name__ == "__main__":
    main()