"""
stampare lo stato di aggregazione dell'acqua data la sua temperatura in input

"""
temperatura=input("inserisci la temperatura ")
temperatura=float(temperatura)
if temperatura<=0:
    print("solido")
elif temperatura>=100:
    print("gassoso")
else:
    print("liquido")
