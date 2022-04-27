# Classe principal para os cálculos

# Instanciando a classe

class Matriz():
    def __init__(self, linhas, colunas, matriz=list()):
        self.linhas = linhas
        self.colunas = colunas

        # Criar a Matriz Principal
        if matriz == list():
            print(f"Definindo Matriz {self.linhas}x{self.colunas}:\n")
            for i in range(self.linhas):
                linha = list()
                for j in range(self.colunas):
                    item = int(input(f"Digite o valor do item [{i+1},{j+1}]: "))
                    linha.append(item)
                matriz.append(linha)
        self.matriz = matriz

    # Exibir a Matriz
    def Mostrar(self):
        print("Sua matriz é: \n")
        for l in range(self.linhas):
            print(self.matriz[l])

    # Somar duas matrizes
    def Soma(self):
        # Definir a matriz a ser somada
        s = Matriz(self.linhas, self.colunas, matriz=list())
        matrizSoma = list()
        for i in range(s.linhas):
            linha = list()
            for j in range(s.colunas):
                item = self.matriz[i][j] + s.matriz[i][j]
                linha.append(item)
            matrizSoma.append(linha)
        Soma = Matriz(self.linhas, self.colunas, matriz = matrizSoma)
        print("O resultado da soma entre essas duas matrizes é: ")
        Matriz.Mostrar(Soma)
        return matrizSoma

    # Subtrair duas matrizes
    def Subtrair(self):
        # Definir a matriz a ser subtraída
        s = Matriz(self.linhas, self.colunas, matriz=list())
        matrizSub = list()
        for i in range(s.linhas):
            linha = list()
            for j in range(s.colunas):
                item = self.matriz[i][j] - s.matriz[i][j]
                linha.append(item)
            matrizSub.append(linha)
        Sub = Matriz(self.linhas, self.colunas, matriz = matrizSub)
        print("O resultado da subtração entre essas duas matrizes é: ")
        Matriz.Mostrar(Sub)
        return matrizSub

    # Multiplicar duas matrizes
    def Multiplicar(self):
        # Definir a matriz a ser multiplicada 
        colunas = int(input("Digite a quantidade de colunas da matriz que multiplicará: "))
        m = Matriz(self.colunas, colunas, matriz=list())
        matrizMult = list()
        for i1 in range(self.linhas):
            linha = list()
            for j1 in range(self.colunas):
                s = 0
                for j2 in range(m.colunas):
                    s += self.matriz[i1][j2] * m.matriz[j2][j1]
                linha.append(s)
            matrizMult.append(linha)
        Mult = Matriz(self.linhas, colunas, matriz = matrizMult)
        print("O resultado da subtração entre essas duas matrizes é: ")
        Matriz.Mostrar(Mult)
        return matrizMult