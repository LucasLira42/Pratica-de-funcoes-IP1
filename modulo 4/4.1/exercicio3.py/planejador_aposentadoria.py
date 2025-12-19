
def main():
 from ferramentas_financeiras import calcular_juros_compostos

 print(calcular_juros_compostos(5000,0.07,20))

if __name__ == "__main__":
    main()  

#Narrativa: A fórmula para calcular juros compostos é uma ferramenta financeira essencial que pode ser usada em diferentes contextos (planejamento de aposentadoria, projeção de investimentos, etc.).
#Tarefa:Crie o arquivo ferramentas_financeiras.py. Nele, defina a função calcular_juros_compostos(principal, taxa_anual, anos) que retorna o montante final.
#Crie o arquivo planejador_aposentadoria.py. Importe a função. No planejador_aposentadoria.py, use a função para calcular o montante de um investimento de R$ 5000 a uma taxa de 7% ao ano por 20 anos e imprima o resultado.