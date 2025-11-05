if __name__ == '__ main __' :
    print('Hello World')

"""
    Format évènement
        description : fonction à switch (ou suite de if else) qui attend l'input de l'utilisateur pour lancer la suite du programme
        type de choix:
                        -options limitée (choix de dialogue)
                        -taper du texte (pour une énigme ?)
"""


"""
    Variables globale
        type: object
        description : ensemble des variables (boolean/int) des choix fait à chaque évènement.
        type de variable: 
                        -boolean (répond à une question oui/non ex:a parlé à tel PNJ)
                        -int (indique un élément cumulable global ex: or,potion de soin)
"""

"""
    Personage
        type: class object
        description : a chaque nouvelle partie crée un nouveaux personage
        variable : nom, PV, or en poche
"""

"""
    Aventure
        type: class 
        description : à chaque partie terminée ou échouée, crée une liste qui reprend
        variable : nom du personage, date, score, (chronologie des choix ?)
"""