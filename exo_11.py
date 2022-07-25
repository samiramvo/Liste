def liste_two(liste1,liste2):
    for x in liste1:
        for y in liste2:
            if x==y:

               return True
    return False
    
print(liste_two([1,2,3],[3,7,8]))
print(liste_two(["Sami",1,8],[3,0,6]))