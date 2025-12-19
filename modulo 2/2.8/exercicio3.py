def main():
 
 saldo_em_conta = 500.0
 def possui_saldo_para_saque(valor_saque):
    if saldo_em_conta >= valor_saque:
       return True
    else: 
       return False
 
 saque = 200
 print(possui_saldo_para_saque(saque))




if __name__ == "__main__":
    main()
