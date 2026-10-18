def ft_filter(func, listing):
    '''
    La fonction filter prend une fonction et l'applique a une liste, tuple, etc
    Le but va etre de verifier le retour de chaque element par la fonction
    afin de retourner la liste repondant true a la fonction
    Si aucune fonction n'est passe, on verifie juste l'existence de chaque
    element
    '''
    if (func):
        return (obj for obj in listing if func(obj))
    return (obj for obj in listing if obj)
