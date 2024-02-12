import os
import main

Fichier = open("texte.txt","rb")
contenu = Fichier.read().decode("utf-8")
print(contenu)
Fichier.close()

print(f"\nTaille du texte : {len(contenu)} caractères\n")

#---------------#------------------------------------

file = open("nouveau.txt", "w", encoding = 'utf-8') 

contenu, codes_huffman = main.encoder_huffman(contenu)

print(contenu)
print(codes_huffman)

file.write(contenu)
file.close()

file = open("nouveau.txt", "rb") 
content2 = file.read().decode("utf-8")
file.close()

print(f"{content2}\n")
print(main.decoder_huffman(content2, codes_huffman))



