def main():

#Narrativa: Podemos simular o crescimento de um investimento ano a ano usando recursão. A cada ano, calculamos o novo saldo e então repetimos o processo para os anos restantes.
#Tarefa: Crie uma função calcular_saldo_recursivo(saldo, taxa, anos_restantes). O caso base é quando anos_restantes for 0, retornando o saldo. Caso contrário, a função deve chamar a si mesma com o novo saldo (saldo * (1 + taxa)) e com anos_restantes - 1. Teste a função para um saldo inicial de R$ 1000, taxa de 10% e 3 anos.

 def calcular_saldo_recursivo(saldo,taxa,anos_restantes):

    while anos_restantes > 0 :
       novo_saldo = (saldo * (1+taxa))
       saldo = novo_saldo
       anos_restantes = anos_restantes - 1

    return novo_saldo   
 
 print(calcular_saldo_recursivo(1000,0.010,3))
 


if __name__ == "__main__":
    main ()