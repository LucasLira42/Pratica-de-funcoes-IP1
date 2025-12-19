def main():
 status_aluno = "cursando"

 def verificar_mudanca_status(status_atual):
    status_atual = "trancado" 
    print(f"{status_atual}")

 verificar_mudanca_status(status_aluno)
 print(status_aluno)

if __name__ == "__main__":
    main()

#Narrativa: O sistema acadêmico precisa de uma função para verificar o que aconteceria se um aluno mudasse seu status de "Cursando" para "Trancado", mas sem efetivar a mudança.
#Tarefa: Crie a variável status_aluno = "Cursando". Defina uma função verificar_mudanca_status(status_atual). Dentro dela, mude o valor: status_atual = "Trancado", e imprima o novo valor. Fora da função, após a chamada, imprima a variável original status_aluno para confirmar que ela permanece "Cursando".