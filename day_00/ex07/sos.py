import sys


def main():
    # Dictionnaire de correspondance entre caractères et code Morse
    NESTED_MORSE = {
        " ": "/ ",  # Espace traduit par slash
        "A": ".- ",   "B": "-... ", "C": "-.-. ", "D": "-.. ",
        "E": ". ",    "F": "..-. ", "G": "--. ",  "H": ".... ",
        "I": ".. ",   "J": ".--- ", "K": "-.- ",  "L": ".-.. ",
        "M": "-- ",   "N": "-. ",   "O": "--- ",  "P": ".--. ",
        "Q": "--.- ", "R": ".-. ",  "S": "... ",  "T": "- ",
        "U": "..- ",  "V": "...- ", "W": ".-- ",  "X": "-..- ",
        "Y": "-.-- ", "Z": "--.. ",
        "0": "----- ", "1": ".---- ", "2": "..--- ", "3": "...-- ",
        "4": "....- ", "5": "..... ", "6": "-.... ", "7": "--... ",
        "8": "---.. ", "9": "----. ",
    }
    '''
    Le but de ce programme est l'encodage en morse d'une string.
    La string est compose d'alphanumerique ainsi que d'espaces.
    Tout le reste entraine une AssertionError
    '''
    try:
        assert len(sys.argv[1]) == 2, "the arguments are bad"
        chain = sys.argv[1].upper()
        encode_chain=[]
        for c in chain:
            if c not in NESTED_MORSE:
                raise AssertionError("the arguments are bad")
            encode_chain.append(NESTED_MORSE[c])
        print(" ".join(encode_chain))

    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()