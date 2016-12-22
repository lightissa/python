#!/usr/local/bin/python3

# demande de la cle de chiffrement
cle=input('entrer la cle de chiffrement\n')
# lecture du message en clair
fichier=open('message.txt','r')
texteclair=fichier.read()
fichier.close()
textechiffre=' '
for i in range (0,len(texteclair)):
    if 97<= ord(texteclair[i])<=122:
           caractere=texteclair[i]
           code=ord(caractere)-97
           decalage=ord(cle[i%len(cle)])-97
           codechiffre=(code+decalage)%26
           caracterechiffre=chr(codechiffre+97)
           textechiffre=textechiffre+caracterechiffre
    else:
           textechiffre=textechiffre+' '
# ecriture dans le fichier message.txt
fichier=open('messagechiffre.txt','w')
fichier.write(textechiffre)
fichier.close()

