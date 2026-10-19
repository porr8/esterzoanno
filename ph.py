"""
scrivere un programma che data una lista di 20 valori di ph geenerati casualmente, crei un dizionario che abbia come chiave
acida, basica e neutrale e come valori il numero di occorrenze
"""
import random
listaph=[]
for i in range(0,20):
    listaph.append(random.randint(0,14))
ph={"acida":0, "basica":0, "neutrale":0}
basico=0
acido=0
neutro=0
print(len(listaph))
for i in range(0,20):
    if listaph[i]<7:
        acido=acido+1
    elif listaph[i]>7:
        basico=basico+1
    else:
        neutro=neutro+1
ph={"acida":acido, "basica":basico, "neutrale":neutro}
print(ph)


        
        