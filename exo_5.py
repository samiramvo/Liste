liste=['abc','aba','xyz','1221']

liste2=list(map(list,liste))

def ver(liste):
    som=0
    for i in liste:
     if len(i)>=2 and i[0]==i[-1]:
         som+=1
    return som
    

print(ver(liste2))

