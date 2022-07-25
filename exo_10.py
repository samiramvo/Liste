def trouver(str,n):
    liste1=[]
    liste=str.split("")
    for mot in liste:
        if len(mot)>n:
            liste1.append(mot)
    return liste1

print(trouver("La vie est belle",3))