def info_eleve():

    for i in range(2):
        nom = input(f"saisir le nom : ")
        prenom = input(f"saisir le prenom : ")
        age = input(f"votre age est: ") 
        classe = input("votre claase : ")
        fichier= open("info.txt","a")
        fichier.writelines(f"{nom}{prenom}:{age} ans  : {classe} Année \n")
        fichier.close

    
info_eleve()