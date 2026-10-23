import os


def ft_tqdm(lst: range) -> None:
    '''
    On cherche ici a reproduire la fonction tqdm original.
    tqdm sert a faire apparaitre une barre de progression dynamique et
    intelligente sur une action en cours.
    Dans un soucis d'authenticite nous allons dynamiquement change la taille
    du chargement en fonction de la taille du terminal

    '''
    total = len(lst)
    if total == 0:
        return
    start_time = os.times()[4]
    for i, object in enumerate(lst, start=1):
        # yield permet de freeze l'avance un par un plutot
        # qu'un bloc comme return
        yield object
        # Pour eviter trop d'appel sys, on va lui faire un update tout
        # les 10 tours
        if i == 1 or i % 10 == 0 or i == total:
            try:
                terminal_len, _ = os.get_terminal_size()
            except OSError:
                terminal_len = 42
        current_time = os.times()[4]
        # Calcul du temps passe depuis le debut
        elapsed_time = current_time - start_time
        # Calcul de la vitesse (itérations par seconde)
        if elapsed_time > 0:
            vitesse = i / elapsed_time
        else:
            vitesse = 0.0
        # Calcul du temps restant estime
        if vitesse > 0:
            eta = (total - i) / vitesse
        else:
            eta = 0.0

        # Formatage du temps écoulé et restant en MM:SS
        min_elapsed, sec_elapsed = divmod(int(elapsed_time), 60)
        min_eta, sec_eta = divmod(int(eta), 60)
        temps_ecoule = f"{min_elapsed:02d}:{sec_elapsed:02d}"
        temps_restant = f"{min_eta:02d}:{sec_eta:02d}"
        # Preparation de l'entourage du chargement
        progression = int((i / total) * 100)
        txt_gauche = f"{progression}%|["
        txt_droite = f"]| {i}/{total} [{temps_ecoule}<{temps_restant}\
, {vitesse:.2f}it/s]"
        # Calcul de l'espace pour le chargement
        charg_len = terminal_len - len(txt_gauche) - len(txt_droite) - 1
        # Protection pour chargement trop petit
        if charg_len < 1:
            charg_len = 1
        rempli = int(charg_len * i // total)
        if rempli > 0:
            barre = "=" * (rempli - 1) + ">"
        else:
            barre = ">"
        barre += " " * (charg_len - len(barre))
        # Assemblage final
        statut = f"\r{txt_gauche}{barre}{txt_droite}"
        # Affichage en supprimant les \n auto de print en fin ainsi
        # qu'en demandant un print sans remplissage complet du tampon
        # via le flush
        print(statut, end="", flush=True)
