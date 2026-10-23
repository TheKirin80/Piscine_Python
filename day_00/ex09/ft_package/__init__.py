# On importe la fonction depuis le fichier local count_in_list.py
from .count_in_list import count_in_list

# Optionnel : On définit explicitement ce qui est exporté par le package
__all__ = ["count_in_list"]