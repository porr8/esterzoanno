#tupla
mytuple=(3,6,8)
#stampare primo elemento della tupla
print(mytuple[0])
#stampare tutti gli elementi della tupla
for i in range (0,len(mytuple)):
    print(mytuple[i])
#modificare elemento della tupla
#mytuple[0]=2
#assegnamento non permesso
mytuple_list=list(mytuple)
mytuple_list[0]=2
mytuple=tuple(mytuple_list)