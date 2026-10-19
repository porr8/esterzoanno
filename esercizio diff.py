"""
Crea una lista di tuple con i coefficienti (a, b, c) di almeno cinque equazioni, ad esempio [(1, -3, 2), (1, 2, 1), (2, 1, 3), ...].
Per ogni equazione calcola il discriminante e salvalo in una variabile.
Con un costrutto condizionale stabilisci se l'equazione ha due soluzioni reali distinte, due coincidenti o nessuna soluzione reale. Calcola le soluzioni quando esistono.
Per ogni equazione costruisci un dizionario con le chiavi "a", "b", "c", "delta", "tipo" e "soluzioni", e aggiungilo a una lista di risultati.
Scrivi su un file equazioni.txt una riga per equazione con i dati principali e l'esito.
Rileggi il file e stampa a schermo il suo contenuto, indicando alla fine quante equazioni hanno due soluzioni distinte.
"""
import math
lista=[]
coefficienti=[(1, -3, 2), (1, 2, 1), (2, 1, 3)]
prima=coefficienti[0]
a=prima[0]
b=prima[1]
c=prima[2]
discriminante=b^2-4*a*c
if discriminante>0:
    x1=-b+math.sqrt(discriminante)/(2*a)
    x2=-b-math.sqrt(discriminante)/(2*a)
    tipo="due soluzioni reali"
    soluzioni={"a":a,"b":b,"c":c,"discriminante":discriminante,"tipo":tipo,"soluzioni":str(x1)+" "+str(x2)}
elif discriminante==0:
    x1=-b+math.sqrt(discriminante)/(2*a)
    tipo="una soluzione reale"
    soluzioni={"a":a,"b":b,"c":c,"discriminante":discriminante,"tipo":tipo,"soluzioni":str(x1)}
else:
    tipo="non ha soluzioni reali"
    soluzioni={"a":a,"b":b,"c":c,"discriminante":discriminante,"tipo":tipo,"soluzioni":"non ha soluzioni reali"}

lista.append(soluzioni)


