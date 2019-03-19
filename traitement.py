import matplotlib.pyplot as plt
import numpy as np
import re
import sys

fichier = sys.argv[1]

def jour(txt):
    return txt[:6]+txt[8:10]
file = open(fichier)
lines = file.readlines()
nbMessage=[0]
jours =[jour(lines[0])]
mem=jour(lines[0])
for line in lines:
    if(re.match(r"[0,1,2,3,4,5,6,7,8,9]{2}/[0,1,2,3,4,5,6,7,8,9]{2}/[0,1,2,3,4,5,6,7,8,9]{4}",line)):
        if(mem == jour(line)):
            nbMessage[len(nbMessage)-1]+=1
        else:
            jours.append(jour(line))
            nbMessage.append(1)
        mem=jour(line)

xplacement = []
xlabel=[]
for x in range(len(jours)):
    if(x%50==0):
        xplacement.append(x)
        xlabel.append(jours[x])

def dataToMoy(nbPoint,donnees):
    dataTmp=[]
    moitier = int(nbPoint/2)
    for k in range(0,len(donnees)):
        if(k< moitier):
            dataTmp.append(np.mean(donnees[k:k+moitier]))
        elif(k > len(donnees)-moitier):
            dataTmp.append(np.mean(donnees[k-moitier:k]))
        else:
            dataTmp.append(np.mean(donnees[k-moitier:k+moitier]))
    return dataTmp

"""
#Sans filtrage
plt.title("Nombre de messages par jours sur la conversation")
plt.xlabel("Date")
plt.ylabel("Nombre de messages")
plt.xticks( xplacement, xlabel )
plt.plot(nbMessage)
plt.show()
"""

#avec filtrage
newNbMessage = dataToMoy(20,nbMessage)

plt.title("Nombre de messages par jours sur la conversation")
plt.xlabel("Date")
plt.ylabel("Nombre de messages")
plt.xticks( xplacement, xlabel )
plt.plot(newNbMessage)
plt.show()
