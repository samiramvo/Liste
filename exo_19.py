liste=[1,3,8,3,0,4]
liste2=["Samira","Laure",4,8,3]

difference1=set(liste).difference(set(liste2))
difference2=set(liste2).difference(set(liste))

list_difference=difference1.union(difference2)
print(list_difference)