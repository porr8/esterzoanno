"""
data una lista[1,2,2,4,5,8,9], calcolare e stampare a video la media
"""
lista=[1,2,2,4,5,8,9]
somma=0
for i in range(0,7):
    somma=somma+lista[i]
media=somma/len(lista)
print(media)