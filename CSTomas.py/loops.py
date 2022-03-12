# Exemplo: Calcular o quadrado de um inteiro
# da maneira mais difícil...
n=3
resposta = 0
iteradasQueFaltam = n
while (iteradasQueFaltam != 0):
    resposta = resposta + n
    iteradasQueFaltam = iteradasQueFaltam - 1
    while resposta == 6:
        print(str(n) + '*' + str(n) + ' = ' + str(resposta))