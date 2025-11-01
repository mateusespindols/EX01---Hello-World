

from collection import deque

def main ():
    fila_prioritaria = deque()
    fila_geral = deque(



        while True:
            print("\n=== Fila Embarque Passageiros - Aeroporto ===")
            print("1 - Adicionar passageiro a fila")
            print("2 - Embarcar passageiro")
            print("3 - Mostrar filas")
            print("4 - Sair")



            opcao = input("Escolha uma opção: ")



            if opcao == 1 :
                nome = input("Nome passageiro: ")
                prioridade = input("O passageiro é prioritário? S/N").lower()
                if prioridade == "s":
                    fila_prioritaria.appened(nome)
                    print(f"{nome} foi adicionado à fila prioritária.")
                else:
                    fila_geral.appened(nome)
                    print(f"{nome} foi adicionado à fila geral.")    

            elif opcao == "2":
                if fila_prioritaria:
                embarcado = fila_prioritaria.popleft()
                print(f"Passageiro prioritário embarcado: {embarcado}")
                elif fila_geral:
                embarcado = fila_geral.popleft()
                    print(f"Passageiro embarcado: {embarcado}")
                else:  
                    print(f"Nenhum passageiro na fila de embarque!!")  
             elif opcao == "3":
                print("\n === FILA PRIORITARIA ===") 
                if fila_prioritaria:
                    for p in fila_prioritaria:
                        print(f"{p}")  
                else:
                    print("Vazia")        

                 print("\n === FILA GERAL ===") 
                if fila_geral:
                    for p in fila_geral:
                        print(f"{p}")  
                else:
                    print("Vazia")  

             elif opcao == "4":
                print("Encerrando o programa...") 
                break

             else:
                print("Opção Inválida. Tente novamente  ")        

if __name__==    "__main__":
    main()              

    )