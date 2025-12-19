def obter_dados_usuario():
   principal = float(input("Digite aqui o capital inicial: "))
   taxa = float(input("digite aqui a taxa em anos: "))
   anos = int(input("digite quantos anos a aplicação ficará rendendo: "))
   
   return principal, taxa, anos

def calcular_projecao(p,t,a):
    M = p * (( t + 1) ** a)
    return M

def exibir_resultado(M):
    print(f"O resultado do montante é R${M}")
    
     

def main():

 exibir_resultado(calcular_projecao(*obter_dados_usuario()))



if __name__ == "__main__":
    main()











#Narrativa: Vamos criar uma ferramenta de linha de comando que pede ao usuário dados sobre um investimento, calcula a projeção e exibe o resultado, tudo de forma estruturada.
#Tarefa:Crie o arquivo simulador_investimento.py.Defina três funções: obter_dados_usuario() (que usa input para pedir principal, taxa e anos, e retorna esses valores), calcular_projecao(p, t, a) (que retorna o montante) e exibir_resultado(montante).
#Crie uma função main() que orquestra o fluxo: chama obter_dados_usuario, passa os resultados para calcular_projecao e, por fim, passa o resultado desta para exibir_resultado. Adicione o bloco if __name__ == "__main__": para executar main().