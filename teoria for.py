#creare una lista vuota
listauno=[]
#creareuna lista con elementi
listadue=[1,2,3,4]
#aggiungere un elemento alla lista (in coda)
listauno.append(4)
#visualizzare lunghezza della stringa
print(len(listauno))
#visualizzare gli elementi di una lista
print(listadue[0])
print(listadue[1])
print(listadue[2])
print(listadue[3])


for i in range(0,4):
    print(listadue[i])

#scorrimento della lista con uso di iteratore 
for element in listadue:
    pint(element)

#generazione di un numero casuale intero
numeroc= random.randint(1,10)

#creazione di una lista con 10 elementi randomici
listarandom=[]
for i in range(0,10):
    listarandom.append(random.randint(1,10))

#creazione di una lista con 10 elementi randomici usando ciclo while
listarandomdue=[]
i=0
while(i<10):
    listarandomdue.append(random.randint(1,10))
    i=i+1
