import random
import string
import time


def generate_password():
    l_mdp = int(input('longueur du mdp: '))
    random_generator = random.SystemRandom()
    chars = string.ascii_letters + string.digits

    password = ""
    for i in range (l_mdp):
        password += random_generator.choice(chars)
    print("Voici votre mdp : ", password)

generate_password()
