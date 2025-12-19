def main():

 despesas_mensais = ["Aluguel", "Internet"]
 def adicionar_gasto_extra(lista_de_despesas, gasto):
    lista_de_despesas.append(gasto)
    
 adicionar_gasto_extra(despesas_mensais,"conserto do carro")
 print(despesas_mensais)


if __name__ == "__main__":
    main()