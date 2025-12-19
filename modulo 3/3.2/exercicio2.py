def main():

#Narrativa: Em um sistema de investimentos, primeiro calculamos o rendimento total e, em seguida, aplicamos uma taxa de imposto sobre esse rendimento. Isso pode ser feito de forma encadeada.
#Tarefa: Crie duas funções: calcular_rendimento_bruto(principal, taxa) e calcular_imposto(valor_bruto, aliquota). Chame as funções em uma única linha para obter o imposto final: 

 def calcular_rendimento_bruto(principal,taxa,anos):
    valor_bruto = principal * ((taxa + 1)**anos)
    return valor_bruto


 def calcular_imposto(valor_bruto,aliquota):
    imposto = valor_bruto * aliquota
    return imposto


 imposto_devido = calcular_imposto(calcular_rendimento_bruto(1000, 0.1,1), 0.15)
 print(f"{imposto_devido}")
  #adicionei o tempo pois creio que deveria para funcionar perfeitamente.

if __name__ == "__main__":
  main()