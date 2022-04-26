# Classe principal para os cálculos

# Instanciando a classe

class Matriz():
    def __init__(self, linhas, colunas, matriz=list()):
        self.linhas = linhas
        self.colunas = colunas

        #Criando a Matriz
        if matriz == list():
            for i in range(0, self.linhas):
                linha = list()
                for j in range(0, self.colunas):
                    item = int(input(f"Digite o valor do item [{i+1},{j+1}]: "))
                    linha.append(item)
                matriz.append(linha)
        self.matriz = matriz

    # Exibir a Matriz
    def Mostrar(self):
        print("Sua matriz é: \n")
        for l in range(0, self.linhas):
            print(self.matriz[l])

    #Somar duas matrizes
    def Soma(self):
        #Definindo a matriz a ser somada
        s = Matriz(self.linhas, self.colunas, matriz=list())
        matrizSoma = list
        for i in range(0, s.linhas):
            linha = list()
            for j in range(0, s.colunas):
                item = self.matriz[i][j] + s.matriz[i][j]
                linha.append(item)
            matrizSoma.append(linha)
        Soma = Matriz(self.linhas, self.colunas, matriz = matrizSoma)
        print("O resultado da soma entre essas duas matrizes é: ")
        Matriz.Mostrar(Soma)

    #Subtrair duas matrizes
    def Subtrair(self):
        s = Matriz(self.linhas, self.colunas, matriz=list())
        matrizSoma = list
        for i in range(0, s.linhas):
            linha = list()
            for j in range(0, s.colunas):
                item = self.matriz[i][j] - s.matriz[i][j]
                linha.append(item)
            matrizSoma.append(linha)
        Soma = Matriz(self.linhas, self.colunas, matriz = matrizSoma)
        print("O resultado da subtração entre essas duas matrizes é: ")
        Matriz.Mostrar(Soma)
