
def add_letter_numbder(lettre,number):
    """ 
    Cette fonction permet d'additionner une lettre et un nombre entier
    Elle renvoie la lettre dont la position corresponde a la position 
    de l'ancienne lettre plus le nombre
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    symbole="!@#$%^&*()_+1234567890-={|}[],<.>/?"
    position = 0
    for i in alphabet:
        if i == lettre:
            return alphabet[(position+number)%26]
            break
        else:
            position += 1


def algo_cryptage_de_cesare(phrase,cle):
    """
    Cette fonction permet de crypter un message avec une cle
    """
    message_crypte = []
    for lettre in phrase:
        message_crypte.append(add_letter_numbder(lettre,cle))
    message_crypte = "".join(message_crypte)
    return message_crypte




def algo_decryptage_de_cesare(phrase,cle):
    """
    Cette algo permet de decrypter un message avec une cle
    """
    message_decrypte = []
    for lettre in phrase:
        message_decrypte.append(add_letter_numbder(lettre,26-cle%26))
    message_decrypte="".join(message_decrypte)
    return message_decrypte




            
