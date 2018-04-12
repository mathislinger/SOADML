# CLass for SOADML project

def get(lst, index, default=None):
    """
        Retourne l'élément de `lst` situé à `index`.
 
        Si aucun élément ne se trouve à `index`,
        retourne la valeur par défaut.
    """
    try:
        return lst[index]
    except IndexError:
        return default