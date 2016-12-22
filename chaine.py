phrase=input("entrez votre phrase\n")
l=[]
mot=''
for car in phrase:
        if car!=" ":
           mot=mot+car
        else:
            l.append(mot)
            mot=''
l.append(mot)
mt=len(l)-1
while mt>-1:
        print(l[mt])
        mt=mt-1

