def main():
 
 def calcular_jcompostos(principal,taxa_anual,anos):
    montante = principal * ((taxa_anual + 1)**anos)
    print(f"O montante final da aplicação é de R${montante}")

 calcular_jcompostos(1000,0.08,10)

if __name__ == "__main__":
    main()
