# periodo intervalo
vezes = int(input())
dicionario = {
    'superior':0,
    'esquerda':0,
    'centro':0,
    'direita':0,
    'inferior':0
}
for i in range(vezes):
    for i in range(1,7):
        entrada = input().split(' ')

        if i == 1:
            dicionario['superior']+=entrada.count('1')
        elif i==6:
            dicionario['inferior']+=entrada.count('1')
        else:
            if entrada[0] == '1':
                dicionario['esquerda']+=1
            if entrada[1]=='1':
                dicionario['centro']+=1
            if entrada[2]=='1':
                dicionario['direita']+=1
retornar = ''

#sério, preciso urgente aprender o argumento key da funcao sorted ou aprender 'itemgetter'
for chave in dicionario:
    contador=0
    for another_chave in dicionario:
        if dicionario[chave] > dicionario[another_chave]:
            contador+=1
    if contador == 4:
        retornar = chave
        break
print(retornar)