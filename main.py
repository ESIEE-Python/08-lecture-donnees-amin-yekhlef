#### Imports et définition des variables globales
#import random
import csv

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []

    with open(filename, mode='r', encoding='utf8') as f:

        l = list(csv.reader(f, delimiter=';'))

        for i in range(len(l)):
            l[i] = list(map(int, l[i]))

    return l

def get_list_k(data, k):

    return data[k]

def get_first(l):

    return l[0]

def get_last(l):

    return l[-1]

def get_max(l):

    return max(l)

def get_min(l):

    return min(l)

def get_sum(l):

    return sum(l)


#### Fonction principale


def main():

    data = read_data(FILENAME)

    for i, l in enumerate(data):
        print(i, l)


if __name__ == "__main__":
    main()
