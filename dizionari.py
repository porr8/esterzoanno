#dizionari

diz={"enzimaA":12, "enzimaB":16, "enzimaC":2}

#accedere singolo elemento
print(diz["enzimaB"])

diz["enzimaC"]=2314

#scorrere dizionario

for key,value in diz.items():
    print(key)
    print(value)