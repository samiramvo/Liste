liste=['Red','Green','white','Black','Pink','Yellow']
liste=[x for (i,x) in enumerate(liste)if not i in (0,4,5)]
print(liste)