# Classe principal para os cálculos

# Instanciando a classe

class Matriz():
    def __init__(self, linhas, colunas, matriz=list()):
        self.linhas = linhas
        self.colunas = colunas

        #Criando a Matriz
        if matriz == list():
            matriz = list()
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


