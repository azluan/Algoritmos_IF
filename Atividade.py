agenda = []

def adicionar_compromisso():
    dt = input("Data (dd/mm/aaaa): ")
    hr = input("Hora (hh:mm): ")
    desc = input("Descrição: ")
    compromisso = {'data': dt, 'hora': hr, 'descricao': desc}
    agenda.append(compromisso)
    print("Compromisso adicionado.")

def visualizar_compromissos():
    if not agenda:
        print("Agenda vazia.")
    else:
        print("Compromissos:")
        for i, comp in enumerate(agenda, 1):
            print(f"Compromisso {i}")
            print("Data:", comp['data'])
            print("Hora:", comp['hora'])
            print("Descrição:", comp['descricao'])
            print("")

def editar_compromisso():
    if not agenda:
        print("Agenda vazia.")
        return
    
    visualizar_compromissos()
    indice = int(input("Digite o número do compromisso que deseja editar: "))
    if 1 <= indice <= len(agenda):
        comp = agenda[indice-1]
        nova_descricao = input("Digite a nova descrição: ")
        comp['descricao'] = nova_descricao
        print("Compromisso editado.")
    else:
        print("Índice inválido.")

def remover_compromisso():
    if not agenda:
        print("Agenda vazia.")
        return

    visualizar_compromissos()
    indice = int(input("Digite o número do compromisso que deseja remover: "))
    if 1 <= indice <= len(agenda):
        del agenda[indice-1]
        print("Compromisso removido.")
    else:
        print("Índice inválido.")

def main():
    while True:
        print("1. Adicionar compromisso")
        print("2. Visualizar compromissos")
        print("3. Editar compromisso")
        print("4. Remover compromisso")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            adicionar_compromisso()
        elif escolha == '2':
            visualizar_compromissos()
        elif escolha == '3':
            editar_compromisso()
        elif escolha == '4':
            remover_compromisso()
        elif escolha == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    main()
