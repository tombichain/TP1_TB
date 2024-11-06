jour = int(input("Entrez le jour : "))
heure = int(input("Entrez les heures : "))
minute = int(input("Entrez les minutes : "))

minspend = (jour*1440) + (heure*60) + minute

print("Le nombre de minutes écoulées depuis le début du mois est :" , minspend)