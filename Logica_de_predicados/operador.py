def tabelaVerdade(lista):
    linhas=2**len(lista)
    print(lista)
    list=[]
    for i in range(8):
        list2=[]  
        for j in range(3):
            list2.append('V')
        list.append(list2)
        print(list[i])


def separaLetraNominal(num):
    listaLetraNominal=[]
    for i in range(len(num)):
        if ord(num[i])>=65 and ord(num[i])<=90:
            if num[i] not in listaLetraNominal:
                listaLetraNominal.append(num[i])
    return listaLetraNominal
arara='~R,(PvQ),~P|-~P'
tabelaVerdade(separaLetraNominal(arara))
print(ord('~'))

print(ord('v'))

print(ord('^'))

print(ord('-'))

print(ord('|'))

print(ord(')'))

print(ord('('))

print(ord('>'))

print(ord('<'))
list=[]

for i in range(8):
    list2=[]  
    for j in range(3):
        list2.append('V')
    list.append(list2)
    print(list[i])