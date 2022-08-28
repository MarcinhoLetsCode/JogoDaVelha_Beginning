#Jogo da Velha
tabela = []
print("Exemplo: ")
for Y in range(0,3,1):
    linha = []
    #print(linha)
    for X in range(0,3,1):
        linha.append(str(Y) + str(X))
    tabela.append(linha[:])
print(tabela[0][0],tabela[0][1],tabela[0][2])
print(tabela[1][0],tabela[1][1],tabela[1][2])
print(tabela[2][0],tabela[2][1],tabela[2][2])
print("")
tabela = []
print("Agora ta valendo: ")
for Y in range(0,3,1):
    linha = []
    #print(linha)
    for X in range(0,3,1):
        linha.append("#")
        #print(Y,",", X)
    tabela.append(linha[:])
print("Escolha O ou X")
print(tabela[0][0],tabela[0][1],tabela[0][2])
print(tabela[1][0],tabela[1][1],tabela[1][2])
print(tabela[2][0],tabela[2][1],tabela[2][2])
for C in range(0,9,1):
    while linha != "O" and linha != "X":
        linha = input().upper()
    print("Escolha Linha:")
    Y = int(input())
    print("Escolha Coluna:")
    X = int(input())
    while tabela[Y][X] == "O" or tabela[Y][X] == "X":
        print("Já Selecionado")
        print("Escolha Linha:")
        Y = int(input())
        print("Escolha Coluna:")
        X = int(input())
    tabela[Y][X] = linha
    if linha == "X":
        linha = "O"
    else:
        linha = "X"
        print("")
    print("É a Vez de", linha)
    print(tabela[0][0],tabela[0][1],tabela[0][2])
    print(tabela[1][0],tabela[1][1],tabela[1][2])
    print(tabela[2][0],tabela[2][1],tabela[2][2])
print("Verifique o Ganhador!")   
