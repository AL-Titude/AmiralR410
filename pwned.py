import requests
import hashlib
import getpass

def verifier_mot_de_passe_pwned(mot_de_passe): 
    sha1_mot_de_passe = hashlib.sha1(mot_de_passe.encode('utf-8')).hexdigest().upper() 
    prefixe_sha1, suffixe_sha1 = sha1_mot_de_passe[:5], sha1_mot_de_passe[5:] 
    url_api = f"https://api.pwnedpasswords.com/range/{prefixe_sha1}" 
    
    try: 
        reponse = requests.get(url_api) 
        if reponse.status_code == 200: 
            suffixes_pwned = reponse.text.splitlines() 
            for suffixe in suffixes_pwned: 
                if suffixe.split(':')[0] == suffixe_sha1: 
                    return True 
            return False 
        
        else: 
            print("Erreur lors de la connexion au serveur.") 
    
    except requests.exceptions.RequestException as e:
        print("Une erreur s'est produite lors de la connexion au serveur:", e)
        return False 

mot_de_passe_utilisateur = getpass.getpass("Entrez votre mot de passe : ") 
if verifier_mot_de_passe_pwned(mot_de_passe_utilisateur):
    print("Ce mot de passe a été piraté plusieurs fois. Change moi ça et VITE !!!!.") 

else:
    print("Rien ici !! Mais ne garanti en rien ta sécurité.")

    