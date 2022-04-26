# Interface de interações com o projeto Matrizes

from Matrizes import Matriz as mt

try:
    linhas = int(input("Digite a quantidade de linhas da matriz principal: "))
    colunas = int(input("Digite a quantidade de colunas da matriz principal: "))
    principal = mt(linhas, colunas, matriz = list())
except:
    print("Caracter inválido!")
testeRapido = 1
if testeRapido == 0:
    while True:
        print("""[0] Modificar a Matriz Principal
[1] Mostrar a Matriz Principal
[2] Somar Duas Matrizes
[3] Subtrair Duas Matrizes
[4] Multiplicar Duas Matrizes
[5] Matriz Transposta
[6] Determinante
[7] Matriz Inversa
[8] Finalizar o programa
""")
        try:
            opcao = int(input("Digite o número equivalente à sua opção: "))
            if opcao > 8:
                break
        except:
            print("Caracter inválido! Encerrando o programa")
            break
        if opcao == 0:
            try:
                linhas = int(input("Digite a quantidade de linhas da matriz principal: "))
                colunas = int(input("Digite a quantidade de colunas da matriz principal: "))
                principal = mt(linhas, colunas, matriz = list())
            except:
                print("Caracter inválido!")
        elif opcao == 1:
            mt.Mostrar(principal)
        elif opcao == 2:
            resposta = mt.Somar(principal)
        elif opcao == 3:
            resposta = mt.Subtrair(principal)
        elif opcao == 4:
            pass
        elif opcao == 5:
            pass
        elif opcao == 6:
            pass
        elif opcao == 7:
            pass
        elif opcao == 8:
            pass
        mudar = str(input("Deseja convertê-la para Matriz Principal [S/N]? "))
        if mudar in "Ss":
            principal = mt(len(resposta), len(resposta[0]), matriz = resposta)
else:
    pass
