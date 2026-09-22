"""
scrivi un programma che:

chieda all'utente la distanza percorsa in km e il tempo impiegato in ore.
calcola la velocità media.
stampa il risultato con due cifre decimali e indica l'unità di misura.

"""

distanza=input("inserisci la distanza in km")
distanza=float(distanza)
tempo=input("inserisci il tempo impiegato in ore")
tempo=int(tempo)
velocita=distanza/tempo
velocita=round(velocita,2)
print(velocita)