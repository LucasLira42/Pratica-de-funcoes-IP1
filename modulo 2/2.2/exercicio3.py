def main():

    def juros_simples(valor, tempo, taxa):
        resultado = valor + (valor * tempo * taxa)
        return print(f"\ncom um valor inicial de {valor} o montante final será de {resultado}\n\n")
    
    juros_simples(1000, 5, 0.15)

    juros_simples(5000, 5, 0.15)




if __name__ == "__main__":
    main()