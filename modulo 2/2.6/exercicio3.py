def main():
 def adicionar_transacao(descricao, valor):
    print(f"Transação registrada: {descricao} - Valor: R$ {valor}")

 adicionar_transacao("feira supermercado",250.75)



if __name__ == "__main__":
    main()

#Narrativa: Um aplicativo de controle financeiro precisa registrar transações, que consistem em uma descrição e um valor.
#Tarefa: Crie uma função adicionar_transacao(descricao, valor). A função deve imprimir "Transação registrada: {descricao} - Valor: R$ {valor}". Chame a função para registrar uma compra de uma feira no supermercado no valor de 250.75.