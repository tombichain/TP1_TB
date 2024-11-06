minspend = int(input("Entrez les minutes écoulées depuis le début du mois : "))

jour = minspend // 1440

restediv1 = minspend % 1440

heure = restediv1 // 60

minute = restediv1 % 60


print("nous sommes le {} il est {}:{}.".format(jour, heure, minute))