def sublist(lst1,lst2):
    lst1=[elmnt for elmnt in lst1 if elmnt in lst2]
    lst2=[elmnt for elmnt in lst2 if elmnt in lst1]
    return lst1==lst2

print(sublist([1,2,3],[4,8,7,1,2,3]))
print(sublist([1,2],[7,0]))
