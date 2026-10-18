import sys
from ft_filter import ft_filter


def main():
    '''
    La fonction doit prendre deux arguments : Arg1 -> str ; Arg2 -> int
    La str ne doit pas comporter de caractere speciaux sauf espace etant
     separateur
    Un lambda et un travail sur liste doit etre present. Le lambda permet\
    de creer une fonction ephemere tres simple comme ici on l'on va chercher a
    verifier si la longueur des mots est superieur a Arg2
    '''
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        assert all(c.isalnum() or c.isspace() for c in sys.argv[1]), \
            "the arguments are bad"
        try:
            lenght = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")
        words = sys.argv[1].split()
        words_trie = ft_filter(lambda x: len(x) > lenght, words)
        print(list(words_trie))
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
