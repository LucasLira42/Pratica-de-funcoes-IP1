def main():

 meu_investimento = 500.0
 def analisar_potencial(valor):
    taxa_rendimento_diaria = 0.005
    print(f"{valor} {taxa_rendimento_diaria}")
 
 analisar_potencial(meu_investimento)
 print(taxa_rendimento_diaria)


if __name__ == "__main__":
    main()

#Narrativa: Ao calcular o potencial de um investimento, uma função pode usar uma variável para a taxa de risco do dia, que não precisa ser armazenada permanentemente.
#Tarefa: Crie uma variável meu_investimento = 500.0. Crie uma função analisar_potencial(valor). Dentro da função, crie taxa_rendimento_diaria = 0.005 e imprima o valor e a taxa_rendimento_diaria. Chame a função com meu_investimento. Fora da função, tente acessar taxa_rendimento_diaria e observe o erro.
