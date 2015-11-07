# Instructions composees <while> - <if> - <elif> - <else>
 
print("Choisissez un nombre de 1 à 3 (ou 0 pour terminer) ", end =' ')
ch = input("numero : ")
a = int(ch)	   # conversion de la chaine entree en entier
while a:	# equivalent e : < while a != 0: >
  if a == 1:
      print("Vous avez choisi un :")
      print("le premier, l'unique, l'unité ...")
  elif a == 2:
      print("Vous preferez le deux :")
      print("la paire, le couple, le duo ...")
  elif a == 3:
      print("Vous optez pour le plus grand des trois :")
      print("le trio, la trinité, le triplet ...")
  else :
      print("Un nombre entre UN et TROIS, s.v.p.")
  print('Choisissez un nombre de 1 à 3 (ou 0 pour terminer) ', end =' ')
  a = int(input())
print("Vous avez entre zero :")
print("L'exercice est donc terminé.")
