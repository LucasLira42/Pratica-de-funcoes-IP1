def main():

 from receitas import adicionar_salario
 from despesas import pagar_conta
 from investimentos import investir_poupanca
  
 saldo = 500

 print(investir_poupanca(pagar_conta( adicionar_salario(saldo,3000),800),1000))
  

if __name__ == "__main__":
    main()        
