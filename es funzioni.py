"""
scrivere un programma che dati due numeri interi
random calcoli la somma utilizzando funzioni
"""
import random

def sommaNumeri (uno,due):
    somma=uno+due
    print(somma)

if __name__=="__main__":
    numeroUno=random.randint(0,20)
    numeroDue=random.randint(0,20)
    
    #somma=numeroUno+numeroDue
    #print(somma)
    sommaNumeri(numeroUno,numeroDue)
    
    numeroTre=random.randint(0,20)
    numeroQuattro=random.randint(0,20)
    
    sommaNumeri(numeroTre,numeroQuattro)
    
    
   