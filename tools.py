#Utilisé pour la gestion de la file de priorité utilisée dans la construction de l'arbre de Huffman.
import heapq
#Utilisé pour calculer les fréquences des caractères dans le texte de manière efficace.
from collections import defaultdict

class Noeud:
    """
    Classe représentant un noeud dans l'arbre de Huffman.

    Attributes:
    - char (str): Le caractère associé au noeud (None pour les noeuds internes).
    - freq (int): La fréquence du caractère dans le texte.
    - gauche (Noeud): Le noeud fils gauche.
    - droite (Noeud): Le noeud fils droit.
    - identifiant (int): Identifiant du noeud.
    """

    def __init__(self, char, freq):
        """
        Initialise un objet Noeud avec un caractère et une fréquence.

        Args:
        - char (str): Le caractère associé au noeud.
        - freq (int): La fréquence du caractère dans le texte.
        """
        self.char = char
        self.freq = freq
        self.gauche = None
        self.droite = None
        self.identifiant = None
        
    def __lt__(self, autre):
        """
        Définit l'ordre de comparaison entre deux noeud en fonction de leur fréquence.

        Args:
        - autre (Noeud): L'autre noeud à comparer.

        Returns:
        - bool: True si la fréquence du noeud actuel est inférieure à celle de l'autre noeud, False sinon.
        """
        return self.freq < autre.freq

def construire_arbre_huffman(texte):
    """
    Construit l'arbre de Huffman pour un texte donnée.

    Args:
    - texte (str): Le texte pour lequel construire l'arbre.

    Returns:
    - file_prioritaire[0]: Le noeud racine de l'arbre de Huffman.
    """
    frequence = defaultdict(int)

    # Calcul des fréquences des caractères dans le texte
    for char in texte:
        frequence[char] += 1

    # Création d'une files de prioritée pour les noeuds feuille
    file_prioritaire = [Noeud(char, freq) for char, freq in frequence.items()]
    heapq.heapify(file_prioritaire)

    identifiant = 0
    # Construction de l'arbre de Huffman à partir de la file de prioritée
    while len(file_prioritaire) > 1:
        noeud_gauche = heapq.heappop(file_prioritaire)
        noeud_droite = heapq.heappop(file_prioritaire)

        noeud_interne = Noeud(None, noeud_gauche.freq + noeud_droite.freq)
        noeud_interne.gauche = noeud_gauche
        noeud_interne.droite = noeud_droite

        identifiant += 1
        setattr(noeud_interne, 'identifiant', identifiant)
        
        heapq.heappush(file_prioritaire, noeud_interne)

    return file_prioritaire[0]

def encoder_huffman(texte):
    """
    Encode un texte en utilisant l'algorithme de Huffman.

    Args:
    - texte (str): Le texte à encoder.

    Returns:
    - texte_encode: Le texte encodé.
    - codes: Un dictionnaire de correspondance entre les caractères et leurs codes binaire.
    """
    racine = construire_arbre_huffman(texte)
    codes = construire_codes_huffman(racine)

    texte_encode = ''.join(codes[char] for char in texte)
    return texte_encode, codes

def decoder_huffman(texte_encode, codes):
    """
    Décode un texte encodé en utilisant les codes de Huffman.

    Args:
    - texte_encode (str): Le texte encodé.
    - codes (dict): Le dictionnaire de correspondance entre les caractères et leurs codes binaires.

    Returns:
    - texte_decode: Le texte décodé.
    """
    correspondance_inverse = {code: char for char, code in codes.items()}

    code_courant = ""
    texte_decode = ""

    # Parcourt les bits du texte encodé et les décode en caractères
    for bit in texte_encode:
        code_courant += bit
        if code_courant in correspondance_inverse:
            texte_decode += correspondance_inverse[code_courant]
            code_courant = ""

    return texte_decode

def construire_codes_huffman(noeud, code="", mapping=None):
    """
    Construit un dictionnaire de correspondance entre les caractères et leurs codes binaires.

    Args:
    - noeud (Noeud): Le noeud de départ dans l'arbre de Huffman.
    - code (str): Le code binaire actuel (utilisé lors de la récursion).
    - mapping (dict): Le dictionnaire de correspondance (utilisé lors de la récursion).

    Returns:
    - mapping: Le dictionnaire de correspondance entre les caractères et leurs codes binaires.
    """
    if mapping is None:
        mapping = {}

    if noeud.char is not None:
        mapping[noeud.char] = code
    if noeud.gauche is not None:
        construire_codes_huffman(noeud.gauche, code + "0", mapping)
    if noeud.droite is not None:
        construire_codes_huffman(noeud.droite, code + "1", mapping)

    return mapping

# # Exemple d'utilisation
# texte = "bonjour le monde"
# texte_encode, codes_huffman = encoder_huffman(texte)
# print(f"codes_huffman = {codes_huffman}")
# texte_decode = decoder_huffman(texte_encode, codes_huffman)
# 
# print(f"Texte original: {texte}")
# print(f"Texte encodé: {texte_encode}")
# print(f"Texte décodé: {texte_decode}")
