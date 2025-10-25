# Importei as bibliotecas necessárias
from datetime import datetime
import os
import platform
import time

# Função para limpar o terminal (Windows e Linux/Mac)
def limpar_tela():
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")

tarefas = []
livros = []

while True:
    limpar_tela()  # Limpa sempre que volta ao menu principal
    print('╔════════════════════╗')
    print('║     Aplicativo     ║')
    print('╚════════════════════╝')
    print()
    print('1 - CALCULADORA\n2 - DATA E HORA\n3 - LISTA DE TAREFAS\n4 - SISTEMA DE GERENCIAMENTO - BIBLIOTECA\n5 - Sair')
    print()
    opção = int(input('Digite a opção desejada: '))
    
    limpar_tela()

    # ================= CALCULADORA =================
    if opção == 1:
        while True:
            limpar_tela()
            print('╔════════════════════╗')
            print('║ CALCULADORA BÁSICA ║')
            print('╚════════════════════╝')
            print('1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Sair')
            opção_calculadora = int(input('Digite a opção desejada: '))
            limpar_tela()

            if opção_calculadora == 1:
                numero1 = float(input('Digite o primeiro número: '))
                numero2 = float(input('Digite o segundo número: '))
                print(f'{numero1} + {numero2} = {numero1 + numero2:.2f}')
                
            elif opção_calculadora == 2:
                numero1 = float(input('Digite o primeiro número: '))
                numero2 = float(input('Digite o segundo número: '))
                print(f'{numero1} - {numero2} = {numero1 - numero2:.2f}')
                
            elif opção_calculadora == 3:
                numero1 = float(input('Digite o primeiro número: '))
                numero2 = float(input('Digite o segundo número: '))
                print(f'{numero1} * {numero2} = {numero1 * numero2:.2f}')
                
            elif opção_calculadora == 4:
                numero1 = float(input('Digite o primeiro número: '))
                numero2 = float(input('Digite o segundo número: '))
                if numero2 == 0:
                    print("Não é possível dividir por 0")
                else:
                    print(f'{numero1} / {numero2} = {numero1 / numero2:.2f}')
            elif opção_calculadora == 5:
                print('Saindo da calculadora...')
                time.sleep(1)
                break
            else:
                print('Digite uma opção válida!')

            input('\nPressione ENTER para continuar...')
            limpar_tela()
      
    # ================= DATA E HORA =================
    elif opção == 2:
        agora = datetime.now()
        formato_brasil = agora.strftime("%d/%m/%Y")
        formato_hora = agora.strftime("%H:%M:%S")
        print(f"Data: {formato_brasil}")
        print(f'Hora: {formato_hora}')
        input('\nPressione ENTER para voltar...')
        limpar_tela()
        
    # ================= LISTA DE TAREFAS =================
    elif opção == 3:
        while True:
            limpar_tela()
            print('╔════════════════════╗')
            print('║  LISTA DE TAREFAS  ║')
            print('╚════════════════════╝')
            print('1 - Criar tarefa\n2 - Listar tarefas\n3 - Atualizar tarefa\n4 - Excluir tarefa\n5 - Sair')
            opção = int(input('Digite o número da opção desejada: '))
            limpar_tela()
    
            if opção == 1: 
                tarefa = input('Digite a descrição da tarefa: ')
                tarefas.append(tarefa)
                print('Tarefa criada com sucesso!')
    
            elif opção == 2:
                if not tarefas:
                    print('Nenhuma tarefa cadastrada.')
                else:
                    for i, t in enumerate(tarefas, 1):
                        print(f'{i}. {t}')
                     
            elif opção == 3:
                if not tarefas:
                    print('Nenhuma tarefa cadastrada.')
                else:
                    for i, t in enumerate(tarefas, 1):
                        print(f'{i}. {t}')
                    atualizar = int(input('Digite o número da tarefa a atualizar: ')) - 1
                    if 0 <= atualizar < len(tarefas):
                        nova = input('Digite a nova descrição: ')
                        tarefas[atualizar] = nova
                        print('Tarefa atualizada com sucesso!')
                    else:
                        print('Número inválido!')
                        
            elif opção == 4:
                if not tarefas:
                    print('Nenhuma tarefa cadastrada.')
                else:
                    for i, t in enumerate(tarefas, 1):
                        print(f'{i}. {t}')
                    excluir = int(input('Digite o número da tarefa a excluir: ')) - 1
                    if 0 <= excluir < len(tarefas):
                        tarefas.pop(excluir)
                        print('Tarefa excluída!')
                    else:
                        print('Número inválido!')
                        
            elif opção == 5:
                print('Saindo da lista de tarefas...')
                time.sleep(1)
                break
            else:
                print('Opção inválida!')   
                
            input('\nPressione ENTER para continuar...')
            limpar_tela()
    
    # ================= BIBLIOTECA =================
    elif opção == 4:
        while True:
            limpar_tela()
            print("╔════════════════════════════════════════╗")
            print("║ SISTEMA DE GERENCIAMENTO - BIBLIOTECA  ║")
            print("╚════════════════════════════════════════╝")
            print("1. Cadastrar livro\n2. Listar livros\n3. Editar livro\n4. Excluir livro\n5. Sair")
            opcao = input("Digite a opção desejada: ")
            limpar_tela()
    
            if not opcao.isdigit():
                print("Opção inválida! Digite um número entre 1 e 5.")
                time.sleep(1.5)
                continue
            opcao = int(opcao)
    
            # 1. Cadastrar livro
            if opcao == 1:
                print("=== CADASTRAR NOVO LIVRO ===")
                titulo = input("Título: ")
                genero = input("Gênero: ")
                autor = input("Autor: ")
                data_publicacao = input("Data de Publicação: ")
                isbn = input("ISBN: ")
        
                novo_livro = [titulo, genero, autor, data_publicacao, isbn]
                if novo_livro in livros:
                    print("Este livro já está cadastrado!")
                else:
                    livros.append(novo_livro)
                    print("✓ Livro cadastrado com sucesso!")
            
            # 2. Listar livros
            elif opcao == 2:
                print("=== LIVROS CADASTRADOS ===")
                if not livros:
                    print("Nenhum livro cadastrado.")
                else:
                    for i, livro in enumerate(livros, 1):
                        print(f"\nLivro #{i}")
                        print(f"Título: {livro[0]}")
                        print(f"Gênero: {livro[1]}")
                        print(f"Autor: {livro[2]}")
                        print(f"Data: {livro[3]}")
                        print(f"ISBN: {livro[4]}")
                    print(f"\nTotal: {len(livros)} livros cadastrados")
            
            # 3. Editar livro
            elif opcao == 3:
                if not livros:
                    print("Nenhum livro cadastrado.")
                else:
                    for i, livro in enumerate(livros, 1):
                        print(f"{i}. {livro[0]}")
                    num = int(input("Número do livro para editar: ")) - 1
                    if 0 <= num < len(livros):
                        titulo = input(f"Novo título (Enter para manter '{livros[num][0]}'): ") or livros[num][0]
                        genero = input(f"Novo gênero (Enter para manter '{livros[num][1]}'): ") or livros[num][1]
                        autor = input(f"Novo autor (Enter para manter '{livros[num][2]}'): ") or livros[num][2]
                        data = input(f"Nova data (Enter para manter '{livros[num][3]}'): ") or livros[num][3]
                        isbn = input(f"Novo ISBN (Enter para manter '{livros[num][4]}'): ") or livros[num][4]
                        livros[num] = [titulo, genero, autor, data, isbn]
                        print("Livro atualizado com sucesso!")
                    else:
                        print("Número inválido!")
            
            # 4. Excluir livro
            elif opcao == 4:
                if not livros:
                    print("Nenhum livro cadastrado.")
                else:
                    for i, livro in enumerate(livros, 1):
                        print(f"{i}. {livro[0]}")
                    num = int(input("Número do livro para excluir: ")) - 1
                    if 0 <= num < len(livros):
                        confirm = input(f"Tem certeza que deseja excluir '{livros[num][0]}'? (S/N): ").upper()
                        if confirm == "S":
                            livros.pop(num)
                            print("Livro excluído!")
                        else:
                            print("Exclusão cancelada.")
                    else:
                        print("Número inválido!")
            
            elif opcao == 5:
                print("Saindo do sistema de biblioteca...")
                time.sleep(1)
                break

            else:
                print("Opção inválida!")
            
            input('\nPressione ENTER para continuar...')
            limpar_tela()
    
    elif opção == 5:
        print('Saindo do aplicativo. Até logo!')
        time.sleep(1)
        break

    else:
        print('Opção inválida! Por favor, escolha uma opção válida.')
        time.sleep(1)
        limpar_tela()
