"""Dati due punti su un piano cartesiano, calcolare la distanza e verificare se
i punti sono sull'asse delle ascisse o su quello dell'ordinate o in quale
quadrante esistono.
I punti sono generati in maniera randomica interi.
Salvare su un file di testo i punti generati, il valore della distanza e
i responsi dei controlli"""
import random

def controlloQuadrante(punto_generico):
    if punto_generico[0]>0 and punto_generico[1]>0:
        print("Il primo punto è sul primo quadrante.")
    elif punto_generico[0]<0 and punto_generico[1]>0:
        print("Il primo punto è sul secondo quadrante.")
    elif punto_generico[0]<0 and punto_generico[1]<0:
        print("Il primo numero è sul terzo quadrante.")
    else:
        print("Il primo numero è sul quarto quadrante.")


if __name__=="__main__":
    puntoUno=[]
    puntoDue=[]
for i in range(0,2):
    puntoUno.append(random.randint(-20,20))
    puntoDue.append(random.randint(-20,20))

controlloQuadrante(puntoUno)
controlloQuadrante(puntoDue)