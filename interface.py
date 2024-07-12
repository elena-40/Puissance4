def dessin_grille(rows, cols):
    # initialiser la grille comme une liste des listes

    grille =[[''for _ in range(cols)] for _ in range(rows)]

    # Imprimer les numeros de la colonne 

    print('  ', end='')
    for c in range(cols):
        print(f'  {c + 1} ', end='')
    print()


    # pour la premier ligne (noté +---+---) # Imprimer la grille avec les numéros de ligne
    for r in range(rows):
        print('  ', end='')
        for c in range(cols):
            print('+---', end='')
        print('+')


        ## # Ligne des cellules avec numéro de ligne au début
        print(f'{r + 1} ', end='')
        for c in range(cols):
            print(f'| {grille[r][c]}  ', end='')
        print('|')

    print('  ', end='')
    for c in range(cols):
        print('+---', end='')
    print('+')

def main():
    rows = 3
    cols = 3

    dessin_grille(rows, cols)

if __name__ == '__main__':
    main()