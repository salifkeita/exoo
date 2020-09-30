def info_eleve():

    for i in range(2):
        nom = input(f"saisir le nom : ")
        prenom = input(f"saisir le prenom : ")
        age = input(f"votre age est: ") 
        classe = input("votre claase : ")
        fichier= open("info.txt","a")
        fichier.writelines(f"{nom} {prenom} {age}ans {classe} Année \n")
        fichier.close

    
def liste_info():
    fichier= open("info.txt","r")
    liste= fichier.readlines()
    for classe in liste:
        classe= classe.split(" ")
        print(f"Nom: {classe [0]}\nPrenom: {classe [1]}\nAge: {classe [2]}\nclasse:{classe [3]} {classe [4]} {classe [5]}")
    fichier.close


info_eleve()
liste_info()