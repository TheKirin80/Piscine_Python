import sys


def main():
    texte = ""
    try:
        '''
        On va chercher ici a verifier s'il n'y a pas trop d'arguments,
        puis on va forcer l'utilisateur a nous mettre une chaine correcte
        s'il en pas deja passer plusieurs.
        Ensuite on va effectuer dans l'ordre le calcul des uppers, des lowers,
        des punctuations, des spaces et des digits et une addition globale
        '''
        assert len(sys.argv) <= 2, "more than one argument is provided"
        if (len(sys.argv) == 1):
            texte = input("What is the text to count?")
        else:
            texte = sys.argv[1]
        while texte == "":
            texte = input("What is the text to count?")
        print(f"{texte}")
        print(f"The text contains {sum(1 for c in texte)} characters:")
        print(f"{sum(c.isupper() for c in texte)} upper letters")
        print(f"{sum(c.islower() for c in texte)} lower letters")
        list_punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
        print(f"{sum(1 for c in texte if c in list_punctuation)} \
punctuation marks")
        print(f"{sum(c.isspace() for c in texte)} spaces")
        print(f"{sum(c.isdigit() for c in texte)} digits")
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
