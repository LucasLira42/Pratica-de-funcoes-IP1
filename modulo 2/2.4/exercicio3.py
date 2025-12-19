def main():
 saldo_conta= 1000
 def simular_bonus(saldo):
    saldo = saldo + 200
    print(f"{saldo}")
 
 simular_bonus(saldo_conta)
 print(saldo_conta)

if __name__ == "__main__":
    main()