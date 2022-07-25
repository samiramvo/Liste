liste=[(2,5),(1,2),(4,4),(2,3)]


def end(liste):
    return liste[-1]

def sort_list (tuple1):
    return sorted(tuple1,key=end)


print(sort_list(liste))