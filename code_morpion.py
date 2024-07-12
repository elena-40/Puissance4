def dessin_grille(grille):
    rows = len(grille)
    cols = len(grille[0])

    # Imprimer les numéros de la colonne
    print('  ', end='')
    for c in range(cols):
        print(f'  {c + 1} ', end='')
    print()

    # Imprimer la grille avec les numéros de ligne
    for r in range(rows):
        print('  ', end='')
        for c in range(cols):
            print('+---', end='')
        print('+')

        print(f'{r + 1} ', end='')
        for c in range(cols):
            print(f'| {grille[r][c] or " "} ', end='')
        print('|')

    print('  ', end='')
    for c in range(cols):
        print('+---', end='')
    print('+')

def verifier_victoire(grille, joueur):
    # Vérifier les lignes
    for row in grille:
        if all(cell == joueur for cell in row):
            return True

    # Vérifier les colonnes
    for col in range(len(grille[0])):
        if all(row[col] == joueur for row in grille):
            return True

    # Vérifier les diagonales
    if all(grille[i][i] == joueur for i in range(len(grille))):
        return True
    if all(grille[i][len(grille)-1-i] == joueur for i in range(len(grille))):
        return True

    return False

def match_nul(grille):
    return all(cell for row in grille for cell in row)

def main():
    rows, cols = 3, 3
    grille = [['' for _ in range(cols)] for _ in range(rows)]
    joueurs = ['X', 'O']
    tour = 0

    while True:
        dessin_grille(grille)
        joueur = joueurs[tour % 2]
        print(f"Joueur {joueur}, c'est votre tour.")
        try:
            row = int(input(f"Choisissez une ligne (1-{rows}): ")) - 1
            col = int(input(f"Choisissez une colonne (1-{cols}): ")) - 1
            if grille[row][col]:
                print("Cette case est déjà occupée. Essayez encore.")
                continue
        except (ValueError, IndexError):
            print("Entrée invalide. Essayez encore.")
            continue

        grille[row][col] = joueur

        if verifier_victoire(grille, joueur):
            dessin_grille(grille)
            print(f"Félicitations, joueur {joueur}! Vous avez gagné!")
            break

        if match_nul(grille):
            dessin_grille(grille)
            print("Match nul!")
            break

        tour += 1

if __name__ == '__main__':
    main()
