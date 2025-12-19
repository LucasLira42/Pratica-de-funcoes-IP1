def main():
 
 elixir_atual = 7
 def verificar_elixir_suficiente(custo_carta):
    if elixir_atual >= custo_carta:
       return True
    else:
       return False
    
 Mago = 5
 Boolean = verificar_elixir_suficiente(Mago)
 print(Boolean)

if __name__ == "__main__":
    main()
