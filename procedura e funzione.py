"""
scrivere un programma che dati due numeri generati casualmente nell'intervallo 10,30
conri e stampi a video il maggiore dei due, controlli se il maggiore è sotto la soglia
di 25
"""
import random


#procedura
def numeromaggiore(uno,due):
    if uno>due:
        print(uno)
    else:
        print(due)
        

#funzione
def numeromaggioreFunzione(uno,due):
    if uno>due:
        return(uno)
    else:
        return(due)
    

if __name__=="__main__":
    numerouno=random.randint(10,30)
    numerodue=random.randint(10,30)
    numeromaggiore(numerouno,numerodue)
    
    maggiore = numeromaggioreFunzione(numerouno,numerodue)
    print(maggiore)
    if maggiore<25:
        print("sotto soglia")
        
#in questo caso uno e due vengono passati per VALORE, cioè viene fatta una copia di numerouno e di numerodue,
#vengono messe dentro la funzione e nominati uno e due ma qualsiasi modifica a uno e due
#quando muore la funzione non modifica numerouno e numerodue