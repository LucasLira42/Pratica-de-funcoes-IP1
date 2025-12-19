def main():


  def calcular_jcompostos(principal,taxa,anos):
    patrimonio_futuro = principal * ((taxa + 1)**anos)
    print(f"O montante final da aplicação é de R${patrimonio_futuro}")
    return patrimonio_futuro
  
  patrimonio_futuro = calcular_jcompostos(1000,0.08,10)

  print(f"{patrimonio_futuro}") 

    

  



if __name__ == "__main__":
    main()
